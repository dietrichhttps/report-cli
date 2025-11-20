from abc import ABC, abstractmethod
from typing import List
from ..models import Employee

class Report(ABC):
    @abstractmethod
    def generate(self, employees: List[Employee]) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass