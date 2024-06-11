import cv2
import numpy as np
import flux_loader
import download_helper

class YoloModelv3():
    """YoloModelv3 _summary_ Yolo model version 3 
    """
    def __init__(self, source):
        self.video_loader = flux_loader.FluxLoader(source)
        yolo3files = download_helper.YoloDownloadsV3()
        yolo3files.download()

        self.net = cv2.dnn.readNetFromDarknet(yolo3files.yolo_cfg_path, yolo3files.yolo_weights_path)
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [
            self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()
        ]
        with open(yolo3files.coco_names_path, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

    def detect(self, frame):
        """detect _summary_ Detection algorithm for v3 model

        Arguments:
            frame -- _description_

        Returns:
            _description_
        """
        height, width = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(
            frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
        )
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        return [(boxes[i], class_ids[i]) for i in indices]


    def make_detection(self, frame):
        """make_detection Class specific detection

        Arguments:
            frame -- string frame representation

        Returns:
            frame -- string 
        """
        detections = self.detect(frame)
        for box, class_id in detections:
            x, y, w, h = box
            label = str(self.classes[class_id])
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
        Run the object detection algorithm
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
