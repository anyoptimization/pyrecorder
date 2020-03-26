import io

import cv2
import numpy as np

from pyrecorder.converter import Converter


class Plotly(Converter):

    def __init__(self, width=None, height=None, scale=None) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.scale = scale

    def do(self, fig=None, **kwargs):
        img = fig.to_image(format="png", width=self.width, height=self.height, scale=self.scale)
        _bytes = np.asarray(bytearray(img), dtype=np.uint8)
        img = cv2.imdecode(_bytes, cv2.IMREAD_COLOR)
        return img

    def do2(self, fig=None, **kwargs):
        from lxml import etree
        from reportlab.graphics import renderPM
        from svglib.svglib import SvgRenderer

        w, h, s = self.width, self.height, self.scale
        img = fig.to_image(format="svg", width=w, height=h, scale=s)

        root = etree.fromstring(img.decode("utf-8"))
        if root is None:
            raise Exception("Error while converting Plotly graphic.")

        svgRenderer = SvgRenderer("my.svg")
        drawing = svgRenderer.render(root)

        buf = io.BytesIO()
        renderPM.drawToFile(drawing, buf, fmt="PNG")
        buf.seek(0)
        _bytes = np.asarray(bytearray(buf.read()), dtype=np.uint8)
        img = cv2.imdecode(_bytes, cv2.IMREAD_COLOR)

        return img
