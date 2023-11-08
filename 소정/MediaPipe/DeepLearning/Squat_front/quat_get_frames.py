import cv2
import os

# 사용할 동영상의 경로
filepath = '/Users/sojeongshin/PycharmProjects/mediaPipe/squat_video/sj_squat.mov'
# 동영상의 프레임을 저장할 디렉토리
out_path = '/Users/sojeongshin/PycharmProjects/mediaPipe/squat_frames'

# 비디오 파일 오픈
video = cv2.VideoCapture(filepath)

# frame 구하기
count=0
fps = video.get(cv2.CAP_PROP_FPS)

while (video.isOpened()):
    ret, image = video.read()
    if (int(video.get(1))):  # 앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(out_path + "/frame%d.jpg" % count, image)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1

video.release()
