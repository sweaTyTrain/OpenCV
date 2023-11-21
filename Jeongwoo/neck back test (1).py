#!/usr/bin/env python
# coding: utf-8

# In[1]:


#다중 분류 

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import regularizers

# 데이터 로드
data = pd.read_csv('test.csv')  # 'pose_data.csv'에 데이터 파일명을 맞추세요

# 클래스 레이블 설정
data['label'] = 0  # 모든 데이터를 클래스 0으로 초기화

# 클래스 1: 올바른 스쿼트 동작 (713부터 1124까지)
data.loc[0:1622, 'label'] = 1

# 클래스 2: 잘못된 동작 1 (0부터 326까지)
data.loc[1623:3100, 'label'] = 2

# 클래스 3: 잘못된 동작 2 (327부터 712까지)
data.loc[3101:4561, 'label'] = 3


# 입력 특성 선택
selected_features = ['back_angle_L']

# 데이터를 입력 특성과 레이블로 분리
X = data[selected_features]
y = data['label']

# 원-핫 인코딩 (One-Hot Encoding)을 사용하여 레이블을 범주형 형태로 변환
y = keras.utils.to_categorical(y)

# 훈련 데이터와 테스트 데이터로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 딥러닝 모델 정의
model = keras.Sequential([
    keras.layers.Input(shape=(1), name='back_angle'),  # 입력 특성 수를 1로 설정하고 열 이름을 명시
    keras.layers.Dense(64, activation='tanh', kernel_regularizer=regularizers.l2(0.01)),
    keras.layers.Dense(32, activation='tanh', kernel_regularizer=regularizers.l2(0.01)),
    keras.layers.Dense(4, activation='softmax')  # 5개의 클래스에 대한 확률 예측  0은 빈 클래스
])

# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_split=0.2)



# 모델 평가
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("테스트 손실:", test_loss)
print("테스트 정확도:", test_accuracy)

model.save('modeltest.h5')


# In[2]:


# 라이브러리 설정
import math
import cv2
import numpy as np
import pandas as pd
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf

# Initializing mediapipe pose class.
# mediapipe pose class를 초기화 한다.
mp_pose = mp.solutions.pose

# Setting up the Pose function.
# pose detect function에 image detect=True, 최소감지신뢰도 = 0.3, 모델 복잡도 =2를 준다.
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.1, model_complexity=2)

# Initializing mediapipe drawing class, useful for annotation.
# mediapipe의 drawing class를 초기화한다.
mp_drawing = mp.solutions.drawing_utils

def detectPose(image, pose, display=True):
    '''
    This function performs pose detection on an image.
    Args:
        image: The input image with a prominent person whose pose landmarks needs to be detected.
        pose: The pose setup function required to perform the pose detection.
        display: A boolean value that is if set to true the function displays the original input image, the resultant image,
                 and the pose landmarks in 3D plot and returns nothing.
    Returns:
        output_image: The input image with the detected pose landmarks drawn.
        landmarks: A list of detected landmarks converted into their original scale.
    '''
    # 예시이미지 copy하기
    output_image = image.copy()

    # 컬러 이미지 BGR TO RGB 변환
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # pose detection 수행
    results = pose.process(imageRGB)

    # input image의 너비&높이 탐색
    height, width, _ = image.shape

    # detection landmarks를 저장할 빈 list 초기화
    landmarks = []

    # landmark가 감지 되었는지 확인
    if results.pose_landmarks:

      # landmark 그리기
      mp_drawing.draw_landmarks(image=output_image, landmark_list=results.pose_landmarks, connections=mp_pose.POSE_CONNECTIONS)

      # 감지된 landmark 반복
      for landmark in results.pose_landmarks.landmark:

        # landmark를 list에 추가하기
        # 이미지의 비율에 맞게 값을 곱해 정규화 해제
        # z값은 이미지의 비율을 알 수 없으므로 대충 너비의 나누기 3한 값을 곱해준다. -> 나중에 적당한 z가중치를 찾는 코드 추가해야 할 듯
        landmarks.append((float(landmark.x * width), float(landmark.y * height), float(landmark.z * width) / 3))

    # 오리지널 image와 pose detect된 image 비교
    if display:
        # 3D 서브플롯을 생성합니다.
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = []
        y = []
        z = []

        for i in range(33):
            x.append(landmarks[i][0])
            y.append(landmarks[i][2])
            z.append(-1 * landmarks[i][1])

        # scatter 함수를 사용하여 3차원 점을 그립니다.
        ax.scatter(x, y, z)

        # 아래 옵션은 더 나은 시각화를 위해 조정되는 옵션임
        # 만일 모델이 찌그러져 나와도 실제 점은 landmarks에 제대로 찍혀있다.
        ax.set_box_aspect([30, 30, 100])  # sqat_img6.PNG 비율

        # 축 레이블을 설정합니다.
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # 그래프를 표시합니다.
        plt.show()

        # # 오리지널 & 아웃풋 이미지 그리기
        # plt.figure(figsize=[17,17])
        #
        # plt.subplot(121)
        # plt.imshow(image[:,:,::-1])
        # plt.title("Original Image")
        # plt.axis('off')
        #
        # plt.subplot(122)
        # plt.imshow(output_image[:,:,::-1])
        # plt.title("Output Image")
        # plt.axis('off')

    return results, output_image, landmarks


# 앵글 계산 함수
# 3차원 관절 각도 계산 함수
# Calculate the angle between three 3D landmarks using unit vectors
def calculateAngle(landmark1, landmark2, landmark3):
    # landmark1에서 landmark2로 향하는 3차원 벡터 계산
    vector1 = np.array(landmark1) - np.array(landmark2)
    # landmark3에서 landmark2로 향하는 3차원 벡터 계산
    vector2 = np.array(landmark3) - np.array(landmark2)

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

def calculateDistance(landmark1, landmark2):
    # point1와 point2는 각각 (x, y, z) 좌표를 담은 튜플 또는 리스트여야 합니다.
    x1, y1, z1 = landmark1
    x2, y2, z2 = landmark2

    # 각 좌표 축에서의 차이를 계산
    x_diff = x2 - x1
    y_diff = y2 - y1
    z_diff = z2 - z1

    # 3차원 거리 계산
    distance = math.sqrt(x_diff**2 + y_diff**2 + z_diff**2)

    return distance


# pose detection function start

# 동영상 또는 웹캠 관절인식 결과 확인 코드

# Setup Pose function for video.
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

# Initialize the VideoCapture object to read from the webcam.
# video = cv2.VideoCapture(0)

# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture(0)
#video = cv2.VideoCapture('./my_squat_train.mp4')

# 스쿼트 카운트 관련 변수
squatCnt = 0
squatBeforeState = 1    # 일어서 있는 상태로 초기 설정 (1)
squatNowState = 1   # 일어서 있는 상태로 초기 설정 (1)

# 반복문 일시 정지를 위한 변수
paused = False

# 프레임을 확인하기 위한 변수
i = 0

# 학습된 모델 불러오기
# model = tf.keras.models.load_model('models/model_ver1.h5')
model = tf.keras.models.load_model('modeltest.h5')

# Iterate until the video is accessed successfully.
while video.isOpened():
    i += 1
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

    # 관절 인식 수행
    results, frame, landmarks = detectPose(frame, pose_video, display=False)

    # landmark가 하나라도 인식되었는지 확인
    if results.pose_world_landmarks:
        cv2.putText(frame, "landmarks detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    # 관절이 하나도 인식되지 않았음 -> 오류 메세지 출력
    else:
        cv2.putText(frame, "all landmarks not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print("랜드마크 검출 불가")

   
    back_angle_left = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])

   
    # 현재 프레임 출력
    print(i, '번째 프레임')

    # 계산된 값들을 모델에 입력으로 넣은 후 결과 확인
    # 예측값이 1에 가까울수록 일어서있을 확률이 높고, 0에 가까울수록 앉아있을 확률이 높다.
    # pre = model.predict(np.array([[inter_foots_value, back_angle_left, back_angle_right, knee_angle_left, knee_angle_right, hip_to_heel_left, hip_to_heel_right]]))
    pre = model.predict(np.array([[back_angle_left]]))

    # 예측값이 0.8보다 높다면 일어서 있는것으로 판단
    if pre[0][1] > 0.8:
        squatNowState = 1
    # 예측값이 0.2보다 낮다면 앉아 있는것으로 판단
    elif pre[0][1] < 0.2:
        squatNowState = 0

    # 만약 squatBeforeState(이전 상태)가 0(앉은 상태)였는데
    # squatNowState(현재 상태)가 1(서있는 상태)가 되면 squatCnt증가
    
    # 다음 프레임을 받아오기 전에 squatNowState를 squatBeforeState에 기억시킨다.
    
    # pre 화면에 출력
    cv2.putText(frame, f"predict: {pre[0][1]:.4f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    print("predict:", pre[0][1])

    # 프레임 출력
    cv2.imshow('Pose Detection', frame)

    # Wait until a key is pressed.
    # Retreive the ASCII code of the key pressed
    k = cv2.waitKey(1) & 0xFF

    # Check if 'ESC' is pressed.
    if (k == 27):
        # Break the loop.
        break

    # 스페이스 바가 눌리면 paused값 not연산
    if k == 32:
        paused = not paused

    # 일시 정지 상태라면 아래 반복문을 무한 반복함
    if paused:
        while True:
            k = cv2.waitKey(0) & 0xFF
            # 다시 스페이스 바가 눌리면 paused값을 False로 바꾸고 반복분을 탈출함
            if k == 32:
                paused = False
                break

# Release the VideoCapture object.
video.release()

# Close the windows.
cv2.destroyAllWindows()

