import cv2
import os
import numpy as np
"""
BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "MidleHip": 8, "RHip": 9,
              "RKnee": 10, "RAnkle": 11, "LHip": 12, "LKnee": 13, "LAnkle": 14,
              "Background": 15}

POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
              ["LElbow", "LWrist"], ["Neck", "MidleHip"], ["MidleHip", "RHip"], ["RHip", "RKnee"],
              ["RKnee", "RAnkle"], ["MidleHip", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]
"""

BODY_PARTS = {0: "Nose", 1: "Neck", 2: "RShoulder", 3: "RElbow", 4: "RWrist",
                      5: "LShoulder", 6: "LElbow", 7: "LWrist", 8: "MidHip", 9: "RHip",
                      10: "RKnee", 11: "RAnkle", 12: "LHip", 13: "LKnee", 14: "LAnkle",
                      15: "REye", 16: "LEye", 17: "REar", 18: "LEar", 19: "LBigToe",
                      20: "LSmallToe", 21: "LHeel", 22: "RBigToe", 23: "RSmallToe", 24: "RHeel", 25: "Background"}

POSE_PAIRS = [[0, 1], [0, 15], [0, 16], [1, 2], [1, 5], [1, 8], [8, 9], [8, 12], [9, 10], [12, 13], [2, 3],
                      [3, 4], [5, 6], [6, 7], [10, 11], [13, 14], [15, 17], [16, 18], [14, 21], [19, 21], [20, 21],
                      [11, 24], [22, 24], [23, 24]]

# 각 파일 path
path = os.path.dirname(os.path.abspath(__file__))
protoFile = path + "/" + "pose_deploy.prototxt"
weightsFile = path + "/" + "pose_iter_584000.caffemodel"


# 위의 path에 있는 network 모델 불러오기
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

# 쿠다 사용 안하면 밑에 이미지 크기를 줄이는게 나을 것이다
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA) #벡엔드로 쿠다를 사용하여 속도향상을 꾀한다
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA) # 쿠다 디바이스에 계산 요청


# 카메라 연결
capture = cv2.VideoCapture(0)  # 카메라 정보 받아옴
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #카메라 속성 설정
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # width:너비, height: 높이

inputWidth = 200
inputHeight = 200
inputScale = 1.0 / 255

# 스쿼트 카운트 관련 변수
squatCnt = 0
squatBeforeState = 0
squatNowState = 0

# 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 비디오 코덱 설정 (MP4로 저장)
output_filename = "output_video.mp4"  # 저장할 비디오 파일 이름
output_frame_rate = 10.0  # 비디오 프레임 속도 (fps)
output_resolution = (640, 480)  # 저장할 비디오 해상도

out = cv2.VideoWriter(output_filename, fourcc, output_frame_rate, output_resolution)

# 반복문을 통해 카메라에서 프레임을 지속적으로 받아옴
while cv2.waitKey(1) < 0:  # 아무 키나 누르면 끝난다.
    # 웹캠으로부터 영상 가져옴
    hasFrame, frame = capture.read()

    # 영상이 커서 느리면 사이즈를 줄이자
    # frame = cv2.resize(frame, dsize=(320,240),interpolation=cv2.INTER_AREA)

    # 웹캠으로부터 영상을 가져올 수 없으면 웹캠 중지
    if not hasFrame:
        cv2.waitKey()
        break

    #
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    inpBlob = cv2.dnn.blobFromImage(
        frame,
        inputScale,
    (inputWidth, inputHeight),
    (0, 0, 0),
        swapRB=False,
        crop=False)

    imgb = cv2.dnn.imagesFromBlob(inpBlob)
    cv2.imshow("motion", (imgb[0]*255.0).astype(np.uint8))

    # network에 넣어주기
    net.setInput(inpBlob)

    # 결과 받아오기
    output = net.forward()

    # 키포인트 검출시 이미지에 그려줌
    points = []
    for i in range(0, 25):
        # 해당 신체부위 신뢰도 얻음.
        probMap = output[0, i, :, :]

        # global 최대값 찾기
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        # 원래 이미지에 맞게 점 위치 변경
        x = (frameWidth * point[0]) / output.shape[3]
        y = (frameHeight * point[1]) / output.shape[2]

        # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로
        if prob > 0.1:
            cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 255), thickness=-1,
                       lineType=cv2.FILLED)  # circle(그릴곳, 원의 중심, 반지름, 색)
            cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
                        lineType=cv2.LINE_AA)
            points.append((int(x), int(y)))
        else:
            points.append(None)

    # 각 POSE_PAIRS별로 선 그어줌 (머리 - 목, 목 - 왼쪽어깨, ...)
    for pair in POSE_PAIRS:
        partA = pair[0]  # Head
        partB = pair[1]  # Neck

        # partA와 partB 사이에 선을 그어줌 (cv2.line)
        if points[partA] and points[partB]:
            cv2.line(frame, points[partA], points[partB], (0, 255, 0), 2)
        # print(points[0]) # 머리의 x, y좌표를 콘솔에 출력

    # RHip, RKnee, RAnkle 세 점의 인덱스
    RHip_idx = 9    # RHip
    RKnee_idx = 10  # RKnee
    RAnkle_idx = 11 # RAnkle

    # RKnee에서 RHip로 향하는 벡터 계산
    if points[RKnee_idx] and points[RHip_idx]:  # 만약 오른쪽 엉덩이 점과 오른쪽 무릎 점이 인식이 된다면
        vector1 = np.array(points[RHip_idx]) - np.array(points[RKnee_idx])  # 두 점 간의 벡터 구하기
    else:
        vector1 = None  # 두 점 중 하나라도 인식이 안되면 벡터를 못구함

    # RKnee에서 RAnkle로 향하는 벡터 계산
    if points[RKnee_idx] and points[RAnkle_idx]:    # 만약 오른쪽 무릎 점과 오른쪽 발목 점이 인식이 된다면
        vector2 = np.array(points[RAnkle_idx]) - np.array(points[RKnee_idx])    # 두 점 간의 벡터 구하기
    else:
        vector2 = None  # 두 점 중 하나라도 인식이 안되면 벡터를 못구함

    # 벡터가 모두 유효한 경우 각도 계산
    if vector1 is not None and vector2 is not None:
        # 각도 계산 (라디안)
        # 두 벡터의 내적을 두 벡터의 크기의 곱으로 나눠 코사인 값을 계산하고, np.arccos()를 사용하여 아크코사인 값을 계산한다.
        # 최종적으로 RKnee_angle_rad에 두 벡터 사이의 각도가 라디안 값으로 저장된다.
        RKnee_angle_rad = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
        # 라디안을 도로 변환
        RKnee_angle_deg = np.degrees(RKnee_angle_rad)
        # 결과 출력
        print("RKnee 각도(도):", RKnee_angle_deg)

        # 만약 오른쪽 무릎의 각도가 160 이상이면 0(서있는 상태)
        if RKnee_angle_deg >= 160:
            squatNowState = 0
        # 90 이하라면 1(앉은 상태)
        elif RKnee_angle_deg <= 90:
            squatNowState = 1

        # 만약 squatBeforeState(이전 상태)가 1(앉은 상태)였는데
        # squatNowState(현재 상태)가 0(서있는 상태)가 되면 squatCnt증가
        if squatBeforeState == 1 and squatNowState == 0:
            squatCnt += 1

        # 다음 프레임을 받아오기 전에 squatNowState를 squatBeforeState에 기억시킨다.
        squatBeforeState = squatNowState
        print("스쿼트 개수:", squatCnt)

        # squatCnt와 RKnee_angle_deg를 화면에 출력
        cv2.putText(frame, f"squatCnt: {squatCnt}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.putText(frame, f"RKnee_angle_deg: {RKnee_angle_deg:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    else:
        print("RKnee 각도를 계산할 수 없습니다.")

    # 프레임을 비디오에 쓰기
    out.write(frame)

    # 프레임 출력
    cv2.imshow("Output-Keypoints", frame)

# 비디오 파일 닫기
out.release()

capture.release()  # 카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows()  # 모든 윈도우 창 닫음