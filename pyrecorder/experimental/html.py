import base64
import os

from pyrecorder.writers import Writer


def to_html(_in, _out, format="video/mp4", remove_in=False, embedded=False):
    with open(_in, 'rb') as f:
        data = f.read()

    encoded = base64.b64encode(data).decode("utf-8")

    if embedded:
        src = f"data:{format};base64,{encoded}"
    else:
        src = str(_in)

    if format.startswith("video"):
        content = f"""<video controls><source type="{format}" src="{src}"></video>"""
    elif format.startswith("image"):
        content = f"""<img src="{src}" alt="gif"/>"""

    html = f"""<div align="middle">{content}</div>"""

    with open(_out, "w") as f:
        f.write(html)

    if remove_in:
        os.remove(_in)


class HTML(Writer):

    def __init__(self, recorder, embedded=False) -> None:
        super().__init__()
        self.recorder = recorder
        self.embedded = embedded

    def do(self, frame, **kwargs):
        self.recorder.do(frame, **kwargs)

    def close(self):
        self.recorder.close()

        _in = self.recorder.fname
        _out = ".".join(_in.split(".")[:-1]) + ".html"

        to_html(_in, _out, embedded=self.embedded, remove_in=self.embedded)
