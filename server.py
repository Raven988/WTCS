import socket
import threading

HOST = '127.0.0.1'
PORT = 9000


class Server:
    def __init__(self):
        self.ip = HOST
        self.port = PORT
        self.all_client = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen()
        threading.Thread(target=self.connect_handler).start()
        print('Сервер запущен')

    def connect_handler(self):
        while True:
            client, address = self.server.accept()
            print(f'{address[0]} подключился к серверу!')
            if client not in self.all_client:
                self.all_client.append(client)
                threading.Thread(target=self.message_handler, args=(client,)).start()
                client.send('Успешное подключение к чату!'.encode('utf-8'))

    def message_handler(self, client_socket):
        while True:
            message = client_socket.recv(1024)
            for client in self.all_client:
                if client != client_socket:
                    client.send(message)


Server()
