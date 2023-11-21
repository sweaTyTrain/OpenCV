import pandas as pd
import numpy as np
import tensorflow as tf

# train, test csv파일 불러오기
data_train = pd.read_csv("train2.csv")

# 공백이 있는 행 제거
data_train = data_train.dropna()

# x_train과 y_train 추출
x_train = []
y_train = []

# x_train에 입력값으로 넣을 값들 불러오기
for i, rows in data_train.iterrows():
    # x_train.append([rows['back_angle_R'], rows['back_angle_L'], rows['knee_angle_R'], rows['knee_angle_L'], rows['ankle_knee_knee_R'], rows['ankle_knee_knee_L']])
    x_train.append([rows['back_angle_R'], rows['back_angle_L'], rows['knee_angle_R'], rows['knee_angle_L'], rows['ankle_knee_knee_R'], rows['ankle_knee_knee_L'], rows['hip_hip_knee_R'], rows['hip_hip_knee_L']])
# y_train에 입력값으로 넣을 값들 불러오기
for i, rows in data_train.iterrows():
    y_train.append([rows['is_stand'], rows['is_back_front'], rows['is_knee_narrow'], rows['is_knee_wide']])

# 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(4, activation='sigmoid'),
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 학습 시작
model.fit(np.array(x_train), np.array(y_train), epochs=100, batch_size=32)

# 모델 저장
model.save('./models/my_model_real2.h5')