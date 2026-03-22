from decimal import Decimal, InvalidOperation
from statistics import median
from typing import List, Dict

from src.domain.constants import COLUMN_STUDENT, COLUMN_COFFEE_SPENT, DECIMAL_PRECISION, DEFAULT_ROUNDING
from src.domain.interfaces import ReportStrategy
from src.domain.models import ReportResult


class MedianCoffeeReport(ReportStrategy):
    def generate(self, raw_data: List[Dict]) -> ReportResult:
        student_spends: Dict[str, List[Decimal]] = {}

        for row in raw_data:
            name = row.get(COLUMN_STUDENT)
            if not name:
                continue

            try:
                val = row.get(COLUMN_COFFEE_SPENT)
                spend = Decimal(val) if val else Decimal(0.00)
                student_spends.setdefault(name, []).append(spend)

            except (InvalidOperation, TypeError, ValueError):
                continue

        results = []
        for name, spends in student_spends.items():
            if not spends:
                continue

            res_median = median(spends)

            formatted_median = res_median.quantize(DECIMAL_PRECISION, rounding=DEFAULT_ROUNDING)
            results.append([name, formatted_median])

        return ReportResult(
            headers=["Student", "Median Coffee Spent"],
            data=results
        )