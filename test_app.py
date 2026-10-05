import pytest
from app import calculate_margin

def test_calculate_margin():
    assert calculate_margin(100, 70) == 30.00
    assert calculate_margin(200, 50) == 75.00

def test_invalid_revenue():
    with pytest.raises(ValueError):
        calculate_margin(0, 10)

def test_gross_profit():
    from app import calculate_gross_profit
    assert calculate_gross_profit(100, 70) == 30.00
