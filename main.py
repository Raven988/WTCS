from PyQt5 import QtWidgets, QtCore, QtGui
import socket
import sys
import time
import cv2
import os
import psycopg2
import numpy as np

from login_win import Ui_Login
from main_win import Ui_MainWindow as Ui_MW
from add_user_win import Ui_Form as add_pers_win
from add_repair_win import Ui_Form as add_repair_win
from add_tech_win import Ui_Form as add_tec_win
from add_work_part_win import Ui_Form as add_work_part_win
from del_win import Ui_Form as del_win

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


def adding_technique(ui, win):
    """Функия добавления техники в базу данных"""
    model = ui.LineEdit.text()
    serial_number = ui.LineEdit_2.text()
    registration_plate = ui.LineEdit_4.text()
    garage_number = ui.LineEdit_5.text()
    date_of_entry = ui.DateEdit.text()
    warehouse_id = ui.ComboBox.currentIndex()
    comments = ui.LineEdit_6.text()
    try:
        with CONNECTION.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO technique(garage_number, registration_plate, model, serial_number, "
                f"date_of_entry, comments, warehouse_id) VALUES ({garage_number},"
                f"'{registration_plate}', '{model}', {serial_number}, '{date_of_entry}',"
                f"'{comments}', {warehouse_id + 1});"
            )
            win.close()
    except:
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Ошибка")
        dlg.setFixedSize(210, 70)
        dlg.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        label = QtWidgets.QLabel("Необходимо заполнить все строки")
        layout = QtWidgets.QVBoxLayout()
        btn = QtWidgets.QPushButton("Ok", dlg)
        btn.clicked.connect(dlg.close)
        layout.addWidget(label)
        layout.addWidget(btn)
        dlg.setLayout(layout)
        dlg.exec_()


def adding_users(ui, win):
    """Функия добавления пользователя в базу данных"""
    first_name = ui.LineEdit.text()
    last_name = ui.LineEdit_2.text()
    fathers_name = ui.LineEdit_3.text()
    warehouse_id = ui.ComboBox.currentIndex()
    position_id = ui.ComboBox_2.currentIndex()
    address_of_registration = ui.LineEdit_7.text()
    address_of_resdence = ui.LineEdit_8.text()
    phone_number = ui.LineEdit_4.text()
    comments = ui.LineEdit_6.text()
    employment_data = ui.DateEdit.text()
    login = ui.LineEdit_5.text()
    password = ui.LineEdit_9.text()
    try:
        with CONNECTION.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO users(first_name, last_name, fathers_name, position_id, "
                f"phone_number, address_of_registration, address_of_resdence, employment_data,"
                f"comments, login, password, warehouse_id) VALUES ('{first_name}',"
                f"'{last_name}', '{fathers_name}', {position_id + 1}, {phone_number},"
                f"'{address_of_registration}', '{address_of_resdence}', '{employment_data}', "
                f"'{comments}', '{login}', '{password}', {warehouse_id + 1});"
            )
            win.close()
    except:
        dlg = QtWidgets.QDialog()
        dlg.setWindowTitle("Ошибка")
        dlg.setFixedSize(210, 70)
        dlg.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        label = QtWidgets.QLabel("Необходимо заполнить все строки")
        layout = QtWidgets.QVBoxLayout()
        btn = QtWidgets.QPushButton("Ok", dlg)
        btn.clicked.connect(dlg.close)
        layout.addWidget(label)
        layout.addWidget(btn)
        dlg.setLayout(layout)
        dlg.exec_()


def delete_technique(ui, win):
    """Удаление техники с базы данных"""
    selcted_data = ui.comboBox_2.currentText()
    try:
        with CONNECTION.cursor() as cursor:
            cursor.execute(f"DELETE FROM technique WHERE garage_number = {selcted_data};")
            win.close()
    except:
        pass


def add_garage_number_to_combobox(ui):
    """Добавление гаражных номеров в выподающий список"""
    warehouse = ui.comboBox.currentText()
    ui.comboBox_2.clear()
    try:
        with CONNECTION.cursor() as cursor:
            cursor.execute(f"SELECT garage_number FROM (SELECT * FROM warehouse JOIN technique "
                           f"ON warehouse.id = technique.warehouse_id) as w "
                           f"WHERE name = '{warehouse}';")
            data = cursor.fetchall()
            for item in data:
                ui.comboBox_2.addItem(str(item[0]))
    except:
        pass


def add_users_to_combobox(ui):
    """Добавление пользователей в выподающий список"""
    warehouse = ui.comboBox.currentText()
    ui.comboBox_2.clear()
    try:
        with CONNECTION.cursor() as cursor:
            cursor.execute(f"SELECT first_name, last_name, fathers_name FROM "
                           f"(SELECT * FROM warehouse JOIN users ON "
                           f"warehouse.id = users.warehouse_id) as w WHERE name = '{warehouse}';")
            data = cursor.fetchall()
            for item in data:
                ui.comboBox_2.addItem(f"{item[0]} {item[1]} {item[2]}")
    except:
        pass


def delete_user(ui, win):
    """Удаление пользователя с базы данных"""
    selcted_data = ui.comboBox_2.currentText()
    split_data = selcted_data.split()
    try:
        with CONNECTION.cursor() as cursor:
            cursor.execute(f"DELETE FROM users WHERE (first_name = '{split_data[0]}' "
                           f"AND last_name = '{split_data[1]}' "
                           f"AND fathers_name = '{split_data[2]}');")
            win.close()
    except:
        pass


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
        self.start_w.pushButton_5.clicked.connect(self.del_tech)
        self.start_w.pushButton_9.clicked.connect(self.add_pers_win)
        self.start_w.pushButton_10.clicked.connect(self.del_user)
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
        self.start_w.pushButton_12.clicked.connect(self.clear_chat)
        self.start_w.pushButton_2.clicked.connect(self.add_row)

        sys.exit(app.exec_())

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
                try:
                    with CONNECTION.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM warehouse;")
                        data = cursor.fetchall()
                        for item in data:
                            self.start_w.camera_box.addItem(item[1])
                            self.start_w.comboBox_3.addItem(item[1])
                        self.start_w.treeWidget.setHeaderLabels(
                            ['Склад', 'Гаражный номер', 'Регистрационный знак', 'Комментарии'])
                        prt1 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget, [data[0][1], '', '', ''])
                        prt2 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget, [data[1][1], '', '', ''])
                        prt3 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget, [data[2][1], '', '', ''])
                        prt4 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget, [data[3][1], '', '', ''])
                        prt5 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget, [data[4][1], '', '', ''])
                        cursor.execute("SELECT * FROM technique JOIN warehouse ON technique.warehouse_id = warehouse.id;")
                        data2 = cursor.fetchall()
                        for i in data2:
                            if i[10] == "РЦ Санкт-Петербург":
                                child = QtWidgets.QTreeWidgetItem(prt1,[str(i[3]), str(i[1]), str(i[2]), str(i[7])])
                        for i in data2:
                            if i[10] == "РЦ Челябинск":
                                child = QtWidgets.QTreeWidgetItem(prt2,[str(i[3]), str(i[1]), str(i[2]), str(i[7])])
                        for i in data2:
                            if i[10] == "РЦ Калининград":
                                child = QtWidgets.QTreeWidgetItem(prt3,[str(i[3]), str(i[1]), str(i[2]), str(i[7])])
                        for i in data2:
                            if i[10] == "РЦ Подольск":
                                child = QtWidgets.QTreeWidgetItem(prt4,[str(i[3]), str(i[1]), str(i[2]), str(i[7])])
                        for i in data2:
                            if i[10] == "РЦ Казань":
                                child = QtWidgets.QTreeWidgetItem(prt5,[str(i[3]), str(i[1]), str(i[2]), str(i[7])])

                        self.start_w.treeWidget_2.setHeaderLabels(
                            ['Склад', 'ФИО', 'Должность', 'Номер телефона'])
                        prt6 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget_2, [data[0][1], '', '', ''])
                        prt7 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget_2, [data[1][1], '', '', ''])
                        prt8 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget_2, [data[2][1], '', '', ''])
                        prt9 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget_2, [data[3][1], '', '', ''])
                        prt10 = QtWidgets.QTreeWidgetItem(self.start_w.treeWidget_2, [data[4][1], '', '', ''])
                        cursor.execute(
                            "SELECT * FROM users JOIN warehouse ON users.warehouse_id = warehouse.id JOIN position ON position.id = users.position_id;")
                        data3 = cursor.fetchall()
                        for i in data3:
                            if i[15] == "РЦ Санкт-Петербург":
                                child = QtWidgets.QTreeWidgetItem(prt6, [str(''), str(i[1])+' '+str(i[2])+' '+str(i[3]), str(i[17]), str(i[5])])
                        for i in data3:
                            if i[15] == "РЦ Челябинск":
                                child = QtWidgets.QTreeWidgetItem(prt7, [str(''), str(i[1])+' '+str(i[2])+' '+str(i[3]), str(i[17]), str(i[5])])
                        for i in data3:
                            if i[15] == "РЦ Калининград":
                                child = QtWidgets.QTreeWidgetItem(prt8, [str(''), str(i[1])+' '+str(i[2])+' '+str(i[3]), str(i[17]), str(i[5])])
                        for i in data3:
                            if i[15] == "РЦ Подольск":
                                child = QtWidgets.QTreeWidgetItem(prt9, [str(''), str(i[1])+' '+str(i[2])+' '+str(i[3]), str(i[17]), str(i[5])])
                        for i in data3:
                            if i[15] == "РЦ Казань":
                                child = QtWidgets.QTreeWidgetItem(prt10, [str(''), str(i[1])+' '+str(i[2])+' '+str(i[3]), str(i[17]), str(i[5])])

                except Exception as ex:
                    print(ex)

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

    def add_row(self):
        """Добавление строки во вкладке задачи"""
        row_position = self.start_w.tableWidget.rowCount()
        self.start_w.tableWidget.insertRow(row_position)

    def del_tech(self):
        """Удаление записи с базы данных"""
        self.del_win = QtWidgets.QWidget()
        self.ui = del_win()
        self.ui.setupUi(self.del_win)
        try:
            with CONNECTION.cursor() as cursor:
                cursor.execute("SELECT * FROM warehouse;")
                data = cursor.fetchall()
                for item in data:
                    self.ui.comboBox.addItem(item[1])
        except:
            pass

        self.del_win.show()
        self.ui.comboBox.activated.connect(lambda: add_garage_number_to_combobox(self.ui))
        self.ui.pushButton.clicked.connect(lambda: delete_technique(self.ui, self.del_win))
        self.ui.pushButton_2.clicked.connect(self.del_win.close)

    def del_user(self):
        """Удаление записи с базы данных"""
        self.del_win = QtWidgets.QWidget()
        self.ui = del_win()
        self.ui.setupUi(self.del_win)
        try:
            with CONNECTION.cursor() as cursor:
                cursor.execute("SELECT * FROM warehouse;")
                data = cursor.fetchall()
                for item in data:
                    self.ui.comboBox.addItem(item[1])
        except:
            pass

        self.del_win.show()
        self.ui.comboBox.activated.connect(lambda: add_users_to_combobox(self.ui))
        self.ui.pushButton.clicked.connect(lambda: delete_user(self.ui, self.del_win))
        self.ui.pushButton_2.clicked.connect(self.del_win.close)

    def clear_chat(self):
        """Очистка окна сообщения"""
        self.start_w.textEdit.clear()

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
        self.ui.pushButton_2.clicked.connect(self.added_win.close)
        self.ui.pushButton.clicked.connect(lambda: adding_technique(self.ui, self.added_win))

    def add_rep_win(self):
        """Функция отображения окна добавления ремонтов"""
        self.added_win = QtWidgets.QWidget()
        self.ui = add_repair_win()
        self.ui.setupUi(self.added_win)
        self.added_win.show()
        self.ui.pushButton_2.clicked.connect(self.added_win.close)
        self.ui.pushButton_5.clicked.connect(self.add_work_win)
        self.ui.pushButton_3.clicked.connect(self.add_parts_win)

    def add_pers_win(self):
        """Функция отображения окна добавления пользователей"""
        self.added_win = QtWidgets.QWidget()
        self.ui = add_pers_win()
        self.ui.setupUi(self.added_win)
        try:
            with CONNECTION.cursor() as cursor:
                cursor.execute(f"SELECT * FROM warehouse;")
                data = cursor.fetchall()
                for item in data:
                    self.ui.ComboBox.addItem(item[1])
                cursor.execute(f"SELECT * FROM position;")
                data_2 = cursor.fetchall()
                for item in data_2:
                    self.ui.ComboBox_2.addItem(item[1])
        except:
            pass
        self.added_win.show()
        self.ui.pushButton_2.clicked.connect(self.added_win.close)
        self.ui.pushButton.clicked.connect(lambda: adding_users(self.ui, self.added_win))

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

    try:
        from log_postgres import host, user, password, port, database
        CONNECTION = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        CONNECTION.autocommit = True
    except:
        print('Подключение к базе данных отсутсвует')
    SERVER_IP = '192.168.194.139'
    LoginWin()

