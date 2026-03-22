from decimal import Decimal, ROUND_HALF_UP
from typing import Final

ENCODING: Final[str] = "utf-8"
CSV_EXTENSION: Final[str] = ".csv"

COLUMN_STUDENT: Final[str] = "student"
COLUMN_COFFEE_SPENT: Final[str] = "coffee_spent"

REPORT_MEDIAN_COFFEE: Final[str] = "median_coffee"

DECIMAL_PRECISION: Final[Decimal] = Decimal("0.01")
DEFAULT_ROUNDING: Final[str] = ROUND_HALF_UP

NOT_FOUND_DATA: Final[str] = "not_found_data"

CLI_ARG_FILES: Final[str] = "--files"
CLI_ARG_REPORT: Final[str] = "--report"