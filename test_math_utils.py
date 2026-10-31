import pytest
from math_utils import add, subtract, multiply, divide, power


def test_add_positive_numbers():
    assert add(5, 7) == 12


def test_add_negative_numbers():
    assert add(-3, -9) == -12


def test_subtract_positive_result():
    assert subtract(15, 4) == 11


def test_multiply_by_zero():
    assert multiply(42, 0) == 0


def test_divide_evenly():
    assert divide(20, 5) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power_positive():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1