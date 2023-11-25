import cv2
import mediapipe as mp
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'webcam_app/index.html')


@require_http_methods(["GET"])
def webcam_with_pose(request):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)

    def generate():
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    print("Failed to capture image")
                    break

                # BGR을 RGB로 변환
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Pose 모델로 포즈 인식
                results = pose.process(rgb_frame)

                # 풀 바디 포즈 그리기
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                # 프레임을 JPEG 이미지로 인코딩하여 반환
                _, jpeg_frame = cv2.imencode('.jpg', frame)
                data = jpeg_frame.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n\r\n')

        cap.release()
        cv2.destroyAllWindows()

    return StreamingHttpResponse(generate(), content_type="multipart/x-mixed-replace;boundary=frame")
