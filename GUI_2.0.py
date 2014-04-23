import sys
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from ui_mainwindow import Ui_MainWindow
from sip import *

def main():
    app = QApplication(sys.argv)
    window = QDialog()
    mainmenu = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainmenu)
    
    mainmenu.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()