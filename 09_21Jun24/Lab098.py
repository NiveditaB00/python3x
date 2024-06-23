"""
def my_decorator1(func):
    def wrapper():
        print("decorator1")
        func()
    return wrapper()


def my_decorator2(func):
    def wrapper():
        print("decorator2")
        func()
    return wrapper()

@my_decorator1
@my_decorator2
def say_hello():
    print("say Hello ")


say_hello()
"""

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
