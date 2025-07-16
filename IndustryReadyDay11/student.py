class student:
    def __init__(self,name,grade):
        self.__name=name
        self.__grade=grade
    def print(self):
        print(f"Name: {self.__name} , grade {self.__grade}")
    def set_grade(self,grade):
        self.__grade=grade
std=student("John", "A")
std.set_grade("B")
std.print()