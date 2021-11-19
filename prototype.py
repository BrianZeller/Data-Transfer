import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *


from NewWindow import Ui_MainWindow

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = error_UI()
        self.ui.setupUi(self)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def dialogbox(self):
        self.hide()
        self.myDialog = MyDialog()
        self.myDialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())