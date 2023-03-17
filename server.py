import socket
import threading

HOST = '192.168.0.12'
PORT = 9000
VIDEO_PORT = 9001

class Server:
    def __init__(self):
        self.ip = HOST
        self.port = PORT
        self.video_port = VIDEO_PORT
        self.all_client = []
        self.all_video_client = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen()
        self.video_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.video_server.bind((self.ip, self.video_port))
        self.video_server.listen()
        threading.Thread(target=self.connect_handler).start()
        print('Сервер запущен')

    def connect_handler(self):
        while True:
            client, address = self.server.accept()
            video_client, video_address = self.video_server.accept()
            print(f'{address[0]} подключился к серверу!')
            for any_client in self.all_client:
                any_client.send(f'{address[0]} вошел в чат!\n'.encode('utf-8'))
            if video_client not in self.all_video_client:
                self.all_video_client.append(video_client)
            if client not in self.all_client:
                self.all_client.append(client)
                client.send('Успешное подключение к чату!\n'.encode('utf-8'))
                threading.Thread(target=self.message_handler, args=(client, address)).start()
                threading.Thread(target=self.video_handler, args=(video_client)).start()

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
                    any_client.send(f'{address[0]} покинул чат!\n'.encode('utf-8'))
                break

    def video_handler(self, client_socket):
        while True:
            try:
                data = client_socket.recv(4024)
                for client in self.all_video_client:
                    if client == client_socket:
                        client.send(data)
            except:
                self.all_video_client.remove(client_socket)
                client_socket.close()
                break


Server()
