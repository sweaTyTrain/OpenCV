import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

# train CSV 파일 불러오기
data_train = pd.read_csv("train_new_lim_angle_0.csv")
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
    x_train.append([rows['back_angle_R'], rows['back_angle_L'],
                    rows['knee_angle_R'], rows['knee_angle_L'],
                    rows['ankle_knee_knee_R'], rows['ankle_knee_knee_L'],
                    rows['hip_hip_knee_R'], rows['hip_hip_knee_L']
                    ])

    # 원-핫 인코딩된 클래스 레이블 생성
    class_label = tf.keras.utils.to_categorical(rows['label'], num_classes)
    y_train.append(class_label)

# 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(8,), name='angle'),
    tf.keras.layers.Dense(160, activation='relu'),
    tf.keras.layers.Dense(60, activation='relu'),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax'),
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 학습 시작
model.fit(np.array(x_train), np.array(y_train), epochs=100, batch_size=16)

# 모델 저장
model.save('./models/train_new_lim_angle_0.h5')