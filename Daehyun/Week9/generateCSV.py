import csv
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from detectPose import detectPose
from calculateData import calculateData

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
mp_drawing = mp.solutions.drawing_utils
poseLandmark = mp_pose.PoseLandmark
"""
1. 양 발 간의 넓이
2. 허리 각도 (이걸 어떻게 알 수 있죠..? 일단 골반 각도로 대체)
3. 왼쪽 무릎 각도
4. 오른쪽 무릎 각도
5. (왼쪽) 엉덩이와 발 사이의 거리
"""
SQUAT_INDEXES = [
    [poseLandmark.LEFT_ANKLE.value, poseLandmark.RIGHT_ANKLE.value],
    [poseLandmark.LEFT_SHOULDER.value, poseLandmark.LEFT_HIP.value,poseLandmark.LEFT_KNEE.value],
    [poseLandmark.LEFT_ANKLE.value, poseLandmark.LEFT_KNEE.value,poseLandmark.LEFT_HIP.value],
    [poseLandmark.RIGHT_ANKLE.value, poseLandmark.RIGHT_KNEE.value,poseLandmark.RIGHT_HIP.value],
    [poseLandmark.LEFT_HIP.value, poseLandmark.LEFT_ANKLE.value],
]

# landmark가 하나라도 인식되었는지 확인
def isLandmarkDetected(results):
    return results.pose_world_landmarks

# Setup Pose function for video.
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

video = cv2.VideoCapture('./Practice/Daehyun/Week9/squat2.mp4')
resultData = []

frameCnt = 0
while video.isOpened():
    # Read a frame.
    hasFrame, frame = video.read()
    
    frameCnt+=1
    if frameCnt == 188:
        break
    # Check if frame is not read properly.
    if not hasFrame:
        break

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
        data = calculateData(results, landmarks, SQUAT_INDEXES)
        resultData.append(data)
        for i, arr in enumerate(data):
            print(i, arr)
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

# 데이터 저장
print('write to csv')
print('total frame: ', len(resultData))
#f = open('./Practice/Daehyun/Week9/data1.csv', 'w') # squat1
f = open('./Practice/Daehyun/Week9/data2.csv', 'w') # squat2
writer = csv.writer(f)
writer.writerow(['distance between two feet','waist angle','Left knee angle','Right knee angle','distance between the hips and feet'])
writer.writerows(resultData)
f.close()

# 27~45, 110~122 -> squat1
# 70~95, 165~188 -> squat2
label_data = np.array([[0] for i in range(len(resultData))])
#label_data[27:46] = [1] # squat1
#label_data[110:123] = [1] # squat1
label_data[70:95] = [1] # squat2
label_data[165:188] = [1] # squat2
# f = open('./Practice/Daehyun/Week9/data1_result.csv', 'w') # squat1
f = open('./Practice/Daehyun/Week9/data2_result.csv', 'w') # squat2
writer = csv.writer(f)
writer.writerow(['0: stand', '1: squat'])
writer.writerows(label_data)
f.close()


# Release the VideoCapture object.
video.release()

# Close the windows.
cv2.destroyAllWindows()

