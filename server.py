import socket
import threading

HOST = '192.168.0.14'
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
            for any_client in self.all_client:
                any_client.send(f'{address[0]} вошел в чат!'.encode('utf-8'))
            if client not in self.all_client:
                self.all_client.append(client)
                threading.Thread(target=self.message_handler, args=(client, address)).start()
                client.send('Успешное подключение к чату!'.encode('utf-8'))
                threading.Thread(target=self.video_handler, args=(client,)).start()

    def message_handler(self, client_socket, address):
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
                    any_client.send(f'{address[0]} покинул чат!'.encode('utf-8'))
                break

    def video_handler(self, client_socket):
        while True:
            try:
                video_signal = client_socket.recv(1024)
                for client in self.all_client:
                    if client != client_socket:
                        client.send(video_signal)
            except:
                break


Server()
