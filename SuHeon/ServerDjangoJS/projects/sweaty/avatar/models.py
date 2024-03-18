from django.db import models
import mediapipe as mp
import math
import cv2
import numpy as np
import tensorflow as tf
import os



class TestModel(models.Model):
    label_1 = models.CharField(max_length=100)
    label_2 = models.CharField(max_length=100)
    label_3 = models.CharField(max_length=100)





# 현재 스크립트의 디렉토리 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 모델 파일의 경로
MODEL_PATH = os.path.join(BASE_DIR, 'AImodel', 'modeltest.h5')

# 모델 로드
model = tf.keras.models.load_model(MODEL_PATH)


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# 각도 계산 함수(객체)
def calculateAngle(landmark1, landmark2, landmark3):
    # landmark1에서 landmark2로 향하는 3차원 벡터 계산
    vector1 = np.array([landmark1.x, landmark1.y, landmark1.z]) - np.array([landmark2.x, landmark2.y, landmark2.z])
    # landmark3에서 landmark2로 향하는 3차원 벡터 계산
    vector2 = np.array([landmark3.x, landmark3.y, landmark3.z]) - np.array([landmark2.x, landmark2.y, landmark2.z])

    # 벡터의 크기를 고려하지 않기 위해 단위벡터로 환산
    unit_vector1 = vector1 / np.linalg.norm(vector1)
    unit_vector2 = vector2 / np.linalg.norm(vector2)

    # 두 단위벡터의 내적을 구한다.(내적: 두 벡터의 방향 유사도(-1~1))
    dot_product = np.dot(unit_vector1, unit_vector2)

    # 내적을 바탕으로 두 단위벡터 사이의 각을 구한다.(라디안)
    angle_radians = math.acos(np.clip(dot_product, -1.0, 1.0))

    # 라디안 각을 degree로 변환
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees



# 각도 계산 함수(좌표)
def calculate_angle2(landmarkx1, landmarky1, landmarkz1, landmarkx2, landmarky2, landmarkz2, landmarkx3, landmarky3, landmarkz3):
    vector1 = np.array([landmarkx1, landmarky1, landmarkz1]) - np.array([landmarkx2, landmarky2, landmarkz2])
    # landmark3에서 landmark2로 향하는 3차원 벡터 계산
    vector2 = np.array([landmarkx3, landmarky3, landmarkz3]) - np.array([landmarkx2, landmarky2, landmarkz2])

    # 벡터의 크기를 고려하지 않기 위해 단위벡터로 환산
    unit_vector1 = vector1 / np.linalg.norm(vector1)
    unit_vector2 = vector2 / np.linalg.norm(vector2)

    # 두 단위벡터의 내적을 구한다.(내적: 두 벡터의 방향 유사도(-1~1))
    dot_product = np.dot(unit_vector1, unit_vector2)

    # 내적을 바탕으로 두 단위벡터 사이의 각을 구한다.(라디안)
    angle_radians = math.acos(np.clip(dot_product, -1.0, 1.0))

    # 라디안 각을 degree로 변환
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees






# 인공지능 뷰 (파이썬으로만 html 없이 opencv 화면 렌더링)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

class VideoCamera(object):
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        success, image = self.cap.read()
        if not success:
            return None

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self.pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            back_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])
            input_data = np.array([[
                back_angle
            ]])

            # 딥러닝 모델로 동작 분류
            predictions = model.predict(input_data)

            # 클래스 1 (올바른  동작)의 확률을 가져와 화면에 표시
            probability_class1 = predictions[0][1]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)

            probability_class2 = predictions[0][2]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)

            probability_class3 = predictions[0][3]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)

            cv2.putText(image, f"Class 1 Probability: {probability_class1:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)
            cv2.putText(image, f"Class 2 Probability: {probability_class2:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            cv2.putText(image, f"Class 3 Probability: {probability_class3:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 0, 0), 2)




        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


