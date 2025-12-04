import pytest
from arithmetic import Arithmetic


@pytest.fixture
def setup() -> Arithmetic:
    return Arithmetic()


def test_addition(setup: Arithmetic):
    # Arrange = vi förbereder
    first = 1
    second = 2
    # Act = vi kallar på funktionen
    result = setup.add(first, second)
    # Assert = vi kontrollerar resultatet
    assert result == 3


def test_addition_float(setup: Arithmetic):
    # Arrange = vi förbereder
    first = 0.1
    second = 0.2
    # Act = vi kallar på funktionen
    result = setup.add_float(first, second)
    # Assert = vi kontrollerar resultatet
    assert result == pytest.approx(0.3)


def test_division(setup: Arithmetic):
    first = 1
    second = 0

    result = setup.divide(first, second)

    assert result == None
