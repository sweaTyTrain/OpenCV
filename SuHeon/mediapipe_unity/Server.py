import socket
import cv2
import numpy as np
from _thread import *

# 배열의 출력 형식 설정
np.set_printoptions(threshold=np.inf)

class SocketServer():
    client_sockets = []
    HOST = "118.37.219.113"
    PORT = 5053

    def __init__(self):
        print(">> Server Start")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()

    def server_run(self):
        try:
            while True:
                print('>> Wait')
                client_socket, addr = self.server_socket.accept()
                self.client_sockets.append(client_socket)
                start_new_thread(self.thread_client, (client_socket, addr))
                print("연결된 수 : ", len(self.client_sockets))
        except Exception as e:
            print("socketServer error : ", e)
        finally:
            self.server_socket.close()

    def thread_client(self, client_socket, addr):
        print('>> Connected by : ', addr[0], ":", addr[1])
        while True:
            try:
                data = client_socket.recv(1024*1000)
                if not data:
                    print(">> Disconnected by ", addr[0], ":", addr[1])
                    break
                #print(data)

                # 바이트 배열을 NumPy 배열로 변환하여 이미지로 디코딩
                np_data = np.frombuffer(data, dtype=np.uint8)
                #print(np_data)
                print(len(np_data))
                img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
                #print(img)
                # 이미지를 표시
                cv2.imshow('Received Image', img)
                cv2.waitKey(1)

            except Exception as e:
                print("Error while processing image:", e)


        # 클라이언트 소켓 닫기
        client_socket.close()

# 서버 인스턴스 생성 및 실행
server = SocketServer()
server.server_run()
