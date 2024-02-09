import play_test_modules

# DNN, 2D, angle
test_video_path = '../data/test/video/test1_1.mp4'
model_path = '../models/dnn_model_2D_angle.h5'

play_test_modules.play_2D_angle(test_video_path, model_path)

# # DNN, 2D, point
# test_video_path = '../data/test/video/test1_1.mp4'
# model_path = '../models/dnn_model_2D_point.h5'
#
# play_test_modules.play_2D_point(test_video_path, model_path)

# # DNN, 3D, angle
# test_video_path = '../data/test/video/test1_1.mp4'
# model_path = '../models/dnn_model_3D_angle.h5'
#
# play_test_modules.play_3D_angle(test_video_path, model_path)

# # DNN, 3D, point
# test_video_path = '../data/test/video/test1_1.mp4'
# model_path = '../models/dnn_model_3D_point.h5'
#
# play_test_modules.play_3D_point(test_video_path, model_path)
