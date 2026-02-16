"""Date utility functions for common date operations."""

from datetime import datetime


def days_between(date1, date2):
    """
    Calculate the absolute number of days between two dates.

    Args:
        date1: First date (datetime.date or datetime.datetime)
        date2: Second date (datetime.date or datetime.datetime)

    Returns:
        int: Absolute number of days between the two dates
    """
    difference = date2 - date1
    return abs(difference.days)


def is_weekend(date):
    """
    Check if a date falls on Saturday or Sunday.

    Args:
        date: Date to check (datetime.date or datetime.datetime)

    Returns:
        bool: True if the date is a weekend (Saturday or Sunday), False otherwise
    """
    return date.weekday() >= 5


def format_date(date, fmt=None):
    """
    Format a date using strftime.

    Args:
        date: Date to format (datetime.date or datetime.datetime)
        fmt: Format string (optional, defaults to '%Y-%m-%d')

    Returns:
        str: Formatted date string
    """
    if fmt is None:
        fmt = '%Y-%m-%d'
    return date.strftime(fmt)
