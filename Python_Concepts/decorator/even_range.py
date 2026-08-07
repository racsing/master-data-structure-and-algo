"""Example showing how decorators can modify function behavior.

The even_range decorator accepts a range and ensures the wrapped function
is called only for even numbers inside that range.
"""

import math

def even_range(x, y):
    """Return a decorator that calls the wrapped function for even values."""

    def decorator(func):
        """Wrap the target function with custom range-based behavior."""

        def wrapper():
            """Execute the function once for each even number in the range."""
            for num in range(x, y + 1):
                if num % 2 == 0:
                    func(num)
        return wrapper

    return decorator


@even_range(1, 10)
def square_root(n) -> float:
    """Print and return the square root of a given number."""
    ans = math.sqrt(n)
    print(f"sq root of {n} is {ans}")
    return ans


if __name__ == "__main__":
    square_root()