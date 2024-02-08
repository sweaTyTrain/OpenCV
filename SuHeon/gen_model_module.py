import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def RF_2D_angle(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
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
    rf_model = RandomForestClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    rf_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = rf_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(rf_model, model_save_route)

    if do_eval:
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

def RF_2D_point(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
    print(len(data_train))

    # 공백이 있는 행 제거
    data_train = data_train.dropna()

    # x_train과 y_train 추출
    X = data_train[['right_shoulder_x', 'right_shoulder_y',
                    'left_shoulder_x', 'left_shoulder_y',
                    'right_hip_x', 'right_hip_y',
                    'left_hip_x', 'left_hip_y',
                    'right_knee_x', 'right_knee_y',
                    'left_knee_x', 'left_knee_y',
                    'right_ankle_x', 'right_ankle_y',
                    'left_ankle_x', 'left_ankle_y']]
    y = data_train['label']

    # 데이터를 학습용과 테스트용으로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 랜덤 포레스트 모델 생성
    rf_model = RandomForestClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    rf_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = rf_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(rf_model, model_save_route)

    if do_eval:
        for i in range(1, 4):
            for j in range(1, 4):
                test_csv = f'test{i}_{j}.csv'
                test_full_path = test_base_route + test_csv

                # 저장된 모델 불러오기
                loaded_model = joblib.load(model_save_route)

                # 새로운 데이터 불러오기
                new_data = pd.read_csv(test_full_path)

                # x_new 추출
                X_new = new_data[['right_shoulder_x', 'right_shoulder_y',
                                  'left_shoulder_x', 'left_shoulder_y',
                                  'right_hip_x', 'right_hip_y',
                                  'left_hip_x', 'left_hip_y',
                                  'right_knee_x', 'right_knee_y',
                                  'left_knee_x', 'left_knee_y',
                                  'right_ankle_x', 'right_ankle_y',
                                  'left_ankle_x', 'left_ankle_y']]
                y_new = new_data['label']

                # 새로운 데이터에 대한 예측
                new_predictions = loaded_model.predict(X_new)

                # 정확도 출력
                new_accuracy = accuracy_score(y_new, new_predictions)
                print(f'New data Accuracy: {new_accuracy:.3f}')

def RF_3D_angle(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
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
    rf_model = RandomForestClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    rf_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = rf_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(rf_model, model_save_route)

    if do_eval:
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

def RF_3D_point(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
    print(len(data_train))

    # 공백이 있는 행 제거
    data_train = data_train.dropna()

    # x_train과 y_train 추출
    X = data_train[['right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z',
                    'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z',
                    'right_hip_x', 'right_hip_y', 'right_hip_z',
                    'left_hip_x', 'left_hip_y', 'left_hip_z',
                    'right_knee_x', 'right_knee_y', 'right_knee_z',
                    'left_knee_x', 'left_knee_y', 'left_knee_z',
                    'right_ankle_x', 'right_ankle_y', 'right_ankle_z',
                    'left_ankle_x', 'left_ankle_y', 'left_ankle_z']]
    y = data_train['label']

    # 데이터를 학습용과 테스트용으로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 랜덤 포레스트 모델 생성
    rf_model = RandomForestClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    rf_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = rf_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(rf_model, model_save_route)

    if do_eval:
        for i in range(1, 4):
            for j in range(1, 4):
                test_csv = f'test{i}_{j}.csv'
                test_full_path = test_base_route + test_csv

                # 저장된 모델 불러오기
                loaded_model = joblib.load(model_save_route)

                # 새로운 데이터 불러오기
                new_data = pd.read_csv(test_full_path)

                # x_new 추출
                X_new = new_data[['right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z',
                                  'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z',
                                  'right_hip_x', 'right_hip_y', 'right_hip_z',
                                  'left_hip_x', 'left_hip_y', 'left_hip_z',
                                  'right_knee_x', 'right_knee_y', 'right_knee_z',
                                  'left_knee_x', 'left_knee_y', 'left_knee_z',
                                  'right_ankle_x', 'right_ankle_y', 'right_ankle_z',
                                  'left_ankle_x', 'left_ankle_y', 'left_ankle_z']]
                y_new = new_data['label']

                # 새로운 데이터에 대한 예측
                new_predictions = loaded_model.predict(X_new)

                # 정확도 출력
                new_accuracy = accuracy_score(y_new, new_predictions)
                print(f'New data Accuracy: {new_accuracy:.3f}')


def LGBM_2D_angle(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
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
    lgbm_model = LGBMClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    lgbm_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = lgbm_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(lgbm_model, model_save_route)

    if do_eval:
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

def LGBM_2D_point(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
    print(len(data_train))

    # 공백이 있는 행 제거
    data_train = data_train.dropna()

    # x_train과 y_train 추출
    X = data_train[['right_shoulder_x', 'right_shoulder_y',
                    'left_shoulder_x', 'left_shoulder_y',
                    'right_hip_x', 'right_hip_y',
                    'left_hip_x', 'left_hip_y',
                    'right_knee_x', 'right_knee_y',
                    'left_knee_x', 'left_knee_y',
                    'right_ankle_x', 'right_ankle_y',
                    'left_ankle_x', 'left_ankle_y']]
    y = data_train['label']

    # 데이터를 학습용과 테스트용으로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # LGBM 모델 생성
    lgbm_model = LGBMClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    lgbm_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = lgbm_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(lgbm_model, model_save_route)

    if do_eval:
        for i in range(1, 4):
            for j in range(1, 4):
                test_csv = f'test{i}_{j}.csv'
                test_full_path = test_base_route + test_csv

                # 저장된 모델 불러오기
                loaded_model = joblib.load(model_save_route)

                # 새로운 데이터 불러오기
                new_data = pd.read_csv(test_full_path)

                # x_new 추출
                X_new = new_data[['right_shoulder_x', 'right_shoulder_y',
                                  'left_shoulder_x', 'left_shoulder_y',
                                  'right_hip_x', 'right_hip_y',
                                  'left_hip_x', 'left_hip_y',
                                  'right_knee_x', 'right_knee_y',
                                  'left_knee_x', 'left_knee_y',
                                  'right_ankle_x', 'right_ankle_y',
                                  'left_ankle_x', 'left_ankle_y']]
                y_new = new_data['label']

                # 새로운 데이터에 대한 예측
                new_predictions = loaded_model.predict(X_new)

                # 정확도 출력
                new_accuracy = accuracy_score(y_new, new_predictions)
                print(f'New data Accuracy: {new_accuracy:.3f}')

def LGBM_3D_angle(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
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
    lgbm_model = LGBMClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    lgbm_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = lgbm_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(lgbm_model, model_save_route)

    if do_eval:
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

def LGBM_3D_point(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
    print(len(data_train))

    # 공백이 있는 행 제거
    data_train = data_train.dropna()

    # x_train과 y_train 추출
    X = data_train[['right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z',
                    'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z',
                    'right_hip_x', 'right_hip_y', 'right_hip_z',
                    'left_hip_x', 'left_hip_y', 'left_hip_z',
                    'right_knee_x', 'right_knee_y', 'right_knee_z',
                    'left_knee_x', 'left_knee_y', 'left_knee_z',
                    'right_ankle_x', 'right_ankle_y', 'right_ankle_z',
                    'left_ankle_x', 'left_ankle_y', 'left_ankle_z']]
    y = data_train['label']

    # 데이터를 학습용과 테스트용으로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # LGBM 모델 생성
    lgbm_model = LGBMClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    lgbm_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = lgbm_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(lgbm_model, model_save_route)

    if do_eval:
        for i in range(1, 4):
            for j in range(1, 4):
                test_csv = f'test{i}_{j}.csv'
                test_full_path = test_base_route + test_csv

                # 저장된 모델 불러오기
                loaded_model = joblib.load(model_save_route)

                # 새로운 데이터 불러오기
                new_data = pd.read_csv(test_full_path)

                # x_new 추출
                X_new = new_data[['right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z',
                                  'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z',
                                  'right_hip_x', 'right_hip_y', 'right_hip_z',
                                  'left_hip_x', 'left_hip_y', 'left_hip_z',
                                  'right_knee_x', 'right_knee_y', 'right_knee_z',
                                  'left_knee_x', 'left_knee_y', 'left_knee_z',
                                  'right_ankle_x', 'right_ankle_y', 'right_ankle_z',
                                  'left_ankle_x', 'left_ankle_y', 'left_ankle_z']]
                y_new = new_data['label']

                # 새로운 데이터에 대한 예측
                new_predictions = loaded_model.predict(X_new)

                # 정확도 출력
                new_accuracy = accuracy_score(y_new, new_predictions)
                print(f'New data Accuracy: {new_accuracy:.3f}')


def XGB_2D_angle(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
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

    # XGB 모델 생성
    xgb_model = XGBClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    xgb_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = xgb_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(xgb_model, model_save_route)

    if do_eval:
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

def XGB_2D_point(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
    print(len(data_train))

    # 공백이 있는 행 제거
    data_train = data_train.dropna()

    # x_train과 y_train 추출
    X = data_train[['right_shoulder_x', 'right_shoulder_y',
                    'left_shoulder_x', 'left_shoulder_y',
                    'right_hip_x', 'right_hip_y',
                    'left_hip_x', 'left_hip_y',
                    'right_knee_x', 'right_knee_y',
                    'left_knee_x', 'left_knee_y',
                    'right_ankle_x', 'right_ankle_y',
                    'left_ankle_x', 'left_ankle_y']]
    y = data_train['label']

    # 데이터를 학습용과 테스트용으로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # XGB 모델 생성
    xgb_model = XGBClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    xgb_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = xgb_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(xgb_model, model_save_route)

    if do_eval:
        for i in range(1, 4):
            for j in range(1, 4):
                test_csv = f'test{i}_{j}.csv'
                test_full_path = test_base_route + test_csv

                # 저장된 모델 불러오기
                loaded_model = joblib.load(model_save_route)

                # 새로운 데이터 불러오기
                new_data = pd.read_csv(test_full_path)

                # x_new 추출
                X_new = new_data[['right_shoulder_x', 'right_shoulder_y',
                                  'left_shoulder_x', 'left_shoulder_y',
                                  'right_hip_x', 'right_hip_y',
                                  'left_hip_x', 'left_hip_y',
                                  'right_knee_x', 'right_knee_y',
                                  'left_knee_x', 'left_knee_y',
                                  'right_ankle_x', 'right_ankle_y',
                                  'left_ankle_x', 'left_ankle_y']]
                y_new = new_data['label']

                # 새로운 데이터에 대한 예측
                new_predictions = loaded_model.predict(X_new)

                # 정확도 출력
                new_accuracy = accuracy_score(y_new, new_predictions)
                print(f'New data Accuracy: {new_accuracy:.3f}')

def XGB_3D_angle(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
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

    # XGB 모델 생성
    xgb_model = XGBClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    xgb_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = xgb_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(xgb_model, model_save_route)

    if do_eval:
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

def XGB_3D_point(train_route, model_save_route, test_base_route, do_eval=False):
    # train CSV 파일 불러오기
    data_train = pd.read_csv(train_route)
    print(len(data_train))

    # 공백이 있는 행 제거
    data_train = data_train.dropna()

    # x_train과 y_train 추출
    X = data_train[['right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z',
                    'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z',
                    'right_hip_x', 'right_hip_y', 'right_hip_z',
                    'left_hip_x', 'left_hip_y', 'left_hip_z',
                    'right_knee_x', 'right_knee_y', 'right_knee_z',
                    'left_knee_x', 'left_knee_y', 'left_knee_z',
                    'right_ankle_x', 'right_ankle_y', 'right_ankle_z',
                    'left_ankle_x', 'left_ankle_y', 'left_ankle_z']]
    y = data_train['label']

    # 데이터를 학습용과 테스트용으로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # XGB 모델 생성
    xgb_model = XGBClassifier(n_estimators=200, random_state=66)

    # 모델 학습
    xgb_model.fit(X_train, y_train)

    # 테스트 데이터에 대한 예측
    y_pred = xgb_model.predict(X_test)

    # 정확도 출력
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Train data Accuracy: {accuracy:.3f}')

    # 모델 저장
    joblib.dump(xgb_model, model_save_route)

    if do_eval:
        for i in range(1, 4):
            for j in range(1, 4):
                test_csv = f'test{i}_{j}.csv'
                test_full_path = test_base_route + test_csv

                # 저장된 모델 불러오기
                loaded_model = joblib.load(model_save_route)

                # 새로운 데이터 불러오기
                new_data = pd.read_csv(test_full_path)

                # x_new 추출
                X_new = new_data[['right_shoulder_x', 'right_shoulder_y', 'right_shoulder_z',
                                  'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z',
                                  'right_hip_x', 'right_hip_y', 'right_hip_z',
                                  'left_hip_x', 'left_hip_y', 'left_hip_z',
                                  'right_knee_x', 'right_knee_y', 'right_knee_z',
                                  'left_knee_x', 'left_knee_y', 'left_knee_z',
                                  'right_ankle_x', 'right_ankle_y', 'right_ankle_z',
                                  'left_ankle_x', 'left_ankle_y', 'left_ankle_z']]
                y_new = new_data['label']

                # 새로운 데이터에 대한 예측
                new_predictions = loaded_model.predict(X_new)

                # 정확도 출력
                new_accuracy = accuracy_score(y_new, new_predictions)
                print(f'New data Accuracy: {new_accuracy:.3f}')