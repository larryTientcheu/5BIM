import argparse
import cv2
from  yoloV3 import YoloModelv3
from  yoloV8 import YoloModelV8


def runV3(feed=0):
    # V3 usage scenario
    detection = YoloModelv3(feed)
    detection.run()

def runV8(feed=0):
    detection = YoloModelV8(feed)
    detection.run()

# # If program is run as a script, execute this
if __name__ == "__main__":
    # Run this script with arguments, m for the model type and s for the source
    parser = argparse.ArgumentParser(description="Script that runs Either YoloV3 or YoloV8 model with image or video file as input, or video feed from users webcam as default.")
    parser.add_argument("--m", required=True, type=str)
    parser.add_argument("--s", required=False, type=str)
    args = parser.parse_args()

    source = 0
    model = args.m
    if args.s:
        source = args.s
    
    # if model == 'v3':
    #     runV3(source)
    # if model == 'v8':
    #     runV8(source)

    runV3(source)