from solution import extract_calibration_value
import pytest


def test_simple_case():
    assert extract_calibration_value("1abc2") == 12

def test_digits_at_ends():
    assert extract_calibration_value("pqr3stu8vwx") == 38

def test_multiple_digits():
    assert extract_calibration_value("a1b2c3d4e5f") == 15

def test_single_digit():
    assert extract_calibration_value("treb7uchet") == 77

def test_empty_string():
    with pytest.raises(ValueError):
        extract_calibration_value("")

def test_only_digits():
    assert extract_calibration_value("12345") == 15

def test_digits_in_middle():
    assert extract_calibration_value("abc123xyz") == 13

# You can run these tests using the command: pytest test_file_name.py