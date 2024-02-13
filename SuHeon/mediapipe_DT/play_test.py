import play_test_modules

# DecisionTree, 2D, angle
test_video_path = '../data/test/video/test1_1.mp4'
model_path = '../models/dt_model_2D_angle.joblib'

play_test_modules.play_2D_angle(test_video_path, model_path)

# # DecisionTree, 2D, point
# test_video_path = '../data/test/video/test1_1.mp4'
# model_path = '../models/dt_model_2D_point.joblib'
#
# play_test_modules.play_2D_point(test_video_path, model_path)

# # DecisionTree, 3D, angle
# test_video_path = '../data/test/video/test1_1.mp4'
# model_path = '../models/dt_model_3D_angle.joblib'
#
# play_test_modules.play_3D_angle(test_video_path, model_path)

# # DecisionTree, 3D, point
# test_video_path = '../data/test/video/test1_1.mp4'
# model_path = '../models/dt_model_3D_point.joblib'
#
# play_test_modules.play_3D_point(test_video_path, model_path)
