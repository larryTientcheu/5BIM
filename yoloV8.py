import cv2
from ultralytics import YOLO
import flux_loader


class YoloModelV8():
    """YoloModelV8 _summary_ Yolo Version 8 detector.
    """
    def __init__(self, source):
        self.model = YOLO("yolov8n.pt")
        self.video_loader = flux_loader.FluxLoader(source)

    def detect_objects(self, frame):
        """
        Detect objects from a frame
        """
        results = self.model(frame)
        detections = []
        class_names = self.model.names
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf[0]
                class_id = int(box.cls[0])
                if confidence > 0.5:
                    detections.append(((x1, y1, x2, y2), class_id))
        return detections, class_names

    def make_detections(self, frame):
        detections, class_names = self.detect_objects(frame)
        for box, class_id in detections:
            x1, y1, x2, y2 = box
            label = class_names[class_id]
            if label in ["mouse", "laptop", "keyboard"]:  # Les objets spécifiques
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10 if y1 - 10 > 10 else y1 + 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )
        self.video_loader.display_detections(frame)

    def run(self):
        """
        Run the object detection
        """
        if self.video_loader.is_image:
            frame = self.video_loader.image
            self.make_detections(frame)

        else:
            while True:
                ret, frame = self.video_loader.cap.read()
                if not ret:
                    break
                self.make_detections(frame)
