from abc import abstractmethod


class Converter:

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def do(self, **kwargs):
        pass

    def finalize(self, **kwargs):
        pass

