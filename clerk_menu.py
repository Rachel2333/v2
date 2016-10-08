
# clerk menu 

import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "clerkmenu.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ClerkMenu(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.profile_button.clicked.connect(self.profile_button_)
        self.payment_button.clicked.connect(self.payment_button_)
        self.print_button.clicked.connect(self.print_button_)
        self.checkin_button.clicked.connect(self.checkin_button_)
        self.camp_button.clicked.connect(self.camp_button_)
        self.bunkhouse_button.clicked.connect(self.bunkhouse_button_)
        self.tribe_button.clicked.connect(self.tribe_button_)
        self.cancellation_button.clicked.connect(self.cancellation_button_)
        self.refund_button.clicked.connect(self.refund_button_)

    def profile_button_(self):
        os.system('create_profile.py')   
    def payment_button_(self):
        os.system('paymentmenu.py') 
    def print_button_(self):
        os.system('print_letter.py') 
    def checkin_button_(self):
        os.system('checkin_menu.py')
    def camp_button_(self):
        pass
    def bunkhouse_button_(self):
        pass
    def tribe_button_(self):
        pass
    def cancellation_button_(self):
        pass
    def refund_button_(self):
        pass 
   
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = ClerkMenu()
    window.show()
    sys.exit(app.exec_())
    