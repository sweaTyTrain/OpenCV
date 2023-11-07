import numpy as np
import math
import mediapipe as mp

mp_pose = mp.solutions.pose

# 앵글 계산 함수
# 3차원 관절 각도 계산 함수
# Calculate the angle between three 3D landmarks using unit vectors
def calculateAngle3D(landmark1, landmark2, landmark3):
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

# 각도를 계산할 점의 인덱스 배열을 받아 각도를 계산
def calculateData(results, landmarks, indexes):
    dataList = []
    for index in indexes:
        # 각도 계산
        if len(index) == 3:
            dataList.append(
                getAngle(results, landmarks, index)
            )
        # 길이 계산
        elif len(index) == 2:
            dataList.append(
                getDistance(results, landmarks, index)
            )
    return dataList

def getAngle(results, landmarks, index):
    p1_visibility = results.pose_world_landmarks.landmark[index[0]].visibility
    p2_visibility = results.pose_world_landmarks.landmark[index[1]].visibility
    p3_visibility = results.pose_world_landmarks.landmark[index[2]].visibility

    # 해당 관절의 신뢰도가 0.9이상이면 잘 인식한것으로 판단 -> 각도 계산
    if (p1_visibility > 0.9 and p2_visibility > 0.9 and p3_visibility > 0.9):
        angle = calculateAngle3D(
            landmarks[index[0]],
            landmarks[index[1]],
            landmarks[index[2]]
        )
        return angle
    else:
        return 0

def getDistance(results, landmarks, index):
    p1_visibility = results.pose_world_landmarks.landmark[index[0]].visibility
    p2_visibility = results.pose_world_landmarks.landmark[index[1]].visibility
     # 해당 관절의 신뢰도가 0.9이상이면 잘 인식한것으로 판단
    if (p1_visibility > 0.9 and p2_visibility > 0.9):
        p1 = landmarks[index[0]]
        p2 = landmarks[index[1]]
        distance = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
        return distance
    else:
        return 0