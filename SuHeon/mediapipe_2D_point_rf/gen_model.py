import gen_model_module

train_route = '../data/train/2D_point_csv/2D_point.csv'
model_save_route = '../models/rf_model_2D_point.joblib'
test_base_route = '../data/test/2D_point_csv/'

gen_model_module.RF_2D_point(train_route, model_save_route, test_base_route, False)