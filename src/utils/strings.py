"""String utility functions for text manipulation."""


def reverse_string(s):
    """Reverse a string.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string
    """
    reversed_s = s[::-1]
    return reversed_s


def capitalize_words(s):
    """Capitalize the first letter of each word in a string.

    Args:
        s (str): The string to capitalize

    Returns:
        str: String with each word capitalized
    """
    words = s.split()
    capitalized = [word.capitalize() for word in words]
    result = ' '.join(capitalized)
    return result


def count_vowels(s):
    """Count the occurrence of each vowel in a string.

    Args:
        s (str): The string to analyze

    Returns:
        dict: Dictionary with vowel counts (keys: 'a', 'e', 'i', 'o', 'u')
    """
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    lowercase_s = s.lower()
    for char in lowercase_s:
        if char in vowel_counts:
            vowel_counts[char] += 1
    return vowel_counts
