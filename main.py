import cv2
import download_helper, flux_loader, yolo


class ObjectDetectionSystem:
    def __init__(self, source, yolo_config, yolo_weights, yolo_names):
        """
        Initialise le système de détection d'objets avec la source vidéo ou image et les paramètres de YOLO.
        """
        self.video_loader = flux_loader.FluxLoader(source)
        self.yolo_detector = yolo.YoloModel(yolo_config, yolo_weights, yolo_names)

    def make_detection(self, frame):
        detections = self.yolo_detector.detect(frame)
        for box, class_id in detections:
            x, y, w, h = box
            label = str(self.yolo_detector.classes[class_id])
            if label in ["mouse", "laptop", "keyboard"]:  # Les objets spécifiques
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )
        cv2.imshow("Detection", frame)
        return frame

    def run(self):
        """
        Exécute le système de détection d'objets.
        """
        if self.video_loader.is_image:
            frame = self.video_loader.image
            frame = self.make_detection(frame)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            while True:
                ret, frame = self.video_loader.cap.read()
                if not ret:
                    break
                frame = self.make_detection(frame)
                
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            self.video_loader.cap.release()
            cv2.destroyAllWindows()


# usage scenario
detection_system = ObjectDetectionSystem(
    0, "yolo/yolov3.cfg", "yolo/yolov3.weights", "yolo/coco.names"
)
detection_system.run()
