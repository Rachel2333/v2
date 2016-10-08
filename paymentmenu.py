# payment menu 

import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "paymentmenu.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class payment(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.new_payment_button.clicked.connect(self.new_payment_button_)
        self.view_payment_button.clicked.connect(self.view_payment_button_)

        
    
    def new_payment_button_(self):  
        os.system('new_payment.py')
    def view_payment_button_(self): 
        os.system('view_search_payment.py')
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = payment()
    window.show()
    

    sys.exit(app.exec_())