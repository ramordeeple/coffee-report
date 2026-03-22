from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ReportResult:
    headers: List[str]
    data: List[List]
