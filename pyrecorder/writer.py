from abc import abstractmethod


class Writer:

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def record(self, frame):
        pass

    def close(self):
        pass
