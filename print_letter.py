# print Acceptance / dinel letter 

import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Print_letter(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
                


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = print_letter()
    window.show()
    sys.exit(app.exec_())