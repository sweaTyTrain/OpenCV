import play_test_modules

test_video_path = '../data/test/video/test1_1.mp4'
model_path = '../models/rf_model_3D_point.joblib'

play_test_modules.play_3D_point(test_video_path, model_path)