import pytest
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from example_package_fatemacz.example import sum_all


def test_sum_all_no_args():
    assert sum_all() == 0


def test_sum_all_single_arg():
    assert sum_all(5) == 5


def test_sum_all_multiple_args():
    assert sum_all(1, 2, 3, 4) == 10


def test_sum_all_negative_args():
    assert sum_all(-1, -2, -3, -4) == -10


def test_sum_all_mixed_args():
    assert sum_all(1, -2, 3, -4) == -2


def test_sum_all_large_numbers():
    assert sum_all(1000000, 2000000, 3000000) == 6000000


if __name__ == "__main__":
    pytest.main()
