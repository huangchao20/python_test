import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.move(200, 300)
win.resize(450, 450)
win.setWindowTitle('尼古拉斯.找死')
win.windowTitle()
win.show()

sys.exit(app.exec_())