# 라이브러리 설정
import modules

import math
import cv2
import joblib
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

# Initialize the VideoCapture object to read from the webcam.
# video = cv2.VideoCapture(0)

# Initialize the VideoCapture object to read from  a video stored in the disk.
video = cv2.VideoCapture('../simulations/video/simul2_1.mp4')

# 스쿼트 카운트 관련 변수
squatCnt = 0
squatBeforeState = 1    # 일어서 있는 상태로 초기 설정 (1)
squatNowState = 1   # 일어서 있는 상태로 초기 설정 (1)
squatState = []  # 스쿼트 진행 상태를 기록하는 리스트 (올바른 자세: 1, 잘못된 자세: 0)
squatAccuracy = -1  # 스쿼트 정확도 초기값 -1
stateQueue = [-1, -1, -1, -1, -1]
class_idx_adj = -1

# 반복문 일시 정지를 위한 변수
paused = False

# 프레임을 확인하기 위한 변수
i = 0

# 학습된 모델 불러오기
model = joblib.load('./models/rf_model_10.joblib')

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
    results, frame, landmarks = modules.detectPose(frame, pose_video, mp_pose, mp_drawing, display=False)

    # 모든 landmark가 인식되었는지 확인
    if results.pose_world_landmarks is not None and all(results.pose_world_landmarks.landmark[j].visibility > 0.1 for j in [11, 12, 23, 24, 25, 26, 27, 28]):
        cv2.putText(frame, "all landmarks detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # 여기서부터 점 좌표 정규화
        # 왼쪽 엉덩이 점을 (0, 0, 0)이 되도록 shift
        adjust_x = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][0]
        adjust_y = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]
        # adjust_z = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][2]

        landmarks_adjust_point = []

        for j in range(0, 33):
            landmarks_adjust_point.append((landmarks[j][0] + adjust_x,
                                           landmarks[j][1] + adjust_y,
                                           # landmarks[j][2] + adjust_z
                                           ))

        # # 왼쪽 엉덩이를 기준으로 정면 보도록 모든 좌표 회전
        # left_hip = np.array(landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value])
        # right_hip = np.array(landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])
        #
        # rotation_angle_y = math.degrees(math.atan2(right_hip[2] - left_hip[2], right_hip[0] - left_hip[0]))
        #
        # landmarks_rotated = rotate_around_left_hip(landmarks_adjust_point, 0, rotation_angle_y, 0)
        # landmarks_rotated = rotate_around_left_hip(landmarks_rotated, 270, 0, 180)

        # 엉덩이 사이의 거리를 1으로 하여 모든 관절을 정규화
        hip_distance = modules.calculateDistance2D(landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value],
                                                   landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])

        landmarks_adjust_ratio = []

        for j in range(0, 33):
            normalized_x = landmarks_adjust_point[j][0] / hip_distance
            normalized_y = landmarks_adjust_point[j][1] / hip_distance

            landmarks_adjust_ratio.append((normalized_x, normalized_y))
        # 여기까지 점 좌표 정규화

        # 왼쪽 허리 각도 계산 및 저장
        back_angle_left = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value]), 1)

        # 오른쪽 허리 각도 계산 및 저장
        back_angle_right = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value]), 1)

        # 왼쪽 무릎 각도 계산 및 저장
        knee_angle_left = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value]), 1)

        # 오른쪽 무릎 각도 계산 및 저장
        knee_angle_right = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_ANKLE.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value]), 1)

        # 발목-무릎-반대쪽 무릎 왼쪽 각도 계산 및 저장
        ankle_knee_knee_left = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                                    landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                                    landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value]), 1)

        # 발목-무릎-반대쪽 무릎 오른쪽 각도 계산 및 저장
        ankle_knee_knee_right = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_ANKLE.value],
                                                     landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                     landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value]), 1)

        # 무릎-엉덩이-반대쪽엉덩이 왼쪽 각도 계산 및 저장
        hip_hip_knee_left = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                                 landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value],
                                                 landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value]), 1)

        # 무릎-엉덩이-반대쪽엉덩이 오른쪽 각도 계산 및 저장
        hip_hip_knee_right = round(modules.calculateAngle2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                  landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                                  landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value]), 1)

        # 무릎-무릎 사이거리 계산 및 저장
        knee_knee_dis = round(modules.calculateDistance2D(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value]), 1)

        # 빈 데이터프레임 생성
        df = pd.DataFrame(columns=['back_angle_R', 'back_angle_L',
                                   'knee_angle_R', 'knee_angle_L',
                                   'ankle_knee_knee_R', 'ankle_knee_knee_L',
                                   'hip_hip_knee_R', 'hip_hip_knee_L',
                                   'knee_knee_dis'])

        # 데이터프레임에 새로운 행 추가
        now_points = [back_angle_left, back_angle_right,
                      knee_angle_left, knee_angle_right,
                      ankle_knee_knee_left, ankle_knee_knee_right,
                      hip_hip_knee_left, hip_hip_knee_right,
                      knee_knee_dis]

        df.loc[len(df)] = now_points

        # x_new 추출
        now_points = df[['back_angle_R', 'back_angle_L',
                         'knee_angle_R', 'knee_angle_L',
                         'ankle_knee_knee_R', 'ankle_knee_knee_L',
                         'hip_hip_knee_R', 'hip_hip_knee_L',
                         'knee_knee_dis']]

        # 계산된 값들을 모델에 입력으로 넣은 후 결과 확인
        # 예측값이 1에 가까울수록 일어서있을 확률이 높고, 0에 가까울수록 앉아있을 확률이 높다.
        pre = model.predict(now_points)
        pre_reli = model.predict_proba(now_points)
        # print(pre[0])
        # print(find_max_index(pre[0])+1, "번째 클래스")
        class_list = ['good_stand', 'good_progress', 'good_sit',
                      'knee_narrow_progress', 'knee_narrow_sit',
                      'knee_wide_progress', 'knee_wide_sit']
        class_idx = pre[0]

        # 연속 5프레임 똑같은 class가 나오면 제대로 인식했다고 판정
        stateQueue.pop(0)
        stateQueue.append(class_idx)

        # 모두 같은지 판별
        all_same = all(element == stateQueue[0] for element in stateQueue)
        print("stateQueue:", stateQueue)
        print("all_same:", all_same)
        # 현재 클래스 보정
        if all_same:
            class_idx_adj = stateQueue[0]

        if class_idx_adj == -1:
            cv2.putText(frame, f"Class: Wating...", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        elif class_idx_adj == 0:
            # squatState.append(1)
            cv2.putText(frame, f"Class: {class_list[class_idx_adj]}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        elif class_idx_adj < 3:
            squatState.append(1)
            cv2.putText(frame, f"Class: {class_list[class_idx_adj]}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        else:
            squatState.append(0)
            cv2.putText(frame, f"Class: {class_list[class_idx_adj]}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        cv2.putText(frame, f"Reliability: {max(pre_reli[0])}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # 예측값이 0.8보다 높다면 일어서 있는것으로 판단
        if class_idx_adj == 0:
            squatNowState = 1
        # 예측값이 0.1보다 낮다면 앉아 있는것으로 판단
        elif class_idx_adj == 2 or class_idx_adj == 4 or class_idx_adj == 6:
            squatNowState = 0
        print("squatState: ", squatState)
        # 만약 squatBeforeState(이전 상태)가 0(앉은 상태)였는데
        # squatNowState(현재 상태)가 1(서있는 상태)가 되면 squatCnt증가
        if squatBeforeState == 0 and squatNowState == 1:
            squatAccuracy = sum(squatState)/len(squatState)

            if squatAccuracy > 0.7:
                squatCnt += 1

            squatState = []

        # 다음 프레임을 받아오기 전에 squatNowState를 squatBeforeState에 기억시킨다.
        squatBeforeState = squatNowState

        # 이번에 한 스쿼트 정확도 출력
        if squatAccuracy >= 0.7:
            cv2.putText(frame, f"{squatAccuracy * 100:.1f}%", (360, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        elif squatAccuracy >= 0:
            cv2.putText(frame, f"{squatAccuracy * 100:.1f}%", (360, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        # 스쿼트 개수 화면에 출력
        cv2.putText(frame, f"squatCnt: {squatCnt}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 관절이 하나라도 인식되지 않았음 -> 오류 메세지 출력
    else:
        cv2.putText(frame, "some or all landmarks not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print("랜드마크 검출 불가")

    # 현재 프레임 출력
    print(i, '번째 프레임')
    print('정확도:', squatAccuracy)
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