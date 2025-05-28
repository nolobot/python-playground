

def MyMethod(statement: str = "No statement was given") -> None:
    print("This is your module's method, here's the statement: {}".format(statement))

class MyClass:
    def __init__(self):
        print("this is the constructor of MyClass")