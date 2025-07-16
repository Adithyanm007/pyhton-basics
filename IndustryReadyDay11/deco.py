def My_deco(func):
    def wrapper():
        print("************")
        func()
        print("************")
    return wrapper
@My_deco
def greet():
    print("Welcome , adi")
greet()
