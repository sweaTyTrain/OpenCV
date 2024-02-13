from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import threading
import time
from django.views.decorators import gzip



# 프레임을 읽어오고 저장하는 함수
def get_frame():
    global cap, global_frame

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # 프레임을 전역 변수에 저장
        global_frame = frame

        time.sleep(0.1)  # 적절한 프레임 간격을 설정

# 스트리밍을 위한 gzip 압축
@gzip.gzip_page
def video_feed(request):
    return StreamingHttpResponse(frame_generator(), content_type="multipart/x-mixed-replace;boundary=frame")

# 프레임을 생성하는 제너레이터 함수
def frame_generator():
    global global_frame

    while True:
        if global_frame is not None:
            # OpenCV에서 읽어온 프레임을 JPEG로 인코딩
            _, jpeg = cv2.imencode('.jpg', global_frame)
            frame_bytes = jpeg.tobytes()

            # boundary를 추가하여 프레임을 전송
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
        else:
            time.sleep(0.1)

# Django 뷰 함수
def index(request):
    # OpenCV VideoCapture 객체
    cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 의미, 다른 카메라를 사용하려면 수정

    # 프레임을 저장할 전역 변수
    global_frame = None

    return render(request, 'index.html')