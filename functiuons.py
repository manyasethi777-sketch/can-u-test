from typing import Iterable


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def is_even(number: int) -> bool:
    """Return True when number is even."""
    return number % 2 == 0


def safe_divide(a: float, b: float) -> float | None:
    """Divide a by b; return None when b is zero."""
    if b == 0:
        return None
    return a / b


def largest_number(numbers: list[int]) -> int | None:
    """Return the largest number, or None for an empty list."""
    if not numbers:
        return None
    return max(numbers)


def count_occurrences(items: list[str], target: str) -> int:
    """Count exact, case-sensitive occurrences of target."""
    return sum(1 for item in items if item == target)


def normalize_username(username: str) -> str:
    """Strip surrounding whitespace and lowercase a username."""
    return username.strip().lower()


def is_palindrome(text: str) -> bool:
    """Return whether text is a palindrome, ignoring spaces and letter case."""
    cleaned = "".join(character.lower() for character in text if not character.isspace())
    return cleaned == cleaned[::-1]


def second_largest_unique(numbers: Iterable[int]) -> int | None:
    """
    Return the second-largest DISTINCT value.
    Return None if fewer than two distinct values exist.
    """
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]


def is_leap_year(year: int) -> bool:
    """Gregorian leap year: divisible by 4, except centuries unless divisible by 400."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def calculate_discount(price: float, percent: float) -> float:
    """
    Apply a percentage discount. Price must be >= 0 and percent must be 0..100.
    Raise ValueError for invalid inputs.
    """
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def merge_sorted_lists(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists, preserving duplicates; either list may be empty."""
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def average(numbers: list[float]) -> float | None:
    """Return the arithmetic mean, or None for an empty list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)