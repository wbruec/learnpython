def f(**kwargs: str):
    """This is my docstring yooooooooooooooooooooooooooooo"""
    for key, val in kwargs.items():
        print(f"k is {key} and v is {val}")
    return

print(f.__annotations__)
#f(key1 = "value1", key2 = "val2")