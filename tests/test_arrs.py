from utils import arrs
import pytest as pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_get_empty_array():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], -3, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -7, 3) == [1, 2, 3]
