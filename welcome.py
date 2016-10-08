# WELCOME PAGE : CHOOSE Maintenance or Clerk 

import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "login1.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Maintenance_button.clicked.connect(self.Maintenance_button_) 
        self.Clerk_button.clicked.connect(self.Clerk_button_)
    
    def Clerk_button_(self):  # when cleck on Clerk button, it runs GUI1.py file ( the window of login for Clerk )
        os.system('Clerk_login.py')
    def Maintenance_button_(self): # when cleck on Maintenance button, it runs GUI2.py file ( the window of login for Maintenance)
       os.system('maintenance_login.py')
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    

    sys.exit(app.exec_())
    