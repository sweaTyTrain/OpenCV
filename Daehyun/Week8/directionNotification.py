import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from detectPose import detectPose

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
mp_drawing = mp.solutions.drawing_utils

# landmark가 하나라도 인식되었는지 확인
def isLandmarkDetected(results):
    return results.pose_world_landmarks

# Setup Pose function for video.
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

video = cv2.VideoCapture(0)

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

    # -----------------------------------------
    if isLandmarkDetected(results):
        # 왼쪽을 보고 있는지 체크
        left_shoulder = mp_pose.PoseLandmark.LEFT_SHOULDER.value
        right_shoulder = mp_pose.PoseLandmark.RIGHT_SHOULDER.value
        landmark_left = landmarks[left_shoulder]
        landmark_right = landmarks[right_shoulder]
        
        # 최소 신뢰도
        min_visibility = 0.8
        left_visibility = results.pose_world_landmarks.landmark[left_shoulder].visibility
        right_visibility = results.pose_world_landmarks.landmark[right_shoulder].visibility

        if left_visibility > min_visibility and right_visibility > min_visibility:
            # Get the required landmarks coordinates.
            x1, y1, z1 = landmark_left
            x2, y2, z2 = landmark_right

            # 왼쪽, 오른쪽 어깨간 거리가 100 이상이면 정면
            if abs(x1 - x2) > 100:
                cv2.putText(frame, "Please turn right.", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255),2)
            else:
                # z축 기준으로 오른쪽 어깨가 더 멀리 떨어져있는지 확인
                if z1 < z2 :
                    cv2.putText(frame, "You turned right.", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                else :
                    cv2.putText(frame, "No, You turned left.", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            
    # -----------------------------------------

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

