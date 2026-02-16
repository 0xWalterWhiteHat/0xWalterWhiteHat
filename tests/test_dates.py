"""Tests for date utility functions."""

from datetime import datetime, date
from src.utils.dates import days_between, is_weekend, format_date


def test_days_between_different_dates():
    """Test days_between with two dates that are different."""
    date1 = date(2026, 1, 1)
    date2 = date(2026, 1, 10)
    assert days_between(date1, date2) == 9


def test_days_between_same_date():
    """Test days_between with the same date returns 0."""
    date1 = date(2026, 1, 1)
    date2 = date(2026, 1, 1)
    assert days_between(date1, date2) == 0


def test_days_between_reversed_order():
    """Test days_between returns absolute value regardless of order."""
    date1 = date(2026, 1, 10)
    date2 = date(2026, 1, 1)
    assert days_between(date1, date2) == 9


def test_is_weekend_saturday():
    """Test is_weekend returns True for Saturday."""
    saturday = date(2026, 2, 14)  # This is a Saturday
    assert is_weekend(saturday) is True


def test_is_weekend_sunday():
    """Test is_weekend returns True for Sunday."""
    sunday = date(2026, 2, 15)  # This is a Sunday
    assert is_weekend(sunday) is True


def test_is_weekend_weekday():
    """Test is_weekend returns False for a weekday."""
    monday = date(2026, 2, 16)  # This is a Monday
    assert is_weekend(monday) is False


def test_format_date_default():
    """Test format_date with default format."""
    test_date = date(2026, 2, 16)
    assert format_date(test_date) == '2026-02-16'


def test_format_date_custom_format():
    """Test format_date with custom format string."""
    test_date = date(2026, 2, 16)
    assert format_date(test_date, '%d/%m/%Y') == '16/02/2026'


def test_format_date_with_time():
    """Test format_date with datetime object and custom format."""
    test_datetime = datetime(2026, 2, 16, 14, 30, 0)
    assert format_date(test_datetime, '%Y-%m-%d %H:%M') == '2026-02-16 14:30'
