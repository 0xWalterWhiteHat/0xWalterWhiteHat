"""Tests for math helper utilities."""
import pytest
from src.utils.math_helpers import fibonacci, is_prime, factorial


class TestFibonacci:
    """Test cases for fibonacci function."""

    def test_fibonacci_zero(self):
        """Test that fibonacci(0) returns 0."""
        assert fibonacci(0) == 0

    def test_fibonacci_tenth(self):
        """Test that fibonacci(10) returns 55."""
        assert fibonacci(10) == 55

    def test_fibonacci_one(self):
        """Test that fibonacci(1) returns 1."""
        assert fibonacci(1) == 1

    def test_fibonacci_negative(self):
        """Test that fibonacci handles negative numbers."""
        assert fibonacci(-5) == 0


class TestIsPrime:
    """Test cases for is_prime function."""

    def test_is_prime_seventeen(self):
        """Test that 17 is correctly identified as prime."""
        assert is_prime(17) is True

    def test_is_prime_four(self):
        """Test that 4 is correctly identified as not prime."""
        assert is_prime(4) is False

    def test_is_prime_one(self):
        """Test that 1 is correctly identified as not prime."""
        assert is_prime(1) is False

    def test_is_prime_two(self):
        """Test that 2 is correctly identified as prime."""
        assert is_prime(2) is True

    def test_is_prime_negative(self):
        """Test that negative numbers are not prime."""
        assert is_prime(-7) is False


class TestFactorial:
    """Test cases for factorial function."""

    def test_factorial_five(self):
        """Test that factorial(5) returns 120."""
        assert factorial(5) == 120

    def test_factorial_zero(self):
        """Test that factorial(0) returns 1."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test that factorial(1) returns 1."""
        assert factorial(1) == 1

    def test_factorial_negative(self):
        """Test that factorial raises ValueError for negative numbers."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
