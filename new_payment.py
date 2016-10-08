# new payment record 
import sys
import os 
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "newpayment.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class newpayment(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.save_button.clicked.connect(self.save_button_)
        self.cancel_button.clicked.connect(self.cancel_button_)
       
    def save_button_(self):  
        # check all fields filled 
        # check for spacific conditions 
        # save info into the database 
        #show conformation message
        pass

    def cancel_button_(self):
        os.system('paymentmenu.py')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = newpayment()
    window.show()
    sys.exit(app.exec_())