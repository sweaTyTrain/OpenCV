import gen_model_module

# XGBoost, 2D, angle
train_route = '../data/train/2D_angle_csv/2D_angle.csv'
test_base_route = '../data/test/2D_angle_csv/'
model_save_route = '../models/xgb_model_2D_angle.joblib'

gen_model_module.XGB_2D_angle(train_route, model_save_route, test_base_route, False)

# # XGBoost, 2D, point
# train_route = '../data/train/2D_point_csv/2D_point.csv'
# test_base_route = '../data/test/2D_point_csv/'
# model_save_route = '../models/xgb_model_2D_point.joblib'
#
# gen_model_module.XGB_2D_point(train_route, model_save_route, test_base_route, False)

# # XGBoost, 3D, angle
# train_route = '../data/train/3D_angle_csv/3D_angle.csv'
# test_base_route = '../data/test/3D_angle_csv/'
# model_save_route = '../models/xgb_model_3D_angle.joblib'
#
# gen_model_module.XGB_3D_angle(train_route, model_save_route, test_base_route, False)

# # XGBoost, 3D, point
# train_route = '../data/train/3D_point_csv/3D_point.csv'
# test_base_route = '../data/test/3D_point_csv/'
# model_save_route = '../models/xgb_model_3D_point.joblib'
#
# gen_model_module.XGB_3D_point(train_route, model_save_route, test_base_route, False)
