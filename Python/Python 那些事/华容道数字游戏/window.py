import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication

class NumberHuaRong(QWidget):
    """华容道主体"""
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # 设置宽和高
        self.setFixedSize(400,400)
        # 设置标题
        self.setWindowTitle("数字华容道")
        # 设置背景颜色
        self.setStyleSheet("background-color:gray;")
        self.show()

class Block(QLabel):
    """数字方块"""
    def __init__(self,number):
        super().__init__()

        self.number = number
        self.setFixedSize(80,80)

        # 设置字体
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)

        # 设置字体颜色
        pa = QPalette()
        pa.setColor(QPalette.WindowText,Qt.white)
        self.setPalette(pa)

        # 设置文字位置
        self.setAlignment(Qt.AlienCenter)

        # 设置背景颜色、圆角和文本内容
        if self.number == 0:
            self.setStyleSheet("background-color:white;border-radius:10px;")
        else:
            self.setStyleSheet("background-color:red;border-radius:10px;")
            self.setText(str(self.number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberHuaRong()
    sys.exit(app.exec_())