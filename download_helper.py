import os
import urllib.request

# TODO: Put this in a class
class YoloDownloadsV3():
    """YoloDownloadsV3 _summary_ Class that handles the download logic of yolov3 files
    """
    def __init__(self) -> None:
        
        # URLs for the YOLO files
        self.yolo_cfg_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg"
        self.yolo_weights_url = "https://pjreddie.com/media/files/yolov3.weights"
        self.coco_names_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"

        # Destination path for the downloaded files
        self.yolo_cfg_path = "yolov3/yolov3.cfg"
        self.yolo_weights_path = "yolov3/yolov3.weights"
        self.coco_names_path = "yolov3/coco.names"

    def download_files(self, url, destination):
        """download_files _summary_ Download files only if they don't already exist

        Arguments:
            url -- string -- url to download
            destination -- string -- destination
        """
        if not os.path.exists(destination):
            print(f"Downloading {destination} from {url}")
            urllib.request.urlretrieve(url, destination)
            print(f"{destination} downloaded successfully!")
        else:
            print(f"{destination} exists already.")


    def download(self):
        """download all the files
        """
        # Dowmlaod the files
        self.download_files(self.yolo_cfg_url, self.yolo_cfg_path)
        self.download_files(self.yolo_weights_url, self.yolo_weights_path)
        self.download_files(self.coco_names_url, self.coco_names_path)
