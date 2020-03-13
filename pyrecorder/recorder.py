from abc import abstractmethod


class Recorder:

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def do(self, frame):
        pass

    def close(self):
        pass

    def load(self):
        pass
