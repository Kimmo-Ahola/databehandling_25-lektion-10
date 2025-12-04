import pytest
from arithmetic import Arithmetic


# When using object we need to create new object before every test
# fixture does that for us.
# Before every test in this class, if the test has setup as a parameter
# We call on fixture
# A new object = no shared state between tests
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

    # För flyttal måste vi använda oss av approximering för att det ska gå att jämföra
    # pytest.approx löser detta åt oss
    assert result == pytest.approx(0.3)


def test_division(setup: Arithmetic):
    first = 1
    second = 0

    result = setup.divide(first, second)

    # Hur ska vi hantera division med 0?
    # Jag väljer att skicka tillbaka None som resultat i min metod
    assert result == None
