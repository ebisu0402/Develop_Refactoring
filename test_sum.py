# test_sum.py
import pytest
from sum import sum  # sum関数が定義されているモジュールをインポート


def test_sum_positive_numbers():
    assert sum(3, 4) == 7  # 3 + 4 = 7 であることを確認


def test_sum_negative_numbers():
    assert sum(-1, -1) == -2  # -1 + -1 = -2 であることを確認


def test_sum_mixed_numbers():
    assert sum(5, -3) == 2  # 5 + (-3) = 2 であることを確認


def test_sum_zero():
    assert sum(0, 0) == 0  # 0 + 0 = 0 であることを確認


def test_sum_large_numbers():
    assert (
        sum(1000000, 5000000) == 6000000
    )  # 1000000 + 5000000 = 6000000 であることを確認
