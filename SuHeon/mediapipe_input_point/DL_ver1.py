import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

# train CSV 파일 불러오기
data_train = pd.read_csv("train_new_0.csv")
print(len(data_train))
# 공백이 있는 행 제거
data_train = data_train.dropna()

# 클래스 레이블을 정수로 인코딩
label_encoder = LabelEncoder()
data_train['label'] = label_encoder.fit_transform(data_train['label'])
num_classes = len(label_encoder.classes_)

# x_train과 y_train 추출
x_train = []
y_train = []

for i, rows in data_train.iterrows():
    x_train.append([rows['right_shoulder_x'], rows['right_shoulder_y'], rows['right_shoulder_z'],
                    rows['left_shoulder_x'], rows['left_shoulder_y'], rows['left_shoulder_z'],
                    rows['right_hip_x'], rows['right_hip_y'], rows['right_hip_z'],
                    rows['left_hip_x'], rows['left_hip_y'], rows['left_hip_z'],
                    rows['right_knee_x'], rows['right_knee_y'], rows['right_knee_z'],
                    rows['left_knee_x'], rows['left_knee_y'], rows['left_knee_z'],
                    rows['right_ankle_x'], rows['right_ankle_y'], rows['right_ankle_z'],
                    rows['left_ankle_x'], rows['left_ankle_y'], rows['left_ankle_z']])

    # 원-핫 인코딩된 클래스 레이블 생성
    class_label = tf.keras.utils.to_categorical(rows['label'], num_classes)
    y_train.append(class_label)

# 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(24,), name='points'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax'),
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 학습 시작
model.fit(np.array(x_train), np.array(y_train), epochs=100, batch_size=32)

# 모델 저장
model.save('./models/model_new_0.h5')