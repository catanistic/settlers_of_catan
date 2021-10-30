from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def onStep(self):
        pass