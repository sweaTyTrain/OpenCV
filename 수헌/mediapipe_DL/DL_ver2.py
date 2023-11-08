import pandas as pd
import numpy as np
import tensorflow as tf

# train, test csv파일 불러오기
data_train = pd.read_csv("my_squat_train_csv.csv")
data_test = pd.read_csv("my_squat_test_csv.csv")

# 공백이 있는 행 제거
data_train = data_train.dropna()
data_test = data_test.dropna()

# y_train에 정답 넣기 (1:서있는, 0:앉아있는)
y_train = data_train['state'].values
x_train = []

# y_test에 정답 넣기 (1:서있는, 0:앉아있는)
y_test = data_test['state'].values
x_test = []

# x_train에 입력값으로 넣을 값들 불러오기
for i, rows in data_train.iterrows():
    x_train.append([rows['back_angle_R'], rows['back_angle_L'], rows['knee_angle_R'], rows['knee_angle_L']])

# x_test에 입력값으로 넣을 값들 불러오기
for i, rows in data_test.iterrows():
    x_test.append([rows['back_angle_R'], rows['back_angle_L'], rows['knee_angle_R'], rows['knee_angle_L']])

# 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

# 모델 학습 과정 설정
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 학습 시작
model.fit(np.array(x_train), np.array(y_train), epochs=1000)

# x_test로 학습이 잘 되었는지 확인
pre = model.predict(np.array(x_test))

# 정답개수와 오답개수를 저장할 변수
cnt_T = 0
cnt_F = 0

# x_test의 행 개수 만큼 반복
for i in range(len(pre)):
    # 일어서 있을 확률이 0.5초과이고 실제 정답이 1(서있는)이면 정답
    if pre[i] > 0.5 and y_test[i] == 1:
        cnt_T += 1
    # 일어서 있을 확률이 0.5이하이고 실제 정답이 0(앉아있는)이면 정답
    elif pre[i] <= 0.5 and y_test[i] == 0:
        cnt_T += 1
    # 나머지는 오답 처리
    else:
        cnt_F += 1
        print("틀린 csv행:", i+2)

# 결과 출력
print("맞은 개수:", cnt_T)
print("틀린 개수:", cnt_F)
print("맞춘 확률:", cnt_T/(cnt_T + cnt_F))

# 모델 저장
# model.save('./models/model_ver2.h5')