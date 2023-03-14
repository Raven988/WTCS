import socket
import sys
import time
from PyQt5 import QtWidgets, QtCore

from login_win import Ui_Login
from main_win import Ui_MW

login_pwd = ("111", "222")
HOST = '192.168.0.14'
PORT = 9000


class message_monitor(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, server_socket, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.server_socket = server_socket
        self.message = None

    def run(self):
        while True:
            self.message = self.server_socket.recv(1024)
            self.mysignal.emit(self.message.decode('utf-8'))


# хэшлиб
class login_win(Ui_Login):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.login_win = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.login_win)
        self.login_win.show()
        self.ui.pushButton.clicked.connect(self.push_btn)
        self.main_win = QtWidgets.QMainWindow()
        self.start_w = Ui_MW()
        self.start_w.setupUi(self.main_win)
        self.start_w.pushButton.clicked.connect(self.input_msg)

        sys.exit(app.exec_())

    def push_btn(self):
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_client.connect((HOST, PORT))

        self.message_monitor = message_monitor(self.tcp_client)
        self.message_monitor.mysignal.connect(self.update_chat)
        self.message_monitor.start()

        if self.ui.lineEdit.text() and self.ui.lineEdit_2.text() in login_pwd:
            self.login_win.close()
            self.main_win.show()
            self.anim = QtCore.QPropertyAnimation(self.main_win, b"pos")
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
            btn = QtWidgets.QPushButton("Ok", dlg)
            btn.clicked.connect(dlg.close)
            layout.addWidget(label)
            layout.addWidget(btn)
            dlg.setLayout(layout)
            dlg.exec_()



    def update_chat(self, value):
        self.start_w.textBrowser.append(value)

    def input_msg(self):
        message = self.start_w.textEdit.toPlainText()
        if len(message) > 0:
            self.start_w.textEdit.clear()
            time_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", time_tuple)
            send_msg = time_string + '\n' + message + '\n'
            self.start_w.textBrowser.append(send_msg)
            self.tcp_client.send(send_msg.encode('utf-8'))


if __name__ == "__main__":
    login_win()
