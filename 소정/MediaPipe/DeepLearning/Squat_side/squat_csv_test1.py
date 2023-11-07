# 'C:/Users/User/JupyterTemp/image/'
import cv2
import mediapipe as mp
import math
import os
import csv
import PoseModule as pm

detector = pm.poseDetector()

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
header = ['Image num', 'Ankle angle', 'Knee angle', 'Hip angle']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for image_path in image_paths:
        # 이미지를 읽어옴
        frame = cv2.imread(image_path)

        # 미디어 파이프에 이미지 전달
        # results = pose.process(frame)

        img = detector.findPose(frame, False)
        lmList = detector.findPosition(frame, False)

        # 스퀏을 위한 왼쪽 랜드마크 인덱스
        toe_index = 31
        ankle_index = 27
        knee_index = 25
        hip_index = 23
        shoulder_index = 11

        # 발목 각도 계산
        angle_ankle = detector.findAngle(frame, toe_index, ankle_index, knee_index)

        # 무릎 각도 계산
        angle_knee = detector.findAngle(frame, ankle_index, knee_index, hip_index)

        # 힙 각도 계산
        angle_hip = detector.findAngle(frame, knee_index, hip_index, shoulder_index)

        # 결과 출력
        print(f"Image: {image_path}")
        print(f"ankle Angle: {angle_ankle}")
        print(f"Knee Angle: {angle_knee}")
        print(f"hip Angle: {angle_hip}")
        print("\n")

        # 결과를 CSV 파일에 저장
        writer.writerow(
            [image_path, angle_ankle, angle_knee, angle_hip])

        # # 미디어 파이프로 추출된 랜드마크와 선 그리기
        # mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 결과를 화면에 표시
        cv2.imshow("Pose Detection", frame)
        cv2.waitKey(0)

cv2.destroyAllWindows()