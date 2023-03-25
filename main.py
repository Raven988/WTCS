from PyQt5 import QtWidgets, QtCore, QtGui
import socket
import sys
import time
import cv2
import os
import numpy as np

from login_win import Ui_Login
from main_win import Ui_MW
from add_pers_win import Ui_Form as add_pers_win
from add_repair_win import Ui_Form as add_repair_win
from add_tec_win import Ui_Form as add_tec_win
from add_work_part_win import Ui_Dialog as add_work_part_win

LOGIN_PSWRD = {'1': '111', '2': '222', '3': '333'}
NUM_AVALIBOL_CAMERAS = 1
MAIN_IP = socket.gethostname()
PORT = 9000
VIDEO_PORT = 9001


class MessageMonitor(QtCore.QThread):
    """Класс реализован потоком для отслеживания чата приложения"""
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, server_socket, parent=None):
        """Инициализация"""
        QtCore.QThread.__init__(self, parent)
        self.server_socket = server_socket
        self.message = None

    def run(self):
        """Запуск потока"""
        while True:
            self.message = self.server_socket.recv(1024)
            self.mysignal.emit(self.message.decode('utf-8'))


class VideoHandler(QtCore.QThread):
    """Класс реализован потоком для отслеживания перенаправленных
    сервером видеопотоков и отоброжения"""
    mysignal = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        """Инициализация"""
        QtCore.QThread.__init__(self, parent)
        self.vid_handler = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.vid_handler.bind((socket.gethostbyname(MAIN_IP), VIDEO_PORT))

    def run(self):
        """Запуск потока"""
        try:
            while True:
                data, _ = self.vid_handler.recvfrom(65507)
                nparr = np.frombuffer(data, np.uint8)
                img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                image = cv2.cvtColor(img_decode, cv2.COLOR_BGR2RGB)
                flipped_image = cv2.flip(image, 1)
                conv_to_qt_format = QtGui.QImage(flipped_image.data, flipped_image.shape[1],
                                                 flipped_image.shape[0], QtGui.QImage.Format_RGB888)
                pic = conv_to_qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                self.mysignal.emit(pic)
        except:
            print('Ошибка с перенапровлением видеопотока')


class VideoMonitor(QtCore.QThread):
    """Класс реализован потоком для оброботки сигнала с веб-камеры и его отоброжения,
    так-же для отправки видеопотока на сервер для последующего перенапровления клиентам"""
    mysignal = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, cam_index, parent=None):
        """Инициализация"""
        QtCore.QThread.__init__(self, parent)
        self.vid_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.vid = cv2.VideoCapture(cam_index)

    def run(self):
        """Запуск потока"""
        while True:
            try:
                ret, frame = self.vid.read()
                if ret:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flipped_img = cv2.flip(image, 1)
                    conv_to_qt_frm = QtGui.QImage(flipped_img.data, flipped_img.shape[1],
                                                  flipped_img.shape[0], QtGui.QImage.Format_RGB888)
                    pic = conv_to_qt_frm.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                    self.mysignal.emit(pic)

                    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
                    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
                    data = np.array(imgencode)
                    string_data = data.tobytes()
                    self.vid_client.sendto(string_data, (SERVER_IP, VIDEO_PORT))

            except:
                print('Ошибка оброботки сигнала с веб-камеры')
                self.vid_client.close()
                self.vid.release()


class LoginWin(Ui_Login):
    """Запуск окна входа в приложения с последующим отоброжение главного окна"""
    def __init__(self):
        """Инициализация"""
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
        self.start_w.pushButton_4.clicked.connect(self.add_tec_win)
        self.start_w.pushButton_9.clicked.connect(self.add_pers_win)
        self.start_w.pushButton_6.clicked.connect(self.add_rep_win)
        self.start_w.frame_8.hide()
        self.num_available_cameras = NUM_AVALIBOL_CAMERAS
        self.tcp_client = None
        self.anim = None
        self.message_monitor = None
        self.video_monitor = None
        self.video_handler = None
        self.start_w.camera_box_2.activated.connect(self.activated_video_combobox)
        self.start_w.print_screen_btn.clicked.connect(self.print_scr)

        sys.exit(app.exec_())

    def print_scr(self):
        """Функция для сохранения скриншота с камеры"""
        pixmap = QtGui.QPixmap(self.start_w.camera_label.size())
        self.start_w.camera_label.render(pixmap)
        time_tuple = time.localtime()
        time_string = time.strftime("%H.%M.%S.%d.%m.%Y,", time_tuple)
        filename = f'screenshot_{time_string}.png'
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screenshots')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        filepath = os.path.join(folder_path, filename)
        pixmap.save(filepath)

    def activated_video_combobox(self, index):
        """Функци для отображения картинки с веб-камеры"""
        if self.num_available_cameras == 1:
            self.video_monitor = VideoMonitor(0)
            self.video_monitor.mysignal.connect(self.image_update_slot)
            self.video_monitor.start()
            self.start_w.camera_box_2.setEnabled(False)
        else:
            if self.video_monitor is None:
                self.video_monitor = VideoMonitor(index)
                self.video_monitor.mysignal.connect(self.image_update_slot)
                self.video_monitor.start()
            else:
                self.video_monitor.vid.release()
                self.video_monitor.vid = cv2.VideoCapture(index)

    def push_btn(self):
        """Функция для отрисобки главного окна.
        Создание потоков реализована в данной функие"""
        try:
            if self.ui.lineEdit.text() in LOGIN_PSWRD and \
                    LOGIN_PSWRD[self.ui.lineEdit.text()] == self.ui.lineEdit_2.text():
                self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tcp_client.connect((SERVER_IP, PORT))

            if self.ui.lineEdit.text() in LOGIN_PSWRD and \
                    LOGIN_PSWRD[self.ui.lineEdit.text()] == self.ui.lineEdit_2.text():
                self.login_win.close()
                self.main_win.show()
                self.anim = QtCore.QPropertyAnimation(self.main_win, b"pos")
                self.anim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
                self.anim.setStartValue(QtCore.QPoint(0, 0))
                self.anim.setEndValue(QtCore.QPoint(300, 100))
                self.anim.setDuration(1000)
                self.anim.start()

                self.message_monitor = MessageMonitor(self.tcp_client)
                self.message_monitor.mysignal.connect(self.update_chat)
                self.message_monitor.start()

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

        except (ConnectionRefusedError, TimeoutError):
            dlg = QtWidgets.QDialog()
            dlg.setWindowTitle("Ошибка входа")
            dlg.setFixedSize(180, 70)
            dlg.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
            label = QtWidgets.QLabel("Сервер недоступен")
            layout = QtWidgets.QVBoxLayout()
            btn = QtWidgets.QPushButton("Ok", dlg)
            btn.clicked.connect(dlg.close)
            layout.addWidget(label)
            layout.addWidget(btn)
            dlg.setLayout(layout)
            dlg.exec_()

    def update_chat(self, value):
        """Функция для обновления чата от других клиентов"""
        self.start_w.textBrowser.append(value)

    def image_update_slot(self, image):
        """Функция для обновления видео с веб-камер"""
        self.start_w.camera_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def image_update_slot2(self, image):
        """Функция для обновления видео с веб-камер 2"""
        self.start_w.camera_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def input_msg(self):
        """Функция обновления чата и отправки данных другим клиентам"""
        message = self.start_w.textEdit.toPlainText()
        if len(message) > 0:
            self.start_w.textEdit.clear()
            time_tuple = time.localtime()
            time_string = time.strftime("%H:%M:%S", time_tuple)
            send_msg = time_string + '\n' + message + '\n'
            self.start_w.textBrowser.append(send_msg)
            self.tcp_client.send(send_msg.encode('utf-8'))

    def add_tec_win(self):
        """Функция отображения окна добовления техникик"""
        self.added_win = QtWidgets.QWidget()
        self.ui = add_tec_win()
        self.ui.setupUi(self.added_win)
        self.added_win.show()

    def add_rep_win(self):
        """Функция отображения окна добавления ремонтов"""
        self.added_win = QtWidgets.QWidget()
        self.ui = add_repair_win()
        self.ui.setupUi(self.added_win)
        self.added_win.show()
        self.ui.pushButton_5.clicked.connect(self.add_work_win)
        self.ui.pushButton_3.clicked.connect(self.add_parts_win)

    def add_pers_win(self):
        """Функция отображения окна добавления пользователей"""
        self.added_win = QtWidgets.QWidget()
        self.ui = add_pers_win()
        self.ui.setupUi(self.added_win)
        self.added_win.show()

    def add_work_win(self):
        """Функция отображения окна добавления работ"""
        self.added_win = QtWidgets.QDialog()
        self.ui = add_work_part_win()
        self.ui.setupUi(self.added_win)
        self.added_win.show()

    def add_parts_win(self):
        """Функция отоброжения окна добавления запчастей"""
        self.added_win = QtWidgets.QDialog()
        self.ui = add_work_part_win()
        self.ui.setupUi(self.added_win)
        self.added_win.show()


if __name__ == "__main__":
    SERVER_IP = input('Введите ип адрес сервера: ')
    LoginWin()
