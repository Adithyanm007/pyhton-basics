def decorator(func):
    def wrapper():
        print("Before running function")
        func()
        print("After running function")
    return wrapper
@decorator
def say_hello():
    print("Hello, World!")
say_hello()