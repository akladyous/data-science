class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point {self.x} {self.y}"

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def calc(self):
        pass


p1 = Point(1, 2)
p2 = Point(1, 2)
print(f"p1 == p2 : {p1 == p2}\n")


def func1(lst: list[int] = []):
    lst.append(0)
    return lst


result1 = func1()
result2 = func1()

print(result1, result2)


def func2(n: int = 0):
    n += 1
    return n


result3 = func2()
result4 = func2()
print(result3, result4)


def func3():
    inner_var = None
    return inner_var


func3()


def my_function(a=None):
    print("Hello, world!")


my_function.custom_attribute = "Custom Value"


print(hasattr(my_function, "__dict__"))  # Output: False


print(p1.__dict__)
print(my_function.__dict__)
print(my_function.__class__)
p1.attr1 = 123

print(p1.__dict__)
print(p1.__class__)
print(my_function.__code__.co_consts)
print(my_function.__code__.co_varnames)


print(dir())
# print("lst" in dir())
