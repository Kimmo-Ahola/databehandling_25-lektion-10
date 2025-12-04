from string_utils import StringUtils
import pytest

"""
input: kimmo
result: Kimmo

input: KIMMO
result: Kimmo
"""


def test_capitalize():
    # Arrange
    input_string = "kimmo"
    # Act
    result = StringUtils.capitalize(input_string)
    # Assert
    assert result == "Kimmo"


def test_capitalize_1():
    input_string = ""

    result = StringUtils.capitalize(input_string)

    assert result == ""


def test_capitalize_2():
    # Arrange
    input_string = "kimmo ahola"
    # Act
    result = StringUtils.capitalize(input_string)
    # Assert
    assert result == "Kimmo Ahola"


def test_capitalize_3():
    # Arrange
    input_string = "kimmo kristian ahola"
    # Act
    result = StringUtils.capitalize(input_string)
    # Assert
    assert result == "Kimmo Kristian Ahola"


def test_capitalize_4():
    # Arrange
    input_string = "kimmo kRISTIAN ahola"
    # Act
    result = StringUtils.capitalize(input_string)
    # Assert
    assert result == "Kimmo Kristian Ahola"


def test_capitalize_5():
    # Arrange
    input_string = "131245"
    # Act
    result = StringUtils.capitalize(input_string)
    # Assert
    assert result == "131245"


@pytest.mark.parametrize(
    "input, expected", [("test", "Test"), ("first second", "First Second")]
)
def test_capitalize_all(input: str, expected: bool):
    result = StringUtils.capitalize(input)

    assert result == expected
