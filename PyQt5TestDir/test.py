import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QWidget, \
    QLabel, QPushButton, QHBoxLayout, QLayout, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()

    def creatUser(self):
        li = []


    def initGui(self):
        self.setWindowTitle('打雷了，下雨了，收衣服了')
        self.move(300, 150)
        self.resize(500, 300)

        menu = self.menuBar()
        add_menu = menu.addMenu('添加')
        add_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        add_file1 = QAction('赵一', self)
        add_file1.setStatusTip('赵大娃儿')
        add_file2 = QAction('赵二', self)
        add_file2.setStatusTip('赵二娃')
        add_file3 = QAction('赵三', self)
        add_file3.setStatusTip('赵可猫儿')
        add_file4 = QAction('赵四', self)
        add_file4.setStatusTip('赵四儿')
        add_file5 = QAction('赵五', self)
        add_file5.setStatusTip('赵五儿')
        add_file6 = QAction('赵六', self)
        add_file6.setStatusTip('赵陆儿')
        # add_file_file = QAction('赵三的小蜜')
        # add_file_file.setStatusTip('小三哥')
        add_menu.addAction(add_file1)
        add_menu.addAction(add_file2)
        add_menu.addAction(add_file3)
        add_menu.addAction(add_file4)
        add_menu.addAction(add_file5)
        add_menu.addAction(add_file6)
        # add_file3.addAction(add_file_file)

        edit_file = QAction('茅斯里头打亮壶儿', self)
        edit_file.setStatusTip('你丫的赵石')
        edit_file.triggered.connect(self.close)
        edit_file.setShortcut('Ctrl+D')
        edit_menu.addAction(edit_file)

        self.statusBar().showMessage("菜英文，他不是人")


class guiTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.GuiTest()
        self.testQLable()

    def CreateTitle(self, listtitle, listotitle, menu):
        tt = 'titlename'
        for i in range(len(listtitle)):
            t = tt.format(i)
            t = QAction(listtitle[i], self)
            t.setStatusTip(listotitle[i])
            print(listtitle[i], listotitle[i])
            # print(t)
            menu.addAction(t)
        return menu

    def GuiTest(self):
        listtitle = ['尼古拉斯', '野猪', '南离', '合欢', '魔泷', '独霸天', '野猪林']
        listotitle= ['赵四', '佩琪', '道人', '老尼', '争霸', '老贼', '出野猪']
        del_list= ['就是删除', '你能', '把我', '怎么滴']
        del_name = ['傻叉', '盘尼', '往死里盘', '滴滴一下']
        self.resize(600, 400)
        self.setWindowTitle('继续小英文')
        menu = self.menuBar()
        add_menu = menu.addMenu('file')
        add_menu.addSeparator()
        del_menu = menu.addMenu('del')
        self.CreateTitle(listtitle, listotitle, add_menu)
        self.CreateTitle(del_list, del_name, del_menu)
        self.statusBar().showMessage('小英子，他不是淫')

    def testQLable(self):
        menubarh = self.menuBar().height()
        lab = QLabel('第一个标签', self)
        lab.move(10, menubarh)
        lab2 = QLabel('第二个标签', self)
        lab2.move(10, menubarh * 2)

        but1 = QPushButton('按钮1', self)
        but2 = QPushButton('按钮2', self)
        but3 = QPushButton('按钮3', self)
        # but1.move(lab.width(), menubarh)
        # but2.move(lab2.width(), menubarh * 2)
        # pass

        """
        #水平摆放
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox1.addWidget(lab)
        hbox1.addWidget(but1)

        hbox2.addWidget(lab2)
        hbox2.addWidget(but2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)
        self.setCentralWidget(layout_widget)
        """

        #网格
        gride = QGridLayout()
        gride.addWidget(lab, 0, 0)
        gride.addWidget(but1, 0, 1)
        gride.addWidget(lab2, 1, 0)
        gride.addWidget(but2, 1, 1)
        gride.addWidget(but3, 2, 0, 1, 5)
        #指定表格的对齐方式...
        gride.setAlignment(Qt.AlignLeft)
        # gride.setAlignment(Qt.AlignRight)
        # gride.setAlignment(Qt.AlignTop)
        # gride.setAlignment(Qt.AlignCenter)
        lay_weight = QWidget()
        lay_weight.setLayout(gride)
        self.setCentralWidget(lay_weight)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = guiTest()
    gui.show()

    sys.exit(app.exec_())