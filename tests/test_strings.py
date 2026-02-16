"""Tests for string utility functions."""

import pytest
from src.utils.strings import reverse_string, capitalize_words, count_vowels


class TestReverseString:
    """Test cases for reverse_string function."""

    def test_reverse_normal_string(self):
        """Test reversing a normal string."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        assert reverse_string("") == ""


class TestCapitalizeWords:
    """Test cases for capitalize_words function."""

    def test_capitalize_multi_word_string(self):
        """Test capitalizing multiple words."""
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python is awesome") == "Python Is Awesome"

    def test_capitalize_single_word(self):
        """Test capitalizing a single word."""
        assert capitalize_words("hello") == "Hello"
        assert capitalize_words("python") == "Python"


class TestCountVowels:
    """Test cases for count_vowels function."""

    def test_count_vowels_mixed(self):
        """Test counting vowels in a string with mixed vowels."""
        result = count_vowels("hello")
        assert result == {'a': 0, 'e': 1, 'i': 0, 'o': 1, 'u': 0}

        result = count_vowels("beautiful")
        assert result == {'a': 1, 'e': 1, 'i': 1, 'o': 0, 'u': 2}

    def test_count_vowels_no_vowels(self):
        """Test counting vowels in a string with no vowels."""
        result = count_vowels("xyz")
        assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        result = count_vowels("bcdfg")
        assert result == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
