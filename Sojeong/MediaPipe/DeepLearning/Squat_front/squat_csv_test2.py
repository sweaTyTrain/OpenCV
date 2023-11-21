# 'C:/Users/User/JupyterTemp/image/'
import cv2
import mediapipe as mp
import math
import os
import csv

# 미디어 파이프 초기화
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# 이미지 파일이 저장된 디렉토리 경로
image_directory = '/Users/sojeongshin/PycharmProjects/mediaPipe/squat_frames'  # 실제 디렉토리 경로로 변경하세요

# CSV 파일 경로
csv_file = '/Users/sojeongshin/PycharmProjects/mediaPipe/squat.csv'

# 디렉토리 내의 모든 이미지 파일 가져오기
image_paths = [os.path.join(image_directory, file) for file in os.listdir(image_directory) if file.endswith('.jpg')]

# CSV 파일에 저장할 헤더
header = ['Image Path', 'Foot Distance', 'Left Hip to Feet Distance', 'Right Hip to Feet Distance', 'Left Knee Angle',
          'Right Knee Angle', 'Waist Angle']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for image_path in image_paths:
        # 이미지를 읽어옴
        frame = cv2.imread(image_path)

        # 미디어 파이프에 이미지 전달
        results = pose.process(frame)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # 랜드마크 인덱스
            left_shoulder_index = 11
            right_shoulder_index = 12
            left_hip_index = 23
            right_hip_index = 24
            left_knee_index = 25
            right_knee_index = 26
            left_foot_index = 31
            right_foot_index = 32

            # 랜드마크 추출
            left_shoulder = landmarks[left_shoulder_index]
            right_shoulder = landmarks[right_shoulder_index]
            left_hip = landmarks[left_hip_index]
            right_hip = landmarks[right_hip_index]
            left_knee = landmarks[left_knee_index]
            right_knee = landmarks[right_knee_index]
            left_foot = landmarks[left_foot_index]
            right_foot = landmarks[right_foot_index]

            # 양발 사이의 거리 계산
            foot_distance = math.sqrt((left_foot.x - right_foot.x) ** 2 + (left_foot.y - right_foot.y) ** 2 + (
                        left_foot.z - right_foot.z) ** 2)

            # 왼쪽 엉덩이와 발 사이의 거리 계산
            left_hip_to_feet_distance = math.sqrt(
                (left_hip.x - left_foot.x) ** 2 + (left_hip.y - left_foot.y) ** 2 + (left_hip.z - left_foot.z) ** 2)

            # 오른쪽 엉덩이와 발 사이의 거리 계산
            right_hip_to_feet_distance = math.sqrt(
                (right_hip.x - right_foot.x) ** 2 + (right_hip.y - right_foot.y) ** 2 + (
                            right_hip.z - right_foot.z) ** 2)

            # 왼쪽 무릎 각도 계산 (2D)
            left_knee_angle = math.degrees(math.atan2(left_knee.y - left_hip.y, left_knee.x - left_hip.x))

            # 오른쪽 무릎 각도 계산 (2D)
            right_knee_angle = math.degrees(math.atan2(right_knee.y - right_hip.y, right_knee.x - right_hip.x))

            # 허리 각도 계산 (왼쪽 어깨와 왼쪽 엉덩이 각도, 오른쪽 어깨와 오른쪽 엉덩이 각도의 평균 2D)
            left_waist_angle = math.degrees(math.atan2(left_hip.y - left_shoulder.y, left_hip.x - left_shoulder.x))
            right_waist_angle = math.degrees(math.atan2(right_hip.y - right_shoulder.y, right_hip.x - right_shoulder.x))
            waist_angle = (left_waist_angle + right_waist_angle) / 2

            # 결과 출력
            print(f"Image: {image_path}")
            print(f"Foot Distance: {foot_distance}")
            print(f"Left Hip to Feet Distance: {left_hip_to_feet_distance}")
            print(f"Right Hip to Feet Distance: {right_hip_to_feet_distance}")
            print(f"Left Knee Angle: {left_knee_angle}")
            print(f"Right Knee Angle: {right_knee_angle}")
            print(f"Waist Angle: {waist_angle}")
            print("\n")

            # 결과를 CSV 파일에 저장
            writer.writerow(
                [foot_distance, left_hip_to_feet_distance, right_hip_to_feet_distance, left_knee_angle,
                 right_knee_angle, waist_angle])

        # 미디어 파이프로 추출된 랜드마크와 선 그리기
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 결과를 화면에 표시
        cv2.imshow("Pose Detection", frame)
        cv2.waitKey(0)

cv2.destroyAllWindows()