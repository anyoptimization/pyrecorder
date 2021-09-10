import io

import cv2
import matplotlib.pyplot as plt
import numpy as np

from pyrecorder.converter import Converter


class Matplotlib(Converter):

    def __init__(self, dpi=100, close_after_recording=True) -> None:
        super().__init__()
        self.dpi = dpi
        self.close_after_recording = close_after_recording

    def do(self, fig=None, **kwargs):
        buf = io.BytesIO()

        if fig is None:
            plt.savefig(buf, format='png', dpi=self.dpi, **kwargs)
        else:
            fig.savefig(buf, format='png', dpi=self.dpi, **kwargs)

        buf.seek(0)
        _bytes = np.asarray(bytearray(buf.read()), dtype=np.uint8)
        img = cv2.imdecode(_bytes, cv2.IMREAD_COLOR)

        if self.close_after_recording:
            plt.close()

        return img

