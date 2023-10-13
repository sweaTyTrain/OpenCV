# 라이브러리 설정
import math
import cv2
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt

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
        landmarks.append((float(landmark.x * width), float(landmark.y * height), float(landmark.z * width)))

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
# Calculate the angle between three 3D landmarks using unit vectors
def calculateAngle(landmark1, landmark2, landmark3):
    # Get the required landmarks coordinates.
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3

    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))

    # Check if the angle is less than zero.
    if angle < 0:
        # Add 360 to the found angle.
        angle += 360

    # Return the calculated angle.
    return angle


# pose detection function start

'''
# 이미지 관절인식 결과 확인 코드

# image = cv2.imread('./sqat.jfif') # 긍정적인 예
# image = cv2.imread('./pose_img3.jfif') # 부정적인 예
image = cv2.imread('./sqat_img5.PNG')
results, output_image, landmarks = detectPose(image, pose, display=True)

# landmark가 하나라도 인식되었는지 확인
if results.pose_world_landmarks:

    # 각 landmark의 신뢰도 출력
    for i in range(0, 32):
        # x, y ,z값도 출력할 수 있지만 -1~1사이 범위로 정규화 되있음
        print(i,"번째 result 신뢰도:", results.pose_world_landmarks.landmark[i].visibility)

    # 각 23번, 25번, 27번
    # 왼쪽 엉덩이, 무릎, 발목의 신뢰도
    left_ankle_visibility = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility
    left_knee_visibility = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE.value].visibility
    left_hip_visibility = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP.value].visibility


    # 해당 관절의 신뢰도가 0.9이상이면 잘 인식한것으로 판단 -> 각도 계산
    if (left_ankle_visibility > 0.9 and left_knee_visibility > 0.9 and left_hip_visibility > 0.9):
        left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                         landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
        print("\n왼쪽 무릎 각:", left_knee_angle, "\n")
    else:
        print("\n왼쪽 다리 인식 불가\n")

    # 신뢰도를 배제하고 인식한 x, y, z 좌표값 출력
    for i in range(0, 32):
        print(i, '번째 landmark:', landmarks[i])

# 관절이 하나도 인식되지 않았음 -> 오류 메세지 출력
else:
    print("랜드마크 인식 불가")
    plt.show()

'''

# 동영상 또는 웹캠 관절인식 결과 확인 코드

# 스쿼트 카운트 관련 변수
squatCnt = 0
squatBeforeState = 0
squatNowState = 0

# Setup Pose function for video.
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

# Initialize the VideoCapture object to read from the webcam.
# video = cv2.VideoCapture(0)

# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture('./sqat_video.mp4')

# Iterate until the video is accessed successfully.
while video.isOpened():
    # Read a frame.
    hasFrame, frame = video.read()

    # Check if frame is not read properly.
    if not hasFrame:
        # Continue the loop.
        continue

    # Flip the frame horizontally for natural (selfie-view) visualization.
    # frame = cv2.flip(frame, 1)

    # Get the width and height of the frame
    frame_height, frame_width, _ = frame.shape

    # Resize the frame while keeping the aspect ratio.
    frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))

    # 관절 인식 수행
    results, frame, landmarks = detectPose(frame, pose_video, display=False)
    print(landmarks)
    # landmark가 하나라도 인식되었는지 확인
    if results.pose_world_landmarks:
        # 최소 신뢰도
        min_visibility = 0.8

        # 왼쪽 엉덩이, 무릎, 발목의 신뢰도
        left_ankle_visibility = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE.value].visibility
        left_knee_visibility = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE.value].visibility
        left_hip_visibility = results.pose_world_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP.value].visibility

        # 만약 왼쪽 엉덩이, 무릎, 발목의 신뢰도가 min_visibility보다 크다면 잘 검출된 것으로 판단 -> 관절 각도 구하기 및 스쿼트 개수 카운트
        if left_ankle_visibility > min_visibility and left_knee_visibility > min_visibility and left_hip_visibility > min_visibility:
            left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value],
                                              landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                              landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])
            # 각도를 화면, 콘솔에 출력
            cv2.putText(frame, f"left_knee_angle: {left_knee_angle}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.6,(255, 0, 0), 2)
            print(left_knee_angle)

            # 만약 오른쪽 무릎의 각도가 140 이상이면 0(서있는 상태)
            if left_knee_angle >= 140:
                squatNowState = 0
            # 90 이하라면 1(앉은 상태)
            elif left_knee_angle <= 90:
                squatNowState = 1

            # 만약 squatBeforeState(이전 상태)가 1(앉은 상태)였는데
            # squatNowState(현재 상태)가 0(서있는 상태)가 되면 squatCnt증가
            if squatBeforeState == 1 and squatNowState == 0:
                squatCnt += 1

            # 다음 프레임을 받아오기 전에 squatNowState를 squatBeforeState에 기억시킨다.
            squatBeforeState = squatNowState

        # 인식된 관절의 신뢰도가 충분히 높지 않으므로 관절인식 실패 판단 -> 오류 메세지 출력
        else:
            cv2.putText(frame, "Left knee landmarks not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            print("왼쪽 다리 인식 불가")
    # 관절이 하나도 인식되지 않았음 -> 오류 메세지 출력
    else:
        cv2.putText(frame, "all landmarks not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print("랜드마크 검출 불가")

    #cv2.putText(frame, f"squatCnt: {squatCnt}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    print("스쿼트 개수:", squatCnt)

    # 프레임 출력
    cv2.imshow('Pose Detection', frame)

    # Wait until a key is pressed.
    # Retreive the ASCII code of the key pressed
    k = cv2.waitKey(1) & 0xFF

    # Check if 'ESC' is pressed.
    if (k == 27):
        # Break the loop.
        break

# Release the VideoCapture object.
video.release()

# Close the windows.
cv2.destroyAllWindows()
