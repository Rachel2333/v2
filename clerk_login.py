# Login window Clerk

import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "login2.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ClerkLogin(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.login_button.clicked.connect(self.login_button_)

    def login_button_(self):
        os.system('clerk_menu.py') 
       
      
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = ClerkLogin()
    window.show()
    sys.exit(app.exec_())
    