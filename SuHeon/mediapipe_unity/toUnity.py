import modules

import cv2
import numpy as np
import socket
from _thread import *
import pandas as pd
import mediapipe as mp
import tensorflow as tf

# # 배열의 출력 형식 설정
# np.set_printoptions(threshold=np.inf)

class socketClient():

    HOST = "118.37.219.113"
    PORT = 5053

    def __init__(self):
        super().__init__()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.alive = True

    def client_run(self):
        start_new_thread(self.recv_data, (self.client_socket,))
        print(">> Connect Server")

        while self.alive:
            # Read a frame.
            hasFrame, frame = video.read()

            # Check if frame is not read properly.
            if not hasFrame:
                # Continue the loop.
                break

            # Flip the frame horizontally for natural (selfie-view) visualization.
            frame = cv2.flip(frame, 1)

            # Get the width and height of the frame
            frame_height, frame_width, _ = frame.shape

            # Resize the frame while keeping the aspect ratio.
            frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))
            print(frame.shape)
            # 관절 인식 수행
            results, frame, landmarks = modules.detectPose(frame, pose_video, mp_pose, mp_drawing, display=False)

            # 모든 landmark가 인식되었는지 확인
            if results.pose_world_landmarks is not None and all(
                    results.pose_world_landmarks.landmark[j].visibility > 0.1 for j in
                    [11, 12, 23, 24, 25, 26, 27, 28]):

                # 여기서부터 점 좌표 정규화
                # 왼쪽 엉덩이 점을 (0, 0, 0)이 되도록 shift
                adjust_x = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][0]
                adjust_y = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]
                adjust_z = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][2]

                landmarks_adjust_point = []

                for j in range(0, 33):
                    landmarks_adjust_point.append((landmarks[j][0] + adjust_x,
                                                   landmarks[j][1] + adjust_y,
                                                   landmarks[j][2] + adjust_z
                                                   ))

                # 엉덩이 사이의 거리를 1으로 하여 모든 관절을 정규화
                hip_distance = modules.calculateDistance3D(
                    landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value],
                    landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])

                landmarks_adjust_ratio = []

                for j in range(0, 33):
                    normalized_x = landmarks_adjust_point[j][0] / hip_distance
                    normalized_y = landmarks_adjust_point[j][1] / hip_distance
                    normalized_z = landmarks_adjust_point[j][2] / hip_distance

                    landmarks_adjust_ratio.append((normalized_x, normalized_y, normalized_z))
                # 여기까지 점 좌표 정규화

                data = []
                #print(landmarks_adjust_ratio)
                for landmark in landmarks_adjust_ratio:
                    data.extend([landmark[0], landmark[1], landmark[2]])
                #print(data)
                self.client_socket.sendto(str.encode(str(data)), (self.HOST, self.PORT))

                # Display
                cv2.imshow("Image", frame)
                cv2.waitKey(1)

        self.client_socket.close()

    def recv_data(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024*10)
                print("recive : ", data)
            except ConnectionResetError as ex:
                break
            except Exception as ex:
                print(ex)
                self.alive = False
        self.alive = False

# 웹캠 받기
video = cv2.VideoCapture("../data/test/video/test1_1.mp4")

# Initializing mediapipe pose class.
# mediapipe pose class를 초기화 한다.
mp_pose = mp.solutions.pose

# Initializing mediapipe drawing class, useful for annotation.
# mediapipe의 drawing class를 초기화한다.
mp_drawing = mp.solutions.drawing_utils

# pose detection function start
# 동영상 또는 웹캠 관절인식 결과 확인 코드
# Setup Pose function for video.
pose_video = mp_pose.Pose(static_image_mode=False,
                          min_tracking_confidence=0.1,
                          min_detection_confidence=0.8,
                          model_complexity=1,
                          smooth_landmarks=True)

client = socketClient()
client.client_run()

#
# # 웹캠 받기
# video = cv2.VideoCapture("../data/train/video/squat_1.mp4")
#
# # Initializing mediapipe pose class.
# # mediapipe pose class를 초기화 한다.
# mp_pose = mp.solutions.pose
#
# # Initializing mediapipe drawing class, useful for annotation.
# # mediapipe의 drawing class를 초기화한다.
# mp_drawing = mp.solutions.drawing_utils
#
# # pose detection function start
# # 동영상 또는 웹캠 관절인식 결과 확인 코드
# # Setup Pose function for video.
# pose_video = mp_pose.Pose(static_image_mode=False,
#                           min_tracking_confidence=0.1,
#                           min_detection_confidence=0.8,
#                           model_complexity=1,
#                           smooth_landmarks=True)
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# serverAddressPort = ("220.87.6.173", 5053)
#
# while video.isOpened():
#     # Read a frame.
#     hasFrame, frame = video.read()
#
#     # Check if frame is not read properly.
#     if not hasFrame:
#         # Continue the loop.
#         break
#
#     # Flip the frame horizontally for natural (selfie-view) visualization.
#     frame = cv2.flip(frame, 1)
#
#     # Get the width and height of the frame
#     frame_height, frame_width, _ = frame.shape
#
#     # Resize the frame while keeping the aspect ratio.
#     frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))
#
#     # 관절 인식 수행
#     results, frame, landmarks = modules.detectPose(frame, pose_video, mp_pose, mp_drawing, display=False)
#
#     # 모든 landmark가 인식되었는지 확인
#     if results.pose_world_landmarks is not None and all(
#             results.pose_world_landmarks.landmark[j].visibility > 0.1 for j in [11, 12, 23, 24, 25, 26, 27, 28]):
#
#         # 여기서부터 점 좌표 정규화
#         # 왼쪽 엉덩이 점을 (0, 0, 0)이 되도록 shift
#         adjust_x = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][0]
#         adjust_y = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]
#         adjust_z = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][2]
#
#         landmarks_adjust_point = []
#
#         for j in range(0, 33):
#             landmarks_adjust_point.append((landmarks[j][0] + adjust_x,
#                                            landmarks[j][1] + adjust_y,
#                                            landmarks[j][2] + adjust_z
#                                            ))
#
#         # 엉덩이 사이의 거리를 1으로 하여 모든 관절을 정규화
#         hip_distance = modules.calculateDistance3D(landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value],
#                                                    landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])
#
#         landmarks_adjust_ratio = []
#
#         for j in range(0, 33):
#             normalized_x = landmarks_adjust_point[j][0] / hip_distance
#             normalized_y = landmarks_adjust_point[j][1] / hip_distance
#             normalized_z = landmarks_adjust_point[j][2] / hip_distance
#
#             landmarks_adjust_ratio.append((normalized_x, normalized_y, normalized_z))
#         # 여기까지 점 좌표 정규화
#
#
#         data = []
#         print(landmarks_adjust_ratio)
#         for landmark in landmarks_adjust_ratio:
#             data.extend([landmark[0], landmark[1], landmark[2]])
#         print(data)
#         sock.sendto(str.encode(str(data)), serverAddressPort)
#
#         # Display
#         cv2.imshow("Image", frame)
#         cv2.waitKey(1)