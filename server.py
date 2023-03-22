"""

****SERVER WTCS****
made by bannikovrt@list.ru

"""
import socket
import threading

HOST = socket.gethostname()


class Server:
    """Данный класс является основном для запуска сервера
    в него передаются параметры портов, на которых будет запущен сервер"""
    def __init__(self, ip=socket.gethostbyname(HOST), port=9000, video_port=9001):
        """Инициализация"""
        self.ip = ip
        self.port = port
        self.video_port = video_port
        self.all_client = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen()
        self.video_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.video_server.bind((self.ip, self.video_port))
        threading.Thread(target=self.connect_handler).start()
        print('Сервер запущен')

    def connect_handler(self):
        """Функция для установки контакта с клиентами"""
        while True:
            client, address = self.server.accept()
            print(f'{address[0]} подключился к серверу!')
            for any_client in self.all_client:
                any_client.send(f'{address[0]} вошел в чат!\n'.encode('utf-8'))
            if client not in self.all_client:
                self.all_client.append(client)
                client.send('Успешное подключение к чату!\n'.encode('utf-8'))
                threading.Thread(target=self.message_handler, args=(client, address)).start()
                threading.Thread(target=self.video_handler).start()

    def message_handler(self, client_socket, address):
        """Функция для обработки сообщений чата приложения"""
        while True:
            try:
                message = client_socket.recv(1024)
                for client in self.all_client:
                    if client != client_socket:
                        client.send(message)
            except:
                print(f'{address[0]} отключился о сервера!')
                self.all_client.remove(client_socket)
                client_socket.close()
                for any_client in self.all_client:
                    any_client.send(f'{address[0]} покинул чат!\n'.encode('utf-8'))
                break

    def video_handler(self):
        """Функция для приема видеопотока и перенапровление его клиентам"""
        while True:
            try:
                data, address = self.video_server.recvfrom(65507)
                for client in self.all_client:
                    self.video_server.sendto(data, (client.getsockname()[0], 9001))
            except:
                print('Ошибка с перенапровлением видеосигнала')


if __name__ == '__main__':
    print(socket.gethostbyname(HOST))
    Server()
