import cv2


class FluxLoader():
    """ FluxLoader _summary_ This class handles the loading of images or videos.
    """
    def __init__(self, source):
        """__init__ Initialize the FluxLoader class with a given source. The source can be an Image path, a video file or a webcam(default).

        Keyword Arguments:
            source -- _description_ (default: {0})
        """
        self.source = source
        if isinstance(source, str) and (
            source.endswith(".jpg")
            or source.endswith(".png")
            or source.endswith(".jpeg")
        ):
            self.is_image = True
            self.image = cv2.imread(source)
        else:
            self.is_image = False
            self.cap = cv2.VideoCapture(source)

    def display_sources(self):
        """display_sources Using openCV, we can display the chosen source.
        When displaying a video, we press 'q' to exit.
        """
        if self.is_image:
            cv2.imshow("Image", self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            while True:
                is_valid, frame = self.cap.read()
                if not is_valid:
                    break
                cv2.imshow("Video", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            self.cap.release()
            cv2.destroyAllWindows()

    def display_detections(self, frame):
        """display_detections Display the detected frames

        Arguments:
            frame -- string frame to display
        """
        cv2.imshow('Detection', frame)
        if self.is_image:
            cv2.waitKey(0)  # Wait for a key press to close
            cv2.destroyAllWindows()
        else:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.cap.release()
                cv2.destroyAllWindows()
