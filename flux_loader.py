import cv2

class FluxLoader:
    def __init__(self, source=0):
        """__init__ Initialize the FluxLoader class with a given source. The source can be an Image path, a video file or a webcam(default).

        Keyword Arguments:
            source -- _description_ (default: {0})
        """
        self.source = source
        self.cap = cv2.VideoCapture(source)