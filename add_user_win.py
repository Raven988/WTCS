# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 195)
        Form.setMinimumSize(QtCore.QSize(800, 195))
        Form.setMaximumSize(QtCore.QSize(800, 195))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(Form)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.LineEdit = QtWidgets.QLineEdit(Form)
        self.LineEdit.setObjectName("LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit)
        self.Label_2 = QtWidgets.QLabel(Form)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.LineEdit_2 = QtWidgets.QLineEdit(Form)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEdit_2)
        self.Label_3 = QtWidgets.QLabel(Form)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.LineEdit_3 = QtWidgets.QLineEdit(Form)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LineEdit_3)
        self.Label_11 = QtWidgets.QLabel(Form)
        self.Label_11.setObjectName("Label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_11)
        self.ComboBox = QtWidgets.QComboBox(Form)
        self.ComboBox.setObjectName("ComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ComboBox)
        self.Label_5 = QtWidgets.QLabel(Form)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.ComboBox_2 = QtWidgets.QComboBox(Form)
        self.ComboBox_2.setObjectName("ComboBox_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ComboBox_2)
        self.Label_9 = QtWidgets.QLabel(Form)
        self.Label_9.setObjectName("Label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_9)
        self.LineEdit_5 = QtWidgets.QLineEdit(Form)
        self.LineEdit_5.setObjectName("LineEdit_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.LineEdit_5)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label_7 = QtWidgets.QLabel(Form)
        self.Label_7.setObjectName("Label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.LineEdit_7 = QtWidgets.QLineEdit(Form)
        self.LineEdit_7.setObjectName("LineEdit_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit_7)
        self.Label_8 = QtWidgets.QLabel(Form)
        self.Label_8.setObjectName("Label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.LineEdit_8 = QtWidgets.QLineEdit(Form)
        self.LineEdit_8.setObjectName("LineEdit_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEdit_8)
        self.Label_4 = QtWidgets.QLabel(Form)
        self.Label_4.setObjectName("Label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.LineEdit_4 = QtWidgets.QLineEdit(Form)
        self.LineEdit_4.setObjectName("LineEdit_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LineEdit_4)
        self.Label_10 = QtWidgets.QLabel(Form)
        self.Label_10.setObjectName("Label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_10)
        self.LineEdit_6 = QtWidgets.QLineEdit(Form)
        self.LineEdit_6.setObjectName("LineEdit_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.LineEdit_6)
        self.Label_6 = QtWidgets.QLabel(Form)
        self.Label_6.setObjectName("Label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.DateEdit = QtWidgets.QDateEdit(Form)
        self.DateEdit.setDisplayFormat("yyyy-MM-dd")
        self.DateEdit.setObjectName("DateEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.DateEdit)
        self.Label_12 = QtWidgets.QLabel(Form)
        self.Label_12.setObjectName("Label_12")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Label_12)
        self.LineEdit_9 = QtWidgets.QLineEdit(Form)
        self.LineEdit_9.setObjectName("LineEdit_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.LineEdit_9)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Label.setText(_translate("Form", "Имя"))
        self.Label_2.setText(_translate("Form", "Фамилия"))
        self.Label_3.setText(_translate("Form", "Отчество"))
        self.Label_11.setText(_translate("Form", "Склад"))
        self.Label_5.setText(_translate("Form", "Должность"))
        self.Label_9.setText(_translate("Form", "Логин"))
        self.Label_7.setText(_translate("Form", "Адрес регистрации"))
        self.Label_8.setText(_translate("Form", "Адрес проживания"))
        self.Label_4.setText(_translate("Form", "Номер телефона"))
        self.Label_10.setText(_translate("Form", "Комментарии"))
        self.Label_6.setText(_translate("Form", "Дата устройства"))
        self.Label_12.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Добваить"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))
