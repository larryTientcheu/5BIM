import cv2
from  yoloV3 import YoloModelv3


class ObjectDetectionSystem:
    def __init__(self, source, yolo_config, yolo_weights, yolo_names):
        """
        Initialise le système de détection d'objets avec la source vidéo ou image et les paramètres de YOLO.
        """
        


# usage scenario
detection_system = YoloModelv3(
    0, "yolo/yolov3.cfg", "yolo/yolov3.weights", "yolo/coco.names"
)
detection_system.run()
