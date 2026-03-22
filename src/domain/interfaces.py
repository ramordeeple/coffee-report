from abc import ABC, abstractmethod
from typing import List, Dict

from src.domain.models import ReportResult


class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, raw_data: List[Dict]) -> ReportResult:
        pass