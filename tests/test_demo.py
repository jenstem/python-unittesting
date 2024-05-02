import pytest
from app.demo import add, subtract, multiply, divide


def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(20, 10) == 10

def test_multiply():
    assert multiply(10, 2) == 20

def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(10, 0)