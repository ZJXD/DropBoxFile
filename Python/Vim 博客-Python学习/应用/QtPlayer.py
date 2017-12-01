# There is no Phonon in Qt5. New QtMultimedia module should be used:
# Written by ZHT

import time
import sys
import PyQt5.QtCore as c
import PyQt5.QtGui as g
import PyQt5.QtWidgets as QW
import PyQt5.QtMultimedia as m

class PollTimeThread(c.QThread):
    """
    This thread works as a timer
    """
    update = c.pyqtSignal()

    def __init__(self,parent):
        super(PollTimeThread,slf).__init__(parent)

    def run(self):
        while True:
            time.sleep(1)
            if self.isRunning():
                # emit signal
                self.updata.emit()

            else:
                return

class Window(QW):
    def __init__(self):
        QW.__init__(self)

        # media
        self.media = m.MediaObject(self)
        self.media.stateChanged.connect(self.handleStateChanged)
        self.video = m.VideoWidget(self)
        self.video.setMinimumSize(200,200)
        self.audio = m.AudioOutput(m.VideoCategory,self)
        m.createPath(self.media,self.audio)
        m.createPath(self.media,self.video)

        # control button
        self.button = g.QPushButton('选择文件',self)
        self.button.clicked.connect(self.handleButton)

        # for display of time lapse
        self.info = g.QLable(self)

        # layout
        layout = g.QGridLayout(self)
        layout.addWidget(self.video,1,1,3,3)
        layout.addWidget(self.info,4,1,1,3)
        layout.addWidget(self.button,5,1,1,3)

        # signal-solt,for time lapse
        self.thread = PollTimeThread(self)
        self.thread.update.connect(self.update)

    def update(self):
        # slot
        lapse = self.media.currentTime()/1000.0
        self.info.setText("%4.2f 秒" % lapse)

    def startPlay(self):
        if self.path:
            self.media.setCurrentSource(m.MediaSource(self.path))

            # use a thread as a timer
            self.thread = PollTimeThread(self)
            self.thread.update.connect(self.update)
            self.thread.start()
            self.media.play()

    def handleButton(self):
        if self.media.state() == m.PlayingState:
            self.media.stop()
            self.thread.terminate()
        else:
            self.path = g.QFileDialog.getOpenFileName(self,self.button.text())
            self.startPlay()

    def handleStateChanged(self,newstate,oldstate):
        if newstate == m.PlayingState:
            self.button.setText('停止')
        elif(newstate != m.LoadingState and newstate != m.BufferingState):
            self.button.setText('选择文件')
            if newstate == m.ErrorState:
                source = self.media.currentSource().fileName()
                print('错误：不能播放：',source.toLocal8Bit().data())
                print(' %s' % self.media.errorString().toLocal8Bit().data())

if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    app.setApplicationName('视频播放')
    window = Window()
    window.show()
    sys.exit(app.exec_())
