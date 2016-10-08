# search/ view payment record 

import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "searchpayment.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class View_search_payment (QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.search_button.clicked.connect(self.search_button_)
        self.cancel_button.clicked.connect(self.cancel_button_)
        
    def search_button_(self):  
        # fetch data from the data base 
        # show data to the user 
        pass 

    def cancel_button_(self):  
        os.system('paymentmenu.py')
    
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = View_search_payment()
    window.show()
    sys.exit(app.exec_())