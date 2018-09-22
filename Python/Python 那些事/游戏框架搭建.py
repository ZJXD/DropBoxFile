import sys
from PyQt5.QtWidgets import QWidget, QApplication

class NumberHuaRong(QWidget):
    """ 华容道主体 """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置宽和高
        self.setFixedSize(400, 400)
        # 设置标题
        self.setWindowTitle('数字华容道')
        # 设置背景颜色
        self.setStyleSheet("background-color:gray;")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberHuaRong()
    sys.exit(app.exec_())