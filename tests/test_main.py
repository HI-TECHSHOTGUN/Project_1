from src.main import divide, calculate_logarithm, reverse_string
import pytest

def test_divide():
    assert  divide(2, 1 ) == 2

    assert divide(2, 0) == 0


def test_calc_log():
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5

    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)

    with pytest.raises(ValueError):
        calculate_logarithm(8, 0)

def test_revers_str_numbers(numbers):
    assert reverse_string('123') =='321'

def test_revers_str_letters(letters):
    assert reverse_string('hello') == 'olleh'