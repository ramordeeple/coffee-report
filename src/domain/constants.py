from decimal import Decimal
from typing import Final

ENCODING: Final[str] = "utf-8"
CSV_EXTENSION: Final[str] = ".csv"

COLUMN_STUDENT: Final[str] = "student"
COLUMN_COFFEE_SPENT: Final[str] = "coffee_spent"

REPORT_MEDIAN_COFFEE: Final[str] = "median_coffee"

DECIMAL_PRECISION: Final[Decimal] = Decimal("0.01")