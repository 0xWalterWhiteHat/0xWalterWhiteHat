"""Unit tests for helpers.math_utils module."""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from helpers.math_utils import factorial, fibonacci


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_large():
    assert factorial(20) == 2432902008176640000


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_positive():
    assert fibonacci(10) == 55
    assert fibonacci(6) == 8


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_large():
    assert fibonacci(30) == 832040
