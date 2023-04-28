from utils import arrs
import pytest as pytest

@pytest.fixture
def array_fixture():
    return [1, 2, 3]

@pytest.fixture
def coll_fixture():
    return [1, 2, 3, 4]


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get(array_fixture, -1, "test") == "test"


def test_get_empty_array():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test") == "test"


def test_slice(coll_fixture):
    assert arrs.my_slice(coll_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(coll_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(coll_fixture, -3, 3) == [2, 3]
    assert arrs.my_slice(coll_fixture, -7, 3) == [1, 2, 3]


def test_slice_empty_coll():
    assert arrs.my_slice([], 1, 3) == []