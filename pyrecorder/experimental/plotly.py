import io

import cv2
import numpy as np

from pyrecorder.converter import Converter


class Plotly(Converter):

    def __init__(self, width=None, height=None, scale=1, upscale=4) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.scale = scale
        self.upscale = upscale

    def do(self, fig=None, **kwargs):
        img = fig.to_image(format="png", width=self.width, height=self.height, scale=self.scale * self.upscale)
        _bytes = np.asarray(bytearray(img), dtype=np.uint8)
        img = cv2.imdecode(_bytes, cv2.IMREAD_COLOR)

        if self.upscale > 1:
            _w, _h, _ = img.shape
            img = cv2.resize(img,
                             (int(_w / self.upscale), int(_h / self.upscale)),
                             interpolation=cv2.INTER_AREA)

        return img


    def do2(self, fig=None, **kwargs):
        from lxml import etree
        from reportlab.graphics import renderPM
        from svglib.svglib import SvgRenderer

        w, h, s = self.width, self.height, self.scale
        svg = fig.to_image(format="svg", width=w, height=h, scale=s * self.upscale)

        root = etree.fromstring(svg.decode("utf-8"))
        if root is None:
            raise Exception("Error while converting Plotly graphic.")

        svgRenderer = SvgRenderer("my.svg")
        drawing = svgRenderer.render(root)

        buf = io.BytesIO()
        renderPM.drawToFile(drawing, buf, fmt="PNG")
        buf.seek(0)
        _bytes = np.asarray(bytearray(buf.read()), dtype=np.uint8)
        img = cv2.imdecode(_bytes, cv2.IMREAD_COLOR)

        _w = int((int(root.get("width")) / self.upscale))
        _h = int((int(root.get("height")) / self.upscale))
        img = cv2.resize(img, (_w, _h), interpolation=cv2.INTER_AREA)

        return img
