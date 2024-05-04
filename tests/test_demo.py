import pytest
from app.demo import add, subtract, multiply, divide, discount_season


@pytest.mark.skip("Not implemented yet")
def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(20, 10) == 10

@pytest.mark.skipif(discount_season(), reason="Not implemented yet")
def test_multiply():
    assert multiply(10, 2) == 20

def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(10, 0)