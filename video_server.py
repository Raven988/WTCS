import socket
import cv2
import threading
import pickle
import struct
import pyshine as ps

HOST = '192.168.0.12'
PORT = 9999


class VideoServer:
    def __init__(self):
        self.ip = HOST
        self.port = PORT
        self.all_client = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen()
        print('Сервер запущен')
        while True:
            client, address = self.server.accept()
            print(f'{address[0]} подключился к серверу!')
            threading.Thread(target=self.video_handler, args=(client, address)).start()

    def video_handler(self, client, address):
        try:
            if client:
                data = b""
                payload_size = struct.calcsize("Q")
                while True:
                    while len(data) < payload_size:
                        packet = client.recv(655500)
                        if not packet:
                            break
                        data += packet
                    packed_msg_size = data[:payload_size]
                    data = data[payload_size:]
                    msg_size = struct.unpack("Q", packed_msg_size)[0]
                    while len(data) < msg_size:
                        data += client.recv(655500)
                    frame_data = data[:msg_size]
                    data = data[msg_size:]
                    frame = pickle.loads(frame_data)
                    text = f"CLIENT: {address}"
                    frame = ps.putBText(frame, text, 10, 10, vspace=10, hspace=1, font_scale=0.7,
                                        background_RGB=(255, 0, 0), text_RGB=(255, 250, 250))
                    cv2.imshow(f"FROM {address}", frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        break
                client.close()
        except:
            print(f'{address[0]} отключился о сервера!')


VideoServer()
