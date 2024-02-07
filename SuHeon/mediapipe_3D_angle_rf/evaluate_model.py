import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

model_save_route = '../models/rf_model_3D_angle.joblib'
test_base_route = '../data/test/3D_angle_csv/'

for i in range(1, 4):
    for j in range(1, 4):
        test_csv = f'test{i}_{j}.csv'
        test_full_path = test_base_route + test_csv

        # 저장된 모델 불러오기
        loaded_model = joblib.load(model_save_route)

        # 새로운 데이터 불러오기
        new_data = pd.read_csv(test_full_path)

        # x_new 추출
        X_new = new_data[['back_angle_R', 'back_angle_L',
                          'knee_angle_R', 'knee_angle_L',
                          'ankle_knee_knee_R', 'ankle_knee_knee_L',
                          'hip_hip_knee_R', 'hip_hip_knee_L',
                          'knee_knee_dis']]
        y_new = new_data['label']

        # 새로운 데이터에 대한 예측
        new_predictions = loaded_model.predict(X_new)

        # 정확도 출력
        new_accuracy = accuracy_score(y_new, new_predictions)
        print(f'New data Accuracy: {new_accuracy:.3f}')