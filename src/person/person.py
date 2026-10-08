"""Simple Person model."""


class Person:
    def __init__(self, name: str, age: int) -> None:
        if age < 0:
            raise ValueError("age must be non-negative")
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name}"

    def is_adult(self) -> bool:
        return self.age >= 18
