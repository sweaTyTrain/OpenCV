import play_test_modules

test_video_path = '../data/test/video/test2_1.mp4'
model_path = '../models/rf_model_2D_angle.joblib'

play_test_modules.play_2D_angle(test_video_path, model_path)