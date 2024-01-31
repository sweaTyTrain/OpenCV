import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
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

# 랜덤 포레스트 모델 생성
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# 모델 학습
rf_model.fit(X_train, y_train)

# 테스트 데이터에 대한 예측
y_pred = rf_model.predict(X_test)

# 정확도 출력
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# 모델 저장
joblib.dump(rf_model, './models/rf_model.joblib')



# 저장된 모델 불러오기
loaded_model = joblib.load('./models/rf_model.joblib')

# 새로운 데이터 불러오기
new_data = pd.read_csv("simulation1.csv")  # 예시 파일명, 실제 파일명으로 변경해주세요

# x_new 추출
X_new = new_data[['back_angle_R', 'back_angle_L',
                  'knee_angle_R', 'knee_angle_L',
                  'ankle_knee_knee_R', 'ankle_knee_knee_L',
                  'hip_hip_knee_R', 'hip_hip_knee_L',
                  'knee_knee_dis']]

# 새로운 데이터에 대한 예측
new_predictions = loaded_model.predict(X_new)
print(f'Predictions for new data: {new_predictions}')

# new_predictions의 길이 출력
print(f'Number of predictions: {len(new_predictions)}')
