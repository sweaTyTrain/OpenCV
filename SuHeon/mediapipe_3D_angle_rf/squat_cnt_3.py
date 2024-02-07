# 라이브러리 설정
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

# Setting up the Pose function.
# pose detect function에 image detect=True, 최소감지신뢰도 = 0.3, 모델 복잡도 =2를 준다.
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.1, model_complexity=1)

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
        landmarks.append((float(landmark.x), float(landmark.y)))

    # 오리지널 image와 pose detect된 image 비교
    if display:
        # 오리지널 & 아웃풋 이미지 그리기
        plt.figure(figsize=[17,17])

        plt.subplot(121)
        plt.imshow(image[:,:,::-1])
        plt.title("Original Image")
        plt.axis('off')

        plt.subplot(122)
        plt.imshow(output_image[:,:,::-1])
        plt.title("Output Image")
        plt.axis('off')

        # 3D 랜드마크 나타내기
        mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
    return results, output_image, landmarks


# 앵글 계산 함수
# 3차원 관절 각도 계산 함수
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

# 3차원 거리계산 함수
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

def rotate_around_left_hip(landmarks, rotation_angle_x=0, rotation_angle_y=0, rotation_angle_z=0):
    # 왼쪽 엉덩이의 좌표
    left_hip = np.array(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])

    # 회전 행렬 생성
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, math.cos(math.radians(rotation_angle_x)), -math.sin(math.radians(rotation_angle_x))],
                                  [0, math.sin(math.radians(rotation_angle_x)), math.cos(math.radians(rotation_angle_x))]])

    rotation_matrix_y = np.array([[math.cos(math.radians(rotation_angle_y)), 0, math.sin(math.radians(rotation_angle_y))],
                                  [0, 1, 0],
                                  [-math.sin(math.radians(rotation_angle_y)), 0, math.cos(math.radians(rotation_angle_y))]])

    rotation_matrix_z = np.array([[math.cos(math.radians(rotation_angle_z)), -math.sin(math.radians(rotation_angle_z)), 0],
                                  [math.sin(math.radians(rotation_angle_z)), math.cos(math.radians(rotation_angle_z)), 0],
                                  [0, 0, 1]])

    # 회전 각도에 따라 각각 x, y, z 축으로 회전 적용
    rotated_landmarks = []
    for landmark in landmarks:
        rotated_landmark = np.array(landmark) - left_hip
        rotated_landmark = np.dot(rotation_matrix_x, rotated_landmark)
        rotated_landmark = np.dot(rotation_matrix_y, rotated_landmark)
        rotated_landmark = np.dot(rotation_matrix_z, rotated_landmark)
        rotated_landmark += left_hip
        rotated_landmarks.append(tuple(rotated_landmark))

    return rotated_landmarks


# 리스트에서 최대값의 인덱스를 찾는 함수
def find_max_index(lst):
    max_value = lst[0]
    max_index = 0

    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i

    return max_index


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
video = cv2.VideoCapture('../simulations/simul2_1.mp4')

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
    results, frame, landmarks = detectPose(frame, pose_video, display=False)

    # 모든 landmark가 인식되었는지 확인
    if results.pose_world_landmarks is not None and all(results.pose_world_landmarks.landmark[j].visibility > 0.1 for j in [11, 12, 23, 24, 25, 26, 27, 28]):
        cv2.putText(frame, "all landmarks detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # 여기서부터 점 좌표 정규화
        # 왼쪽 엉덩이 점을 (0, 0, 0)이 되도록 shift
        adjust_x = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][0]
        adjust_y = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][1]
        adjust_z = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][2]

        landmarks_adjust_point = []

        for j in range(0, 33):
            landmarks_adjust_point.append((landmarks[j][0] + adjust_x,
                                           landmarks[j][1] + adjust_y,
                                           landmarks[j][2] + adjust_z))

        # 왼쪽 엉덩이를 기준으로 정면 보도록 모든 좌표 회전
        left_hip = np.array(landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value])
        right_hip = np.array(landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])

        rotation_angle_y = math.degrees(math.atan2(right_hip[2] - left_hip[2], right_hip[0] - left_hip[0]))

        landmarks_rotated = rotate_around_left_hip(landmarks_adjust_point, 0, rotation_angle_y, 0)
        landmarks_rotated = rotate_around_left_hip(landmarks_rotated, 270, 0, 180)

        # 엉덩이 사이의 거리를 1으로 하여 모든 관절을 정규화
        hip_distance = calculateDistance(landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value],
                                         landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])

        landmarks_adjust_ratio = []

        for j in range(0, 33):
            normalized_x = landmarks_rotated[j][0] / hip_distance
            normalized_y = landmarks_rotated[j][1] / hip_distance
            normalized_z = landmarks_rotated[j][2] / hip_distance

            landmarks_adjust_ratio.append((normalized_x, normalized_y, normalized_z))

        # 왼쪽 허리 각도 계산 및 저장
        back_angle_left = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value]), 1)

        # 오른쪽 허리 각도 계산 및 저장
        back_angle_right = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value]), 1)

        # 왼쪽 무릎 각도 계산 및 저장
        knee_angle_left = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                               landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value]), 1)

        # 오른쪽 무릎 각도 계산 및 저장
        knee_angle_right = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_ANKLE.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value]), 1)

        # 발목-무릎-반대쪽 무릎 왼쪽 각도 계산 및 저장
        ankle_knee_knee_left = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                                    landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                                    landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value]), 1)

        # 발목-무릎-반대쪽 무릎 오른쪽 각도 계산 및 저장
        ankle_knee_knee_right = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_ANKLE.value],
                                                     landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                     landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value]), 1)

        # 무릎-엉덩이-반대쪽엉덩이 왼쪽 각도 계산 및 저장
        hip_hip_knee_left = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                                 landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value],
                                                 landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value]), 1)

        # 무릎-엉덩이-반대쪽엉덩이 오른쪽 각도 계산 및 저장
        hip_hip_knee_right = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                                  landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                                  landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value]), 1)

        # 무릎-무릎 사이거리 계산 및 저장
        knee_knee_dis = round(calculateDistance(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value],
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