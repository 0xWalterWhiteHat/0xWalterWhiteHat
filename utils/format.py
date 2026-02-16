"""Formatting utilities for dates and currency."""


def format_date(d):
    """Format a date or datetime object as a human-readable string.

    Args:
        d: A datetime.date or datetime.datetime object

    Returns:
        A string in the format 'Month Day, Year' (e.g., 'February 16, 2026')

    Raises:
        AttributeError: If d is not a date/datetime object
    """
    if d is None:
        raise ValueError("Date cannot be None")

    # Cross-platform solution: build the string manually to avoid leading zeros
    day = d.day
    month = d.strftime('%B')
    year = d.year
    return f'{month} {day}, {year}'


def format_currency(amount, currency='USD'):
    """Format a number as a currency string.

    Args:
        amount: A numeric value to format
        currency: Currency code ('USD', 'EUR', 'GBP', or other)

    Returns:
        A formatted currency string with symbol/code, thousands separators,
        and 2 decimal places (e.g., '$1,234.56' or '-€99.99')

    Raises:
        TypeError: If amount is not a number
        ValueError: If amount cannot be converted to float
    """
    # Validate input
    try:
        amount = float(amount)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Amount must be a number, got {type(amount).__name__}") from e

    # Get currency symbol
    if currency == 'USD':
        symbol = '$'
    elif currency == 'EUR':
        symbol = '€'
    elif currency == 'GBP':
        symbol = '£'
    else:
        symbol = currency

    # Format the absolute value with commas and 2 decimal places
    formatted_amount = '{:,.2f}'.format(abs(amount))

    # Add symbol and handle negative amounts
    if amount < 0:
        return f'-{symbol}{formatted_amount}'
    else:
        return f'{symbol}{formatted_amount}'
