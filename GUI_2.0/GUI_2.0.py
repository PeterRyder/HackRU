import sys
from PyQt4.QtGui import QApplication, QDialog
from ui_imagedialog import *  # here you need to correct the names

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Application()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())