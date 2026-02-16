"""Unit tests for format utilities."""

import datetime
from utils.format import format_date, format_currency


def test_format_date_with_date():
    """Test format_date with a date object."""
    result = format_date(datetime.date(2026, 2, 16))
    assert result == 'February 16, 2026'


def test_format_date_with_datetime():
    """Test format_date with a datetime object."""
    result = format_date(datetime.datetime(2023, 12, 25, 10, 30))
    assert result == 'December 25, 2023'


def test_format_currency_usd():
    """Test format_currency with USD (default)."""
    result = format_currency(1234.56)
    assert result == '$1,234.56'


def test_format_currency_eur():
    """Test format_currency with EUR."""
    result = format_currency(1234.56, 'EUR')
    assert result == '€1,234.56'


def test_format_currency_zero():
    """Test format_currency with zero amount."""
    result = format_currency(0)
    assert result == '$0.00'


def test_format_currency_negative():
    """Test format_currency with negative amount."""
    result = format_currency(-99.99)
    assert result == '-$99.99'


def test_format_currency_large():
    """Test format_currency with large amount."""
    result = format_currency(1000000)
    assert result == '$1,000,000.00'


def test_format_date_day_ten():
    """Test that day '10' doesn't get corrupted."""
    result = format_date(datetime.date(2025, 3, 10))
    assert result == 'March 10, 2025'


def test_format_date_day_twenty():
    """Test that day '20' doesn't get corrupted."""
    result = format_date(datetime.date(2025, 4, 20))
    assert result == 'April 20, 2025'


def test_format_date_day_thirty():
    """Test that day '30' doesn't get corrupted."""
    result = format_date(datetime.date(2025, 5, 30))
    assert result == 'May 30, 2025'


def test_format_date_year_with_zero():
    """Test year ending in zero."""
    result = format_date(datetime.date(2020, 5, 5))
    assert result == 'May 5, 2020'


def test_format_date_year_2000():
    """Test year 2000 with multiple zeros."""
    result = format_date(datetime.date(2000, 1, 1))
    assert result == 'January 1, 2000'


def test_format_date_with_leading_zero_day():
    """Test date with leading zero in day (should be stripped)."""
    result = format_date(datetime.date(2026, 10, 1))
    assert result == 'October 1, 2026'


def test_format_date_none_input():
    """Test format_date with None raises ValueError."""
    import pytest
    with pytest.raises(ValueError, match="Date cannot be None"):
        format_date(None)


def test_format_date_invalid_input():
    """Test format_date with invalid input raises AttributeError."""
    import pytest
    with pytest.raises(AttributeError):
        format_date("2026-02-16")


def test_format_currency_invalid_input():
    """Test format_currency with invalid input raises ValueError."""
    import pytest
    with pytest.raises(ValueError, match="Amount must be a number"):
        format_currency("not a number")


def test_format_currency_none_input():
    """Test format_currency with None raises ValueError."""
    import pytest
    with pytest.raises(ValueError, match="Amount must be a number"):
        format_currency(None)
