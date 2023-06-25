from abc import ABC, abstractmethod
from typing import Any


class Service(ABC):

    @abstractmethod
    def create(self, *args, **kwargs) -> Any:
        pass
