import warnings

from pyrecorder.converters.matpotlib import Matplotlib


class Video:

    def __init__(self,
                 recorders,
                 converter=Matplotlib(),
                 ) -> None:

        super().__init__()
        self.converter = converter

        self.rec = recorders
        if not (isinstance(self.rec, list) or isinstance(self.rec, tuple)):
            self.rec = [self.rec]

    def record(self):
        img = self.converter.do()
        self.converter.finalize()

        for r in self.rec:
            r.do(img)

    def close(self):
        for r in self.rec:
            r.close()

    @classmethod
    def from_iteratable(cls, video, iteratable, func=None, **kwargs):
        for entry in iteratable:
            plot = True
            if func is not None:
                ret = func(entry, **kwargs)
                plot = not (isinstance(ret, bool) and not ret)

            if plot:
                video.record()

        video.close()


def load(fname, height="500px"):
    if fname.endswith("gif"):
        from IPython.display import Image
        return Image(filename=fname)

    elif fname.endswith("mp4"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            from IPython.display import HTML
            code = f"<iframe height='{height}' width='100%' src='{fname}' frameborder='0' allowfullscreen></iframe>"
            return HTML(code)
