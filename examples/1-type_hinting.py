# First Example
def add(a: int, b: int) -> int:
    return a + b


# Second Example
def process_data(data: dict) -> list:
    return list(data.values())

# Third Example


def add_numbers(a: int, b: int, c: int | None = 0) -> int:
    return a + b + c

# Fourth Example


class MyClass:
    def __init__(self, value: int | None = None):
        self.value = value


def print_value(obj: MyClass) -> None:
    print(obj.value)


if __name__ == "__main__":
    # print(add(1, 2))
    # # print(add(1, '2'))  # This will raise a TypeError
    # print(process_data({1: 'one', 2: 'two'}))
    print(add_numbers(1, 2, 3))
    # print(add_numbers(1, 2, None))
    # print(add_numbers(1, 2, '3'))
    # obj = MyClass(10)
    # print_value(obj)
