from absl import app, flags, logging
from object_tracker_test2 import VehiclesCounting

VC = VehiclesCounting('TEST_CAM', tiny=True, video='./data/videos/test-shoes.mp4' ,output='./outputs/countline11.avi',dont_show=True, info=True)

VC.run()