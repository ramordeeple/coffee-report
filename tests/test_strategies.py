from decimal import Decimal

from src.domain.strategies import MedianCoffeeReport


def test_median_coffee_calculation():
    mock_data = [
        {"student": "Иван", "coffee_spent": Decimal("100.00")},
        {"student": "Иван", "coffee_spent": Decimal("200.00")},
        {"student": "Олег", "coffee_spent": Decimal("500.00")},
    ]

    strategy = MedianCoffeeReport()
    result = strategy.generate(mock_data)

    assert result.headers == ["Student", "Median Coffee Spent"]

    ivan_row = next(row for row in result.data if row[0] == "Иван")
    assert ivan_row[1] == Decimal("150.00")

    oleg_row = next(row for row in result.data if row[0] == "Олег")
    assert oleg_row[1] == Decimal("500.00")


def test_median_ignore_invalid_data():
    mock_data = [
        {"student": "Анна", "coffee_spent": Decimal("100.00")},
        {"student": "Анна", "coffee_spent": "not_a_number"},
        {"student": "", "coffee_spent": Decimal("500.00")},
    ]

    strategy = MedianCoffeeReport()
    result = strategy.generate(mock_data)

    assert len(result.data) == 1
    assert result.data[0][0] == "Анна"
    assert result.data[0][1] == Decimal("100.00")