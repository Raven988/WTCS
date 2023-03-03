import sys
from PyQt5 import QtWidgets, QtCore

from login_win import Ui_Login
from main_win import Ui_MW

login_pwd = ("111", "222")

class login_win(Ui_Login):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.pushButton.clicked.connect(self.push_btn)
        self.MainW2 = QtWidgets.QMainWindow()

        sys.exit(app.exec_())

    def push_btn(self):
        if self.ui.lineEdit.text() and self.ui.lineEdit_2.text() in login_pwd :
            self.MainWindow.close()
            start_w = Ui_MW()
            start_w.setupUi(self.MainW2)
            self.MainW2.show()
            self.anim = QtCore.QPropertyAnimation(self.MainW2, b"pos")
            self.anim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
            self.anim.setStartValue(QtCore.QPoint(0, 0))
            self.anim.setEndValue(QtCore.QPoint(300, 100))
            self.anim.setDuration(1000)
            self.anim.start()

        else:
            dlg = QtWidgets.QDialog()
            dlg.setWindowTitle("Ошибка входа")
            dlg.setFixedSize(180, 70)
            dlg.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
            label = QtWidgets.QLabel("Неверный логин или пароль")
            layout = QtWidgets.QVBoxLayout()
            btn = QtWidgets.QPushButton("Выход",dlg)
            btn.clicked.connect(dlg.close)
            layout.addWidget(label)
            layout.addWidget(btn)
            dlg.setLayout(layout)
            dlg.exec_()



if __name__ == "__main__":
    login_win()
