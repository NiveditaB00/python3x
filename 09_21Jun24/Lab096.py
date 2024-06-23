#Decorators
#what is Decorators
#it is the function it takes anoter function as argument
# and returns a new function by extending its behaviour

def my_decorator(func):
    def wrapper():
        print("Staring your function")
        print(".............")
        func()
        print(".............")
        print("Finished your function")
    return wrapper()


@my_decorator
def say_hello():
    print("say Hello ")


#say_hello()
"""

def my_decorator(func):
    def wrapper():
        print("Starting.....")
        print("****************")
        func()
        print("****************")
        print("Ending")

    return wrapper()


@my_decorator
def say_hello():
    print("Say Hello")
    """