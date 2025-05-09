import pytest

from source.date_validator import MyDate


def test_valid_date():
    d0 = MyDate()
    assert d0.dateInput == "2023-10-01"

    d1 = MyDate(dateInput="2020-01-01")
    assert d1.dateInput == "2020-01-01"


def test_invalid_date():
    with pytest.raises(ValueError) as e:
        MyDate(dateInput="1919-01-01")
    assert "Year out of range: 1919-01-01" in str(e.value)

    with pytest.raises(ValueError) as e:
        MyDate(dateInput="cica")
    text = "Value error, time data 'cica' does not match format '%Y-%m-%d'"
    assert text in str(e.value)
