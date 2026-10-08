import pytest

from person.person import Person


def test_greet():
    p = Person("Alice", 20)
    assert p.greet() == "Hello, my name is Alice"


def test_is_adult():
    assert Person("Bob", 18).is_adult() is True
    assert Person("Kid", 10).is_adult() is False


def test_negative_age():
    with pytest.raises(ValueError):
        Person("X", -1)
