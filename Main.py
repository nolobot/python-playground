import MyModule

# python numeric types
varInt = 5
varFloat = 5.0
varComplex = 5.0 + 5j

# python string type
varString = "my string"

# python types for sequences of data (lists, tuples, ranges)
varList = [15, 36, 42]
varTuple = (15, 20, 30)
varRange = range(10)

# python mapping type (dictionaries)
varDict = {"key1": 12, "key2": "value2"}

# python set types (sets, frozensets)
varSet = {5, 10, 12, 18}
varFrozenset = frozenset(varSet)

# python bool type
varBool = True

# python binary types (bytes, bytearray, memoryview)
varBytes = b"\x00\x01\x02\x03"
varBytearray = bytearray(b"\x00\x01\x02\x03")
varMemoryview = memoryview(b"\x00\x01\x02\x03")

# TODO: modules, classes

# Python things:
# decorators
# context managers
# generators

# for Nolan TODO:
# multiprocessing / multithreading / asyncio
# file IO

def main():
    print("Printing variables")

    # python numeric types
    print("varInt")
    print(f"{varInt}, type = {type(varInt)}\n")

    print("varFloat")
    print(f"{varFloat}, type = {type(varFloat)}\n")

    print("varComplex")
    print(f"{varComplex}, type = {type(varComplex)}\n")

    # python string type
    print("varString")
    print(f"{varString}, type = {type(varString)}\n")

    # python types for sequences of data (lists, tuples, ranges)
    print("varList")
    print(f"{varList}, type = {type(varList)}")
    print("List items are: ordered, changeable, and allow duplicate values.\n"
    "List items are indexed, the first item has index [0], the second item has index [1] etc.\n")

    print("varTuple")
    print(f"{varTuple}, type = {type(varTuple)}")
    print("Tuple items are ordered and unchangeable.\n")

    print("varRange")
    print(f"{varRange}, type = {type(varRange)}\n")

    # python mapping type (dictionaries)
    print("varDict")
    print(f"{varDict}, type = {type(varDict)}")
    print("Dictionary items are ordered*, changeable, and do not allow duplicates.\n"
    "* Note: As of Python version 3.7, dictionaries are ordered.\n")

    # python set types (sets, frozensets)
    print("varSet")
    print(f"{varSet}, type = {type(varSet)}")
    print("Set items are unordered, unchangeable*, and unindexed.\n"
    "* Note: Set items are unchangeable, but you can remove items and add new items.\n")

    print("varFrozenset")
    print(f"{varFrozenset}, type = {type(varFrozenset)}")
    print("Frozenset items are unordered, unchangeable, and unindexed.\n")

    # python bool type
    print("varBool")
    print(f"{varBool}, type = {type(varBool)}\n")

    # python binary types (bytes, bytearray, memoryview)
    print("varBytes")
    print(f"{varBytes}, type = {type(varBytes)}\n")

    print("varBytearray")
    print(f"{varBytearray}, type = {type(varBytearray)}\n")

    print("varMemoryview")
    print(f"{varMemoryview}, type = {type(varMemoryview)}\n")

    print(MyModule)
    # print(MyModule.__dict__)
    print(MyModule.MyMethod())
    # MyModule.MyMethod()

    print("")

    # string handling
    myString = "this is my string"
    print(f"myString's first character = {myString[0]}")
    print(f"myString's 6 thru end characters = {myString[5:]}")

    # this is an object of your MyModule's class, MyClass
    myObject = MyModule.MyClass()
    print(myObject)

    # this is a for loop in Python
    for character in myString:
        print(character)

    fileName = "some-text-file.txt"

    textFile = open(fileName, "r")
    print("Closing textFile now")
    textFile.close()

    print("Using with statement to open {fileName} it now")
    with open(fileName, "r") as withOpenedTextFile:
        print(f"This is the first line of {fileName} with the newline character stripped: {withOpenedTextFile.readline()[:-1]}")

    print("Now we'll do some try/except stuff!")

    try:
        print("This is in the try block")
        print(f"{undefinedVariable}")
    except:
        print("Woops, hit an exception")
    finally:
        print("This is occurring because it it's in the finally block of the try/except")

    print()

    try:
        print("This is in the try block")
    except:
        print("Woops, hit an exception, except this won't occur, you should only be reading this in the source code")
    else:
        print("Congratulations, your try block succeeded")
    finally:
        print("This is *still* occurring because it it's in the finally block of the try/except")


if __name__ == "__main__":
    main()