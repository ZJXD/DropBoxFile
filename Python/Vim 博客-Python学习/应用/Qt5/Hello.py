import sys
from PyQt5 import (QtWidgets,QtCore)

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(500,200)
widget.setWindowTitle("Hello,PyQt5!")
widget.show()
sys.exit(app.exec_())

