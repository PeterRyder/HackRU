# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Apr 17 12:32:10 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from files import *
from sip import *

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.folderWasChosen = False
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(803, 462)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.timeFrame = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeFrame.sizePolicy().hasHeightForWidth())
        self.timeFrame.setSizePolicy(sizePolicy)
        self.timeFrame.setObjectName(_fromUtf8("timeFrame"))
        self.timeFrame.addItem(_fromUtf8(""))
        self.timeFrame.addItem(_fromUtf8(""))
        self.timeFrame.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.timeFrame, 0, 2, 1, 1)
        self.fileSizeType = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileSizeType.sizePolicy().hasHeightForWidth())
        self.fileSizeType.setSizePolicy(sizePolicy)
        self.fileSizeType.setObjectName(_fromUtf8("fileSizeType"))
        self.fileSizeType.addItem(_fromUtf8(""))
        self.fileSizeType.addItem(_fromUtf8(""))
        self.fileSizeType.addItem(_fromUtf8(""))
        self.fileSizeType.addItem(_fromUtf8(""))
        self.fileSizeType.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.fileSizeType, 2, 2, 1, 1)
        self.ignoreList = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignoreList.sizePolicy().hasHeightForWidth())
        self.ignoreList.setSizePolicy(sizePolicy)
        self.ignoreList.setObjectName(_fromUtf8("ignoreList"))
        self.gridLayout_2.addWidget(self.ignoreList, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.deselectAllRemove = QtGui.QPushButton(self.centralwidget)
        self.deselectAllRemove.setObjectName(_fromUtf8("deselectAllRemove"))
        self.gridLayout_2.addWidget(self.deselectAllRemove, 1, 3, 1, 1)
        self.chooseFolder = QtGui.QPushButton(self.centralwidget)
        self.chooseFolder.setObjectName(_fromUtf8("chooseFolder"))
        self.gridLayout_2.addWidget(self.chooseFolder, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.fileAge = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileAge.sizePolicy().hasHeightForWidth())
        self.fileAge.setSizePolicy(sizePolicy)
        self.fileAge.setObjectName(_fromUtf8("fileAge"))
        self.gridLayout_2.addWidget(self.fileAge, 1, 2, 1, 1)
        self.cancel = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.gridLayout_2.addWidget(self.cancel, 11, 5, 1, 1)
        self.commit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commit.sizePolicy().hasHeightForWidth())
        self.commit.setSizePolicy(sizePolicy)
        self.commit.setObjectName(_fromUtf8("commit"))
        self.gridLayout_2.addWidget(self.commit, 11, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 1, 1, 1)
        self.deselectAllIgnore = QtGui.QPushButton(self.centralwidget)
        self.deselectAllIgnore.setObjectName(_fromUtf8("deselectAllIgnore"))
        self.gridLayout_2.addWidget(self.deselectAllIgnore, 1, 5, 1, 1)
        self.fileSize = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileSize.sizePolicy().hasHeightForWidth())
        self.fileSize.setSizePolicy(sizePolicy)
        self.fileSize.setObjectName(_fromUtf8("fileSize"))
        self.gridLayout_2.addWidget(self.fileSize, 3, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 383, 314))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 3, 9, 3)
        self.selectAllRemove = QtGui.QPushButton(self.centralwidget)
        self.selectAllRemove.setObjectName(_fromUtf8("selectAllRemove"))
        self.gridLayout_2.addWidget(self.selectAllRemove, 0, 3, 1, 1)
        self.selectAllIgnore = QtGui.QPushButton(self.centralwidget)
        self.selectAllIgnore.setObjectName(_fromUtf8("selectAllIgnore"))
        self.gridLayout_2.addWidget(self.selectAllIgnore, 0, 5, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 1, 1, 1)
        self.log = QtGui.QCheckBox(self.centralwidget)
        self.log.setObjectName(_fromUtf8("log"))
        self.gridLayout_2.addWidget(self.log, 8, 0, 1, 1)
        self.showLog = QtGui.QCheckBox(self.centralwidget)
        self.showLog.setObjectName(_fromUtf8("showLog"))
        self.gridLayout_2.addWidget(self.showLog, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_Folder = QtGui.QAction(MainWindow)
        self.actionChoose_Folder.setObjectName(_fromUtf8("actionChoose_Folder"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionChoose_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.chooseFolder, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update)
        QtCore.QObject.connect(self.commit, QtCore.SIGNAL(_fromUtf8("clicked()")), self.commitFunc)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.selectAllRemove, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectAllRemoveFunc)
        QtCore.QObject.connect(self.deselectAllRemove, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deselectAllRemoveFunc)
        QtCore.QObject.connect(self.deselectAllIgnore, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deselectAllIgnoreFunc)
        QtCore.QObject.connect(self.selectAllIgnore, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectAllIgnoreFunc)
        self.log.click()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #self.menuFile.menuAction.triggered.connect(QtGui.qApp.quit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Reinigen", "Reinigen", None))
        self.timeFrame.setItemText(0, _translate("MainWindow", "Days", None))
        self.timeFrame.setItemText(1, _translate("MainWindow", "Months", None))
        self.timeFrame.setItemText(2, _translate("MainWindow", "Years", None))
        self.fileSizeType.setItemText(0, _translate("MainWindow", "Bytes", None))
        self.fileSizeType.setItemText(1, _translate("MainWindow", "Kilobytes", None))
        self.fileSizeType.setItemText(2, _translate("MainWindow", "Megabytes", None))
        self.fileSizeType.setItemText(3, _translate("MainWindow", "Gigabytes", None))
        self.fileSizeType.setItemText(4, _translate("MainWindow", "Terabytes", None))
        self.label_3.setText(_translate("MainWindow", "Select File Size", None))
        self.deselectAllRemove.setText(_translate("MainWindow", "Deselect All Remove", None))
        self.chooseFolder.setText(_translate("MainWindow", "Choose Folder", None))
        self.label.setText(_translate("MainWindow", "Select Time Frame", None))
        self.fileAge.setText(_translate("MainWindow", "1", None))
        self.cancel.setText(_translate("MainWindow", "Cancel", None))
        self.commit.setText(_translate("MainWindow", "OK", None))
        self.label_2.setText(_translate("MainWindow", "Age of File", None))
        self.label_5.setText(_translate("MainWindow", "Ignore List", None))
        self.deselectAllIgnore.setText(_translate("MainWindow", "Deselect All Ignore", None))
        self.fileSize.setText(_translate("MainWindow", "1", None))
        self.label_4.setText(_translate("MainWindow", "File Size", None))
        self.selectAllRemove.setText(_translate("MainWindow", "Select All Remove", None))
        self.selectAllIgnore.setText(_translate("MainWindow", "Select All Ignore", None))
        self.label_7.setText(_translate("MainWindow", "Config Options", None))
        self.log.setText(_translate("MainWindow", "Log", None))
        self.showLog.setText(_translate("MainWindow", "Show Log", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionChoose_Folder.setText(_translate("MainWindow", "Choose Folder", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

    def update(self):
        self.folderWasChosen = True
        
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        
        folder_path = str(QtGui.QFileDialog.getExistingDirectory())
        
        time_frame = str(self.timeFrame.currentText())
        file_size_type = str(self.fileSizeType.currentText())
        file_age = int(self.fileAge.text())
        file_size = int(self.fileSize.text())
        ignore_list = str(self.ignoreList.text())
        
        #print "Time Frame: " + time_frame
        #print "File Size Type: " + file_size_type
        #print "File Age: " + file_age
        #print "File Size: " + file_size
        #print "Ignore List: " + ignore_list
        
        day_amount = 0
        if (time_frame == "Days"):
            day_amount = 1
        elif (time_frame == "Months"):
            day_amount = 31
        elif (time_frame == "Years"):
            day_amount = 365
        
        size_multiplier = 0
        if (file_size_type == "Bytes"):
            size_multiplier = 0
        if (file_size_type == "Kilobytes"):
            size_multiplier = 1
        elif (file_size_type == "Megabytes"):
            size_multiplier = 2
        elif (file_size_type == "Gigabytes"):
            size_multiplier = 3
        elif (file_size_type == "Terabytes"):
            size_multiplier = 4        
        
        temp_string = []
        if ignore_list != '':
            temp_string = ignore_list.strip(" ")
            temp_string = ignore_list.split(',')        
        
        self.inputData = Files(folder_path, file_age, day_amount, file_size, size_multiplier, temp_string)
        
        self.inputData.traverse()
        #self.inputData.printIt()
        
        i = 1
        self.radioGroup = []
        for item in self.inputData.deleteFiles:
            #print item
            
            
            radioButtons = QtGui.QButtonGroup(self.scrollAreaWidgetContents)
            
            removeButton = QtGui.QRadioButton(self.scrollAreaWidgetContents)
            removeButton.setObjectName(_fromUtf8("removeButton"))
            removeButton.setText(_translate("MainWindow", "Remove", None))
            radioButtons.setObjectName(_fromUtf8("radioButtons"))
            
            self.gridLayout.addWidget(removeButton, i, 1, 1, 1)
            
            addToBlacklist = QtGui.QRadioButton(self.scrollAreaWidgetContents)
            addToBlacklist.setObjectName(_fromUtf8("addToBlacklist"))
            addToBlacklist.setText(_translate("MainWindow", "Add to Blacklist", None))
            radioButtons.setObjectName(_fromUtf8("radioButtons"))
            
            self.gridLayout.addWidget(addToBlacklist, i, 2, 1, 1)            
            
            
            ignoreButton = QtGui.QRadioButton(self.scrollAreaWidgetContents)
            ignoreButton.setObjectName(_fromUtf8("ignoreButton"))            
            ignoreButton.setText(_translate("MainWindow", "Ignore", None))            
            
            self.gridLayout.addWidget(ignoreButton, i, 3, 1, 1)

            radioButtons.addButton(ignoreButton)
            radioButtons.addButton(removeButton)
            radioButtons.addButton(addToBlacklist)
                        
            label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
            label_6.setObjectName(_fromUtf8("label_6"))
            self.gridLayout.addWidget(label_6, i, 0, 1, 1) 
            label_6.setText(_translate("MainWindow", item[1], None))
            
            ignoreButton.click()
            self.radioGroup.append(radioButtons)
            i = i+1
            
    def commitFunc(self):
        #print "test"
        
        entireStructure = []
        entireStructure = list(self.inputData.deleteFiles)    
        
        count = 0
        for button in self.radioGroup:
            buttonPressed = button.checkedButton()
            if buttonPressed != None:
                if buttonPressed.text() == "Ignore":
                    item = list(entireStructure[count])
                    item[3] = False
                    print item[1] + " will be ignored"
                    item = tuple(item)
                    entireStructure[count] = item
                    
                if buttonPressed.text() == "Add to Blacklist":
                    item = list(entireStructure[count])
                    print item[1] + " will be added to the blacklist"
                    item[3] == False
                    
        
            count = count + 1
    
            
        entireStructure=set(entireStructure)
        self.inputData.deleteFiles = entireStructure        

        log = False
        if (self.log.isChecked() == True):
            log = True
            print "Saving log"
            
        self.inputData.delete_checked(log)   
        
        if (self.showLog.isChecked() == True):
            #print("test")
            path = os.path.expanduser("~")
            path = path + "\\AppData\\Roaming\\Reinigen\\Logs"
            #print path
            os.system('explorer ' + path)
            
    def selectAllRemoveFunc(self):
        #print "Select all remove"
        for radioButtons in self.radioGroup:
            buttons = []
            buttons = radioButtons.buttons()
            for button in buttons:
                if button.text() == "Remove":
                    button.click()
        
    def deselectAllRemoveFunc(self):
        for radioButtons in self.radioGroup:
            buttons = []
            buttons = radioButtons.buttons()
            for button in buttons:
                if button.text() == "Remove":
                    if button.isChecked():
                        radioButtons.setExclusive(False)
                        button.setChecked(False)
                        radioButtons.setExclusive(True)
        
    def selectAllIgnoreFunc(self):
        for radioButtons in self.radioGroup:
            buttons = []
            buttons = radioButtons.buttons()
            for button in buttons:
                if button.text() == "Ignore":
                    button.click()
        
    def deselectAllIgnoreFunc(self):
        for radioButtons in self.radioGroup:
            buttons = []
            buttons = radioButtons.buttons()
            for button in buttons:
                if button.text() == "Ignore":
                    if button.isChecked():
                        radioButtons.setExclusive(False)
                        button.setChecked(False)
                        radioButtons.setExclusive(True)
        
    

