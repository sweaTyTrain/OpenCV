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

def isSqat(left_knee_angle, squatCnt, squatBeforeState, squatNowState):
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

    return left_knee_angle, squatCnt, squatBeforeState, squatNowState

def isLandmarkDetected(results, frame):
    # landmark가 하나라도 인식되었는지 확인
    if results.pose_world_landmarks:
        return True
    return False

def calculateAngle(landmark1_idx, landmark2_idx, landmark3_idx, min_visibility, results, landmarks):
    landmark1 = landmarks[landmark1_idx]
    landmark2 = landmarks[landmark2_idx]
    landmark3 = landmarks[landmark3_idx]

    # 각 landmark의 신뢰도
    landmark1_visibility = results.pose_world_landmarks.landmark[landmark1_idx].visibility
    landmark2_visibility = results.pose_world_landmarks.landmark[landmark2_idx].visibility
    landmark3_visibility = results.pose_world_landmarks.landmark[landmark3_idx].visibility

    # 만약 왼쪽 엉덩이, 무릎, 발목의 신뢰도가 min_visibility보다 크다면 잘 검출된 것으로 판단 -> 관절 각도 구하기 및 스쿼트 개수 카운트
    if landmark1_visibility > min_visibility and landmark2_visibility > min_visibility and landmark3_visibility > min_visibility:
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

        # 계산된 각이 180이 넘는다면 반대 각을 인식한 것 이므로 angle을 조정해 준다.
        if angle > 180:
            angle = 360 - angle

        # Return the calculated angle.
        return angle
    return -1

# Setup Pose function for video.
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

# Initialize the VideoCapture object to read from the webcam.
# video = cv2.VideoCapture(0)

# Initialize the VideoCapture object to read from a video stored in the disk.
video = cv2.VideoCapture('./sqat_video.mp4')

# 스쿼트 카운트 관련 변수
squatCnt = 0
squatBeforeState = 0
squatNowState = 0

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

    if isLandmarkDetected(results, frame):
        # 최소 신뢰도
        min_visibility = 0.8

        # 왼쪽 무릎각 계산
        left_knee_angle = calculateAngle(mp_pose.PoseLandmark.LEFT_ANKLE.value,
                                         mp_pose.PoseLandmark.LEFT_KNEE.value,
                                         mp_pose.PoseLandmark.LEFT_HIP.value, min_visibility, results, landmarks)

        # 각도를 화면, 콘솔에 출력
        cv2.putText(frame, f"left_knee_angle: {left_knee_angle}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 0, 0),
                    2)
        print(left_knee_angle)

        # 스쿼트 인식 여부
        left_knee_angle, squatCnt, squatBeforeState, squatNowState = isSqat(left_knee_angle, squatCnt, squatBeforeState, squatNowState)
    else:
        cv2.putText(frame, "all landmarks not detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print("랜드마크 검출 불가")

    cv2.putText(frame, f"squatCnt: {squatCnt}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
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
