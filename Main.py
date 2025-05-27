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


# TODO: bytes (all types), classes, etc.

def main():
    print("Printing variables")

    # python numeric types
    print("varInt")
    print("{}, type = {}\n".format(varInt, type(varInt)))

    print("varFloat")
    print("{}, type = {}\n".format(varFloat, type(varFloat)))

    print("varComplex")
    print("{}, type = {}\n".format(varComplex, type(varComplex)))

    # python string type
    print("varString")
    print("{}, type = {}\n".format(varString, type(varString)))

    # python types for sequences of data (lists, tuples, ranges)
    print("varList")
    print("{}, type = {}".format(varList, type(varList)))
    print("List items are: ordered, changeable, and allow duplicate values.\n"
    "List items are indexed, the first item has index [0], the second item has index [1] etc.\n")

    print("varTuple")
    print("{}, type = {}".format(varTuple, type(varTuple)))
    print("Tuple items are ordered and unchangeable.\n")

    print("varRange")
    print("{}, type = {}\n".format(varRange, type(varRange)))

    # python mapping type (dictionaries)
    print("varDict")
    print("{}, type = {}".format(varDict, type(varDict)))
    print("Dictionary items are ordered*, changeable, and do not allow duplicates.\n"
    "* Note: As of Python version 3.7, dictionaries are ordered.\n")

    # python set types (sets, frozensets)
    print("varSet")
    print("{}, type = {}".format(varSet, type(varSet)))
    print("Set items are unordered, unchangeable*, and unindexed.\n"
    "* Note: Set items are unchangeable, but you can remove items and add new items.\n")

    print("varFrozenset")
    print("{}, type = {}".format(varFrozenset, type(varFrozenset)))
    print("Frozenset items are unordered, unchangeable, and unindexed.\n")

    # python bool type
    print("varBool")
    print("{}, type = {}\n".format(varBool, type(varBool)))

    # python binary types (bytes, bytearray, memoryview)
    print("varBytes")
    print("{}, type = {}\n".format(varBytes, type(varBytes)))

    print("varBytearray")
    print("{}, type = {}\n".format(varBytearray, type(varBytearray)))

    print("varMemoryview")
    print("{}, type = {}\n".format(varMemoryview, type(varMemoryview)))

if __name__ == "__main__":
    main()