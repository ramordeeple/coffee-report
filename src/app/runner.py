"""
Связывает загрузку данных, выбор стратегии, получение результата
"""

from typing import List

from src.app.factory import ReportFactory
from src.app.processor import DataProcessor
from src.domain.constants import NOT_FOUND_DATA
from src.domain.exceptions import DataEmptyError
from src.domain.models import ReportResult


class ReportRunner:
    @staticmethod
    def run(file_paths: List[str], report_type: str) -> ReportResult:
        raw_data = DataProcessor.collect_data(file_paths)
        if not raw_data:
            DataEmptyError(NOT_FOUND_DATA)

        strategy = ReportFactory.get_report(report_type)

        return strategy.generate(raw_data)