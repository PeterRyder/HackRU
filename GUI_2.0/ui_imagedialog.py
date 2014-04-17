# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui.ui'
#
# Created: Mon Apr 14 13:17:25 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName(_fromUtf8("Application"))
        Application.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Application)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(Application)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtGui.QLabel(Application)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(Application)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.checkBox = QtGui.QCheckBox(Application)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Application)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Application)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(Application)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Application)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(Application)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Application)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Application)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Application)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Application)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Application)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 2)

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        Application.setWindowTitle(_translate("Application", "Dialog", None))
        self.pushButton.setText(_translate("Application", "Choose Folder", None))
        self.label.setText(_translate("Application", "Select Time Frame", None))
        self.comboBox.setItemText(0, _translate("Application", "Days", None))
        self.comboBox.setItemText(1, _translate("Application", "Months", None))
        self.comboBox.setItemText(2, _translate("Application", "Years", None))
        self.checkBox.setText(_translate("Application", "Log", None))
        self.label_2.setText(_translate("Application", "Age of File", None))
        self.checkBox_2.setText(_translate("Application", "Show Log", None))
        self.label_3.setText(_translate("Application", "Select File Size", None))
        self.comboBox_2.setItemText(0, _translate("Application", "Bytes", None))
        self.comboBox_2.setItemText(1, _translate("Application", "Kilobytes", None))
        self.comboBox_2.setItemText(2, _translate("Application", "Megabytes", None))
        self.comboBox_2.setItemText(3, _translate("Application", "Gigabytes", None))
        self.comboBox_2.setItemText(4, _translate("Application", "Terabytes", None))
        self.label_4.setText(_translate("Application", "File Size", None))
        self.label_5.setText(_translate("Application", "Ignore List", None))

