from IPython.display import display

from pyrecorder.converters.matplotlib import Matplotlib


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

    def record(self, **kwargs):
        img = self.converter.do(**kwargs)
        self.converter.finalize()

        for r in self.rec:
            r.do(img)

    def close(self):
        for r in self.rec:
            r.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.close()

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


def load(fname):
    if fname.endswith("gif"):
        from IPython.display import Image
        return Image(filename=fname)

    elif fname.endswith("mp4"):
        from IPython.display import HTML
        html = """
        <div align="middle">
            <video controls>
            <source src="%s" type="video/mp4">
        </video>
        </div>
        """
        return display(HTML(data=html % fname))

    elif fname.endswith("html"):
        from IPython.display import HTML
        return HTML(filename=fname)
