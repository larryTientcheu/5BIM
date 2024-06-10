import os
import urllib.request

# TODO: Put this in a class
class YoloDownloadsV3():
    def __init__(self) -> None:
        
        # URLs for the YOLO files
        self.yolo_cfg_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg"
        self.yolo_weights_url = "https://pjreddie.com/media/files/yolov3.weights"
        self.coco_names_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"

        # Chemins de destination des fichiers
        self.yolo_cfg_path = "yolo/yolov3.cfg"
        self.yolo_weights_path = "yolo/yolov3.weights"
        self.coco_names_path = "yolo/coco.names"

    def download_files(self, url, destination):
        if not os.path.exists(destination):
            print(f"Downloading {destination} from {url}")
            urllib.request.urlretrieve(url, destination)
            print(f"{destination} downloaded successfully!")
        else:
            print(f"{destination} exists already.")


    def download(self):
        # Télécharger les fichiers
        self.download_files(self.yolo_cfg_url, self.yolo_cfg_path)
        self.download_files(self.yolo_weights_url, self.yolo_weights_path)
        self.download_files(self.coco_names_url, self.coco_names_path)
