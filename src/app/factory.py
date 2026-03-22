from src.domain.constants import REPORT_MEDIAN_COFFEE
from src.domain.interfaces import ReportStrategy
from src.domain.strategies import MedianCoffeeReport


class ReportFactory:
    _strategies: dict[str, ReportStrategy] = {REPORT_MEDIAN_COFFEE: MedianCoffeeReport()}

    @classmethod
    def get_report(cls, report_name: str) -> ReportStrategy:
        strategy = cls._strategies.get(report_name)
        if not strategy:
            available = ", ".join(cls._strategies.keys())
            raise ValueError(
                f"The report '{report_name} does not support. Available: {available}'"
            )

        return strategy