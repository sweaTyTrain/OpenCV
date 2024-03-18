from django.shortcuts import render
from django.http import StreamingHttpResponse
from .models import *
import numpy as np
import json
from django.http import JsonResponse
import logging


logger = logging.getLogger(__name__)




#홈 화면
def index(request):
    return render(request, 'index.html')



#인공지능 모델 뷰 (따로 html 파일을 만들 필요 X)
def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')



#아바타 뷰
def second(request):
    return render(request, 'second.html')



def test(request):
    if request.method == 'POST':
        leftShoulderXCoordinate = float(request.POST.get('leftShoulderXCoordinate'))
        leftShoulderYCoordinate = float(request.POST.get('leftShoulderYCoordinate'))
        leftShoulderZCoordinate = float(request.POST.get('leftShoulderZCoordinate'))
        leftHipXCoordinate = float(request.POST.get('leftHipXCoordinate'))
        leftHipYCoordinate = float(request.POST.get('leftHipYCoordinate'))
        leftHipZCoordinate = float(request.POST.get('leftHipZCoordinate'))
        leftKneeXCoordinate = float(request.POST.get('leftKneeXCoordinate'))
        leftKneeYCoordinate = float(request.POST.get('leftKneeYCoordinate'))
        leftKneeZCoordinate = float(request.POST.get('leftKneeZCoordinate'))
        landmarkData = request.POST.get('landmarkData')



        #임시로 좌표로 받는 각도 계산 함수 사용
        back_angle = calculate_angle2(leftShoulderXCoordinate,leftShoulderYCoordinate,leftShoulderZCoordinate,leftHipXCoordinate,leftHipYCoordinate,leftHipZCoordinate,leftKneeXCoordinate,leftKneeYCoordinate,leftKneeZCoordinate)

        input_data = np.array([[
            back_angle
        ]])

        # 딥러닝 모델로 동작 분류
        predictionsTest = model.predict(input_data)

        # 클래스 1 (올바른  동작)의 확률을 가져와 화면에 표시
        Nprobability_class1 = predictionsTest[0][1]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)

        Nprobability_class2 = predictionsTest[0][2]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)

        Nprobability_class3 = predictionsTest[0][3]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)



        Cprobability_class1 = str(Nprobability_class1)
        Cprobability_class2 = str(Nprobability_class2)
        Cprobability_class3 = str(Nprobability_class3)


        TestModel.objects.create(label_1=Cprobability_class1, label_2=Cprobability_class2, label_3=Cprobability_class3)

    latest_entry = TestModel.objects.latest('id')
    json_data1 = latest_entry.label_1
    json_data2 = latest_entry.label_2
    json_data3 = latest_entry.label_3


    return JsonResponse({'json_data1': json_data1, 'json_data2': json_data2, 'json_data3': json_data3})








def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

