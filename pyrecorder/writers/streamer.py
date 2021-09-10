import time

import cv2

from pyrecorder.writer import Writer


class Streamer(Writer):

    def __init__(self,
                 mode="live",
                 delay=None,
                 close_window=True,
                 sleep=None) -> None:

        super().__init__()
        self.close_window = close_window
        self.frame = None
        self.sleep = sleep

        if mode == "live":
            self.delay = 1
        elif mode == "key":
            self.delay = 0
        elif mode == "stream":
            self.delay = delay
        else:
            self.delay = None

    def write(self, frame):
        cv2.imshow('image', frame)
        if self.delay is not None:
            cv2.waitKey(self.delay)
        self.frame = frame

        if self.sleep is not None:
            time.sleep(self.sleep)

    def close(self):
        if self.close_window:
            cv2.destroyAllWindows()
        else:
            delay = self.delay

            self.delay = 0
            self.write(self.frame)

            self.delay = delay


