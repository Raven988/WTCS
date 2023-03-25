# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MW(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setLineWidth(1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.pushButton_12.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/screenshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_7.addWidget(self.pushButton_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.camera_box = QtWidgets.QComboBox(self.tab)
        self.camera_box.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.camera_box.setFont(font)
        self.camera_box.setObjectName("camera_box")
        self.camera_box.addItem("")
        self.camera_box.setItemText(0, "")
        self.camera_box.addItem("")
        self.camera_box.addItem("")
        self.camera_box.addItem("")
        self.camera_box.addItem("")
        self.horizontalLayout_6.addWidget(self.camera_box)
        self.camera_box_2 = QtWidgets.QComboBox(self.tab)
        self.camera_box_2.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.camera_box_2.setFont(font)
        self.camera_box_2.setObjectName("camera_box_2")
        self.camera_box_2.addItem("")
        self.camera_box_2.addItem("")
        self.horizontalLayout_6.addWidget(self.camera_box_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.print_screen_btn = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.print_screen_btn.setFont(font)
        self.print_screen_btn.setText("")
        self.print_screen_btn.setIcon(icon1)
        self.print_screen_btn.setIconSize(QtCore.QSize(45, 30))
        self.print_screen_btn.setObjectName("print_screen_btn")
        self.horizontalLayout_6.addWidget(self.print_screen_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.camera_label = QtWidgets.QLabel(self.tab)
        self.camera_label.setMinimumSize(QtCore.QSize(0, 0))
        self.camera_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);")
        self.camera_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.camera_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.camera_label.setLineWidth(2)
        self.camera_label.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_label.setObjectName("camera_label2")
        self.verticalLayout_4.addWidget(self.camera_label)
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4.addWidget(self.frame_8)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.calendarWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_5.addWidget(self.calendarWidget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_10.setFont(font)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.setItemText(0, "")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_2.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_6.addWidget(self.textBrowser_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon4)
        self.pushButton_16.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_11.addWidget(self.pushButton_16)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_4)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_7.addWidget(self.textBrowser_3)
        self.frame_5 = QtWidgets.QFrame(self.tab_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_13.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/repair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.tableView = QtWidgets.QTableView(self.tab_5)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_8.addWidget(self.tableView)
        self.frame_6 = QtWidgets.QFrame(self.tab_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.setItemText(0, "")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_9.addWidget(self.comboBox_6)
        self.listView = QtWidgets.QListView(self.tab_6)
        self.listView.setObjectName("listView")
        self.verticalLayout_9.addWidget(self.listView)
        self.frame_7 = QtWidgets.QFrame(self.tab_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_5.addWidget(self.pushButton_15)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_5.addWidget(self.pushButton_10)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_9.addWidget(self.frame_7)
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Warehouse Technique Control Software"))
        self.camera_box.setItemText(1, _translate("MainWindow", "ЭШ-68"))
        self.camera_box.setItemText(2, _translate("MainWindow", "ЭШ-69"))
        self.camera_box.setItemText(3, _translate("MainWindow", "ЭШ-70"))
        self.camera_box.setItemText(4, _translate("MainWindow", "ЭШ-71"))
        self.camera_box_2.setItemText(0, _translate("MainWindow", "Вилы"))
        self.camera_box_2.setItemText(1, _translate("MainWindow", "Кабина"))
        self.camera_label.setText(_translate("MainWindow", "Нет сигнала"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Камеры"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Петров Петр Петрович"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Иванов Иван Иванович"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Сергеев Сергей Сергеевич"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Column"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Задачи"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "ЭШ-68"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "ЭШ-69"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "ЭШ-70"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "ЭШ-71"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Показатели"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "ЭШ-68"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ЭШ-69"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "ЭШ-70"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "ЭШ-71"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Техника"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "ЭШ-68"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "ЭЩ-69"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "ЭШ-70"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "ЭШ-71"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Ремонты"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Петров Петр Петрович"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Иванов Иван Иванович"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Сергеев Сергей Сергеевич"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Персонал"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Сохранить как"))
        self.action_4.setText(_translate("MainWindow", "Свернуть"))
        self.action_5.setText(_translate("MainWindow", "О приложении"))
        self.action_6.setText(_translate("MainWindow", "Инсрукция"))
        self.action.setText(_translate("MainWindow", "Развернуть"))
        self.action_7.setText(_translate("MainWindow", "Выход"))
import icons_rc
