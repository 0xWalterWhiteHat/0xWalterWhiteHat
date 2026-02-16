def factorial(n):
    """Return the factorial of n.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError(f"factorial() not defined for negative values, got {n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """Return the nth Fibonacci number.

    fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).

    Args:
        n: A non-negative integer index.

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError(f"fibonacci() not defined for negative values, got {n}")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
