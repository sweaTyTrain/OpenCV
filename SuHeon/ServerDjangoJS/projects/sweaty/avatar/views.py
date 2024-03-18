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
        rightShoulderXCoordinate = float(request.POST.get('rightShoulderXCoordinate'))
        rightShoulderYCoordinate = float(request.POST.get('rightShoulderYCoordinate'))
        rightShoulderZCoordinate = float(request.POST.get('rightShoulderZCoordinate'))
        leftShoulderXCoordinate = float(request.POST.get('leftShoulderXCoordinate'))
        leftShoulderYCoordinate = float(request.POST.get('leftShoulderYCoordinate'))
        leftShoulderZCoordinate = float(request.POST.get('leftShoulderZCoordinate'))

        rightHipXCoordinate = float(request.POST.get('rightHipXCoordinate'))
        rightHipYCoordinate = float(request.POST.get('rightHipYCoordinate'))
        rightHipZCoordinate = float(request.POST.get('rightHipZCoordinate'))
        leftHipXCoordinate = float(request.POST.get('leftHipXCoordinate'))
        leftHipYCoordinate = float(request.POST.get('leftHipYCoordinate'))
        leftHipZCoordinate = float(request.POST.get('leftHipZCoordinate'))
        
        rightKneeXCoordinate = float(request.POST.get('rightKneeXCoordinate'))
        rightKneeYCoordinate = float(request.POST.get('rightKneeYCoordinate'))
        rightKneeZCoordinate = float(request.POST.get('rightKneeZCoordinate'))
        leftKneeXCoordinate = float(request.POST.get('leftKneeXCoordinate'))
        leftKneeYCoordinate = float(request.POST.get('leftKneeYCoordinate'))
        leftKneeZCoordinate = float(request.POST.get('leftKneeZCoordinate'))

        rightAnkleXCoordinate = float(request.POST.get('rightAnkleXCoordinate'))
        rightAnkleYCoordinate = float(request.POST.get('rightAnkleYCoordinate'))
        rightAnkleZCoordinate = float(request.POST.get('rightAnkleZCoordinate'))
        leftAnkleXCoordinate = float(request.POST.get('leftAnkleXCoordinate'))
        leftAnkleYCoordinate = float(request.POST.get('leftAnkleYCoordinate'))
        leftAnkleZCoordinate = float(request.POST.get('leftAnkleZCoordinate'))
        landmarkData = request.POST.get('landmarkData')


        # 오른쪽 허리 각도 계산 및 저장
        back_angle_right = round(
            calculateAngle3D_2(rightShoulderXCoordinate, rightShoulderYCoordinate, rightShoulderZCoordinate,
                               rightHipXCoordinate, rightHipYCoordinate, rightHipZCoordinate,
                               rightKneeXCoordinate, rightKneeYCoordinate, rightKneeZCoordinate), 1)
        # 왼쪽 허리 각도 계산 및 저장
        back_angle_left = round(
            calculateAngle3D_2(leftShoulderXCoordinate, leftShoulderYCoordinate, leftShoulderZCoordinate,
                               leftHipXCoordinate, leftHipYCoordinate, leftHipZCoordinate,
                               leftKneeXCoordinate, leftKneeYCoordinate, leftKneeZCoordinate), 1)

        # 오른쪽 무릎 각도 계산 및 저장
        knee_angle_right = round(
            calculateAngle3D_2(rightHipXCoordinate, rightHipYCoordinate, rightHipZCoordinate,
                               rightKneeXCoordinate, rightKneeYCoordinate, rightKneeZCoordinate,
                               rightAnkleXCoordinate, rightAnkleYCoordinate, rightAnkleZCoordinate), 1)
        # 왼쪽 무릎 각도 계산 및 저장
        knee_angle_left = round(
            calculateAngle3D_2(leftHipXCoordinate, leftHipYCoordinate, leftHipZCoordinate,
                               leftKneeXCoordinate, leftKneeYCoordinate, leftKneeZCoordinate,
                               leftAnkleXCoordinate, leftAnkleYCoordinate, leftAnkleZCoordinate), 1)
        
        # 발목-무릎-반대쪽 무릎 오른쪽 각도 계산 및 저장
        ankle_knee_knee_right = round(
            calculateAngle3D_2(rightAnkleXCoordinate, rightAnkleYCoordinate, rightAnkleZCoordinate,
                               rightKneeXCoordinate, rightKneeYCoordinate, rightKneeZCoordinate,
                               leftKneeXCoordinate, leftKneeYCoordinate, leftKneeZCoordinate), 1)
        # 발목-무릎-반대쪽 무릎 왼쪽 각도 계산 및 저장
        ankle_knee_knee_left = round(
            calculateAngle3D_2(leftAnkleXCoordinate, leftAnkleYCoordinate, leftAnkleZCoordinate,
                               leftKneeXCoordinate, leftKneeYCoordinate, leftKneeZCoordinate,
                               rightKneeXCoordinate, rightKneeYCoordinate, rightKneeZCoordinate), 1)
        
        # 무릎-엉덩이-반대쪽엉덩이 오른쪽 각도 계산 및 저장
        hip_hip_knee_right = round(
            calculateAngle3D_2(rightKneeXCoordinate, rightKneeYCoordinate, rightKneeZCoordinate,
                               rightHipXCoordinate, rightHipYCoordinate, rightHipZCoordinate,
                               leftHipXCoordinate, leftHipYCoordinate, leftHipZCoordinate), 1)
        # 무릎-엉덩이-반대쪽엉덩이 왼쪽 각도 계산 및 저장
        hip_hip_knee_left = round(
            calculateAngle3D_2(leftKneeXCoordinate, leftKneeYCoordinate, leftKneeZCoordinate,
                               leftHipXCoordinate, leftHipYCoordinate, leftHipZCoordinate,
                               rightHipXCoordinate, rightHipYCoordinate, rightHipZCoordinate), 1)
        

        input_data = np.array([[
            back_angle_right, back_angle_left,
            knee_angle_right, knee_angle_left,
            ankle_knee_knee_right, ankle_knee_knee_left,
            hip_hip_knee_right, hip_hip_knee_left
        ]])

        print(input_data)

        # 딥러닝 모델로 동작 분류
        # predictionsTest = model.predict(input_data) # .h5
        predictionsTest = model.predict_proba(input_data) # .joblib

        # 클래스 1 (올바른  동작)의 확률을 가져와 화면에 표시
        Nprobability_class0 = predictionsTest[0][0]  # 클래스 0에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)
        Nprobability_class1 = predictionsTest[0][1]  # 클래스 1에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)
        Nprobability_class2 = predictionsTest[0][2]  # 클래스 2에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)
        Nprobability_class3 = predictionsTest[0][3]  # 클래스 3에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)
        Nprobability_class4 = predictionsTest[0][4]  # 클래스 4에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)
        Nprobability_class5 = predictionsTest[0][5]  # 클래스 5에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)
        Nprobability_class6 = predictionsTest[0][6]  # 클래스 6에 해당하는 확률 (0은 클래스 0, 1은 클래스 1)

        Cprobability_class0 = str(Nprobability_class0)
        Cprobability_class1 = str(Nprobability_class1)
        Cprobability_class2 = str(Nprobability_class2)
        Cprobability_class3 = str(Nprobability_class3)
        Cprobability_class4 = str(Nprobability_class4)
        Cprobability_class5 = str(Nprobability_class5)
        Cprobability_class6 = str(Nprobability_class6)


        TestModel.objects.create(label_0=Cprobability_class0, label_1=Cprobability_class1, label_2=Cprobability_class2,
                                 label_3=Cprobability_class3, label_4=Cprobability_class4, label_5=Cprobability_class5,
                                 label_6=Cprobability_class6)

    latest_entry = TestModel.objects.latest('id')
    json_data0 = latest_entry.label_0
    json_data1 = latest_entry.label_1
    json_data2 = latest_entry.label_2
    json_data3 = latest_entry.label_3
    json_data4 = latest_entry.label_4
    json_data5 = latest_entry.label_5
    json_data6 = latest_entry.label_6


    return JsonResponse({'json_data0': json_data0, 'json_data1': json_data1, 'json_data2': json_data2,
                         'json_data3': json_data3, 'json_data4': json_data4, 'json_data5': json_data5,
                         'json_data6': json_data6})


def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

