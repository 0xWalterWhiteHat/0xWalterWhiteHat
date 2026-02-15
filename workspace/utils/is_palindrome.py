"""Palindrome checker utility."""

import string


def is_palindrome(s):
    """Check if a string is a palindrome.

    Removes all whitespace characters and punctuation, then performs
    a case-insensitive comparison.

    Args:
        s: The string to check. Must be a string type.

    Returns:
        True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If s is not a string type.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected string, got {type(s).__name__}")

    cleaned = s.lower().translate(str.maketrans("", "", string.whitespace + string.punctuation))
    return cleaned == cleaned[::-1]
