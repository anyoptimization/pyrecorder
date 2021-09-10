from pyrecorder.converters.matplotlib import Matplotlib


class Recorder:

    def __init__(self,
                 writer,
                 converter=Matplotlib(),
                 ) -> None:
        """

        The video object used to convert and store images.

        Parameters
        ----------
        converter
            The converter to be used to create an image out of the current plotting.

        writer
            The object responsible for writing the recorded image

        """

        super().__init__()
        self.converter = converter
        self.writer = writer

    def record(self, **kwargs):
        img = self.converter.do(**kwargs)
        self.writer.write(img)

    def close(self):
        self.writer.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.close()


def record_from_iterable(video, iteratable, func=None, **kwargs):

    for entry in iteratable:
        plot = True
        if func is not None:
            ret = func(entry, **kwargs)
            plot = not (isinstance(ret, bool) and not ret)

        if plot:
            video.record()

    video.close()
