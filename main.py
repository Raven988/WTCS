import socket
import sys
import time
import cv2
import pickle
import struct
from PyQt5 import QtWidgets, QtCore, QtGui

from login_win import Ui_Login
from main_win import Ui_MW

login_pwd = ("111", "222")
HOST = '192.168.0.12'
PORT = 9000


class MessageMonitor(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, server_socket, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.server_socket = server_socket
        self.message = None

    def run(self):
        while True:
            self.message = self.server_socket.recv(1024)
            self.mysignal.emit(self.message.decode('utf-8'))

class data_ac(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(QtGui.QImage)
    def __init__(self, server_socket, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.server_socket = server_socket

    def run(self):
        while True:
            try:
                data = b''
                payload_size = struct.calcsize("Q")
                while True:
                    while len(data) < payload_size:
                        packet = self.server_socket.recv(1024 * 4)
                        if not packet:
                            break
                        data += packet
                    packed_msg_size = data[:payload_size]
                    data = data[payload_size:]
                    msg_size = struct.unpack("Q", packed_msg_size)[0]
                    while len(data) < msg_size:
                        data += self.server_socket.recv(1024 * 4)
                    frame_data = data[:msg_size]
                    data = data[msg_size:]
                    frame = pickle.loads(frame_data)
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flipped_image = cv2.flip(image, 1)
                    convert_to_qt_format = QtGui.QImage(flipped_image.data, flipped_image.shape[1],
                                                flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                    pic = convert_to_qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                    self.mysignal.emit(pic)
            except:
                self.server_socket.close()

class VideoMonitor(QtCore.QThread):
    def __init__(self, server_socket, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.server_socket = server_socket
        self.vid = cv2.VideoCapture(0)

    def run(self):
        while True:
            try:
                while True:
                    ret, frame = self.vid.read()
                    a = pickle.dumps(frame)
                    msg = struct.pack("Q", len(a)) + a
                    self.server_socket.sendall(msg)
            except:
                self.server_socket.close()
                self.vid.release()


class LoginWin(Ui_Login):
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

        self.vid_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.vid_client.connect((HOST, 9001))

        self.message_monitor = MessageMonitor(self.tcp_client)
        self.message_monitor.mysignal.connect(self.update_chat)
        self.message_monitor.start()

        self.video_monitor = VideoMonitor(self.vid_client)
        self.video_monitor.start()

        self.data_ac = data_ac(self.vid_client)
        self.data_ac.mysignal.connect(self.image_update_slot)
        self.data_ac.start()

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

    def image_update_slot(self, image):
        self.start_w.graphicsView.setPixmap(QtGui.QPixmap.fromImage(image))

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
    LoginWin()
