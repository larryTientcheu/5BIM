import os
import urllib.request


def download_files(url, destination):
    if not os.path.exists(destination):
        print(f"Downloading {destination} from {url}")
        urllib.request.urlretrieve(url, destination)
        print(f"{destination} downloaded successfully!")
    else:
        print(f"{destination} exists already.")


# URLs for the YOLO files
yolo_cfg_url = (
    "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg"
)
yolo_weights_url = "https://pjreddie.com/media/files/yolov3.weights"
coco_names_url = (
    "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
)

# Chemins de destination des fichiers
yolo_cfg_path = "yolo/yolov3.cfg"
yolo_weights_path = "yolo/yolov3.weights"
coco_names_path = "yolo/coco.names"

if __name__ == "main":
    # Télécharger les fichiers
    download_files(yolo_cfg_url, yolo_cfg_path)
    download_files(yolo_weights_url, yolo_weights_path)
    download_files(coco_names_url, coco_names_path)
