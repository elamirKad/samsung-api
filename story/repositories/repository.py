from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session


class Repository(ABC):

    @abstractmethod
    def get(self, id: int) -> Optional[object]:
        pass

    @abstractmethod
    def create(self, obj: object) -> object:
        pass
