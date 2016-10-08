
# Maintenance_ login 
import sys
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "login3.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class Maintenance_Login(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Maintenance_Login()
    window.show()
    sys.exit(app.exec_())
    