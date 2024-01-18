class Person:
    first_name: str
    last_name: str

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


print(repr(Person()))
