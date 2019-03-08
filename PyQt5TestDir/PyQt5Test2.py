import sys
from PyQt5.QtWidgets import QApplication,QWidget,QAction,QMainWindow

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        # self.win = QWidget()
        self.setWindowTitle('遭不住的狗二娃')

class GUi(QApplication):
    def __init__(self):
        self.InitU()

    def InitU(self):
        self.win = QWidget()
        self.win.setWindowTitle("赵二黑不黑")
        self.win.backgroundRole()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = GUI()
#     gui.win.show()
#     sys.exit(app.exec_())

# coding:utf-8
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# class GUi():
#     def __init__(self):
#         self.initUI()
#     def initUI(self):
#         self.win = QWidget()
#         self.win.setWindowTitle('州的先生Zmister.com GUI教程')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = GUi()
#     gui.win.show()
#     sys.exit(app.exec_())

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.guiInitGui()

    def guiInitGui(self):
        self.setWindowTitle('卷心菜英文')
        self.resize(450, 450)
        self.move(400, 100)

        menu = self.menuBar()
        file_menu = menu.addMenu("说是文件")
        file_menu.addSeparator()
        edit_menu = menu.addMenu('想玩吗')

        new_file1 = QAction('小英文黢黑', self)
        new_file2 = QAction('滚粗吧', self)
        new_file3 = QAction('小艾淫', self)
        new_file4 = QAction('小英文黢黑', self)
        new_file = QAction('黑包子，图狼狗', self)
        new_file1.setStatusTip('小英文1')
        new_file2.setStatusTip('小英文2')
        new_file3.setStatusTip('小英文3')
        new_file4.setStatusTip('小英文4')
        new_file.setStatusTip('小英文')
        file_menu.addAction(new_file1)
        file_menu.addAction(new_file2)
        file_menu.addAction(new_file3)
        file_menu.addAction(new_file4)
        file_menu.addAction(new_file)

        # file_menu.setStatusTip('滚粗吧，小艾淫')

        self.statusBar().showMessage("菜英文，他不是人")

        edit_file = QAction('玩你麻痹嗨', self)
        edit_file.setStatusTip('要滚了吗')
        edit_file.triggered.connect(self.close)
        edit_file.setShortcut('Ctrl+Q')
        edit_menu.addAction(edit_file)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # gui = GUI()
    # gui.show()
    #
    # sys.exit(app.exec_())
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()

    sys.exit(app.exec_())