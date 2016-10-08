import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "searchcheckin.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class SerchCheckin(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.search_button.clicked.connect(self.search_button_)
        self.cancel_button.clicked.connect(self.cancel_button_)
    def search_button_(self):  
        #check not empty fields
        #check for specfic conditions 
        # fetch info from the database 
        # show info 
        pass
    def cancel_button_(self): 
       os.system('checkin_menu.py')
           
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = SerchCheckin()
    window.show()
    sys.exit(app.exec_())