import sys
from PyQt4.QtGui import QApplication, QDialog, QMainWindow
from ui_mainwindow import *  # here you need to correct the names

app = QApplication(sys.argv)
window = QDialog()
mainmenu = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainmenu)

mainmenu.show()
sys.exit(app.exec_())