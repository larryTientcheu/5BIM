# Introduction

This is an object detection algorithm, this algorithm is able to detect a mouse a keyboard or a laptop from an image, a video or a video feed from the users webcamera. This algorithm uses OpenCV and YOLO(You Only Look Once).

## Getting Started

* From the root of the repository, create a new python environment `.venv` using

```python
python -m venv .venv
```

* Make sure to select this environment as your working environment.
* For Windows With Unix Like Shells For Example Git Bash CLI., use

 ```sh
source venv/Scripts/activate
```

* For Windows With CMD.

 ```cmd
.\venv\Scripts\activate.bat
```

* For Windows With Power shell.

 ```powershell
.\venv\Scripts\activate.ps1
```

* After creating the environment, install the necessary packages using the file `requirements.txt`.

 ```bash
pip install -r requirements.txt
```

## How to run

* To run this script, we directly run the file `main.py` with some arguments. If using `v3`, make sure to create a directory called `yolov3` to store the downloaded v3 model.

* ```bash

  python main.py --m=modelName --s=fluxSource

  ```

* The `m` argument takes the model name: This is either `v3` or `v8`.
* The `s` argument takes the source file path: This is the exact path of the file on your computer `/path_to_image/image.jpg` or no `s` argument to use the webcam as default.
* In case you use an image, it supports `jpeg`, `png`, and `jpg` extensions only.

## Examples

* This runs the v3 yolo model with the image file mouse.jpg as an input

 ```bash

  python main.py --m=v3 --s=mouse.jpg

  ```

* This runs the v8 yolo model with the image file mouse.jpg as an input

  ```bash

  python main.py --m=v8 --s=mouse.jpg

  ```

* This runs the v3 yolo model with the webcam feed

  ```bash

  python main.py --m=v3

  ```

## Results and Observations

* Two YOLO models have been implemented, both successfully detect the objects we want, However, I have noticed that V8 model uses less computing resources and is also noticeably faster with detection. It also works well in low light.
* In the file `detection.mp4` Is an example of a working detection I did. Here we can see that it successfully detects the keyboard.
