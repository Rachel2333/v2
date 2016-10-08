
# checkin menu 
import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "checkinmenu.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Checkin(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.search_checkin_button.clicked.connect(self.search_checkin_button_)
        self.view_checkin_button.clicked.connect(self.view_checkin_button_)
        self.new_checkin_button.clicked.connect(self.new_checkin_button_)
    
    def search_checkin_button_(self):  
        os.system('search_checkin.py')
    def view_checkin_button_(self):
            # I dont know where should go 
            pass
    def new_checkin_button_(self):
       os.system('new_checkin.py')
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Checkin()
    window.show()
    sys.exit(app.exec_())