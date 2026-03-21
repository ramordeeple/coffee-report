from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ReportResult:
    headers: List[str]
    data: List[List]

class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, raw_data: List[Dict]) -> ReportResult:
        pass
