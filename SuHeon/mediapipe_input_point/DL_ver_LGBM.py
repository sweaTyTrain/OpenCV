import joblib
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# train CSV 파일 불러오기
data_train = pd.read_csv("train_new_angle_dis_2D_0.csv")
print(len(data_train))

# 공백이 있는 행 제거
data_train = data_train.dropna()

# x_train과 y_train 추출
X = data_train[['back_angle_R', 'back_angle_L',
                'knee_angle_R', 'knee_angle_L',
                'ankle_knee_knee_R', 'ankle_knee_knee_L',
                'hip_hip_knee_R', 'hip_hip_knee_L',
                'knee_knee_dis']]
y = data_train['label']

# 데이터를 학습용과 테스트용으로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LGBM 모델 생성
lgbm_model = LGBMClassifier(n_estimators=100, random_state=42)

# 모델 학습
lgbm_model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
y_pred = lgbm_model.predict(X_test)

# 정확도 출력
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# 모델 저장
joblib.dump(lgbm_model, 'lgbm_model.joblib')

# 저장된 모델 불러오기
loaded_model = joblib.load('lgbm_model.joblib')

# 새로운 데이터에 대한 예측
new_data = pd.read_csv("squat.csv")
new_data = new_data.dropna()
X_new = new_data[['back_angle_R', 'back_angle_L',
                  'knee_angle_R', 'knee_angle_L',
                  'ankle_knee_knee_R', 'ankle_knee_knee_L',
                  'hip_hip_knee_R', 'hip_hip_knee_L',
                  'knee_knee_dis']]
new_predictions = loaded_model.predict(X_new)
print(f'Predictions for new data: {new_predictions}')
