from django.urls import path
from webcam_app.views import index, webcam_with_pose

urlpatterns = [
    path('', index, name='index'),
    path('webcam_with_pose/', webcam_with_pose, name='webcam_with_pose'),
]