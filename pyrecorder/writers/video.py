import cv2

from pyrecorder.writer import Writer


class Video(Writer):

    def __init__(self,
                 fname,
                 codec='mp4v',
                 fps=1,
                 ) -> None:
        super().__init__()

        self.fname = fname
        self.codec = codec
        self.fps = fps
        self.file = None

    def write(self, frame, n_frames=1):
        if self.file is None:
            height, width, layers = frame.shape

            fourcc = self.codec
            if isinstance(fourcc, str):
                fourcc = cv2.VideoWriter_fourcc(*self.codec)

            self.file = cv2.VideoWriter(self.fname,
                                        fourcc,
                                        self.fps,
                                        frameSize=(width, height))

        for k in range(n_frames):
            self.file.write(frame)

    def close(self):
        cv2.destroyAllWindows()
        if self.file is not None:
            self.file.release()
