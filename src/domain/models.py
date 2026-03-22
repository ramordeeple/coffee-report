from dataclasses import dataclass
from typing import List


@dataclass
class ReportResult:
    headers: List[str]
    data: List[List]
