import gen_model_module

train_route = '../data/train/3D_point_csv/3D_point.csv'
model_save_route = '../models/rf_model_3D_point_test.joblib'
test_base_route = '../data/test/3D_point_csv/'

gen_model_module.RF_3D_point(train_route, model_save_route, test_base_route, False)