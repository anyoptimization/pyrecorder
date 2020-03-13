import cv2

from pyrecorder.recorder import Recorder


class Streamer(Recorder):

    def __init__(self,
                 mode="live",
                 delay=None,
                 close_window=True) -> None:
        super().__init__()
        self.close_window = close_window
        self.frame = None

        if mode == "live":
            self.delay = 1
        elif mode == "key":
            self.delay = 0
        elif mode == "stream":
            self.delay = delay
        else:
            self.delay = None

    def do(self, frame):
        cv2.imshow('image', frame)
        if self.delay is not None:
            cv2.waitKey(self.delay)

        self.frame = frame

    def close(self):
        if self.close_window:
            cv2.destroyAllWindows()
        else:
            delay = self.delay
            self.delay = 0
            self.do(self.frame)
            self.delay = delay


