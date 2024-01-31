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
# 2차원 관절 각도 계산 함수
# Calculate the angle between three 2D landmarks using unit vectors
def calculateAngle(landmark1, landmark2, landmark3):
    # 벡터를 만듭니다.
    vector1 = (landmark1[0] - landmark2[0], landmark1[1] - landmark2[1])
    vector2 = (landmark3[0] - landmark2[0], landmark3[1] - landmark2[1])

    # 벡터의 크기를 계산합니다.
    magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
    magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

    # 벡터의 내적을 계산합니다.
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    # 각도를 계산합니다.
    cos_theta = dot_product / (magnitude1 * magnitude2)
    angle_rad = math.acos(cos_theta)

    # 라디안을 각도로 변환하고 0~180 범위로 조정합니다.
    angle_deg = math.degrees(angle_rad) % 180

    return angle_deg

def calculateDistance(landmark1, landmark2):
    # point1와 point2는 각각 (x, y) 좌표를 담은 튜플 또는 리스트여야 합니다.
    x1, y1 = landmark1
    x2, y2 = landmark2

    # 각 좌표 축에서의 차이를 계산
    x_diff = x2 - x1
    y_diff = y2 - y1

    # 2차원 거리 계산
    distance = math.sqrt(x_diff**2 + y_diff**2)

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

# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture('./simulation1.mp4')

# 빈 데이터프레임 생성
df = pd.DataFrame(columns=['back_angle_R', 'back_angle_L',
                           'knee_angle_R', 'knee_angle_L',
                           'ankle_knee_knee_R', 'ankle_knee_knee_L',
                           'hip_hip_knee_R', 'hip_hip_knee_L',
                           'knee_knee_dis'])

# 반복문 일시 정지를 위한 변수
paused = False

# csv 행을 확인하기 위한 변수
i = 1

# Iterate until the video is accessed successfully.
while video.isOpened():
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
        #adjust_z = -1 * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value][2]

        landmarks_adjust_point = []

        for j in range(0, 33):
            landmarks_adjust_point.append((landmarks[j][0] + adjust_x,
                                           landmarks[j][1] + adjust_y,
                                           #landmarks[j][2] + adjust_z
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
        hip_distance = calculateDistance(landmarks_adjust_point[mp_pose.PoseLandmark.LEFT_HIP.value],
                                         landmarks_adjust_point[mp_pose.PoseLandmark.RIGHT_HIP.value])

        landmarks_adjust_ratio = []

        for j in range(0, 33):
            normalized_x = landmarks_adjust_point[j][0] / hip_distance
            normalized_y = landmarks_adjust_point[j][1] / hip_distance

            landmarks_adjust_ratio.append((normalized_x, normalized_y))
        # 여기까지 점 좌표 정규화

        # # 좌표 추출
        # x_values = [point[0] for point in landmarks_adjust_ratio[:-1]]
        # y_values = [point[1] * -1 for point in landmarks_adjust_ratio[:-1]]
        #
        # # 플롯 생성
        # plt.scatter(x_values, y_values, marker='o')
        # plt.title('Scatter Plot of 32 Points')
        # plt.xlabel('X-axis')
        # plt.ylabel('Y-axis')
        # plt.grid(True)
        # plt.show()

        # 왼쪽 허리 각도 계산 및 저장
        back_angle_left = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                         landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_HIP.value],
                                         landmarks_adjust_ratio[mp_pose.PoseLandmark.LEFT_KNEE.value]), 1)
        print(back_angle_left)
        # 오른쪽 허리 각도 계산 및 저장
        back_angle_right = round(calculateAngle(landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                          landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                          landmarks_adjust_ratio[mp_pose.PoseLandmark.RIGHT_KNEE.value]), 1)
        print(back_angle_right)
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

        # 데이터프레임에 새로운 행 추가
        now_points = [ back_angle_left, back_angle_right,
                       knee_angle_left, knee_angle_right,
                       ankle_knee_knee_left, ankle_knee_knee_right,
                       hip_hip_knee_left, hip_hip_knee_right,
                       knee_knee_dis]

        df.loc[len(df)] = now_points
        i += 1
    # 관절이 하나도 인식되지 않았음 -> 오류 메세지 출력
    else:
        cv2.putText(frame, "some or all landmarks not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print("랜드마크 검출 불가")

    # 현재 프레임 번호 출력
    print(i, '번째 csv행')

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

# csv파일로 저장
df.to_csv("squat.csv", index=False)