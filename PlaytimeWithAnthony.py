
class Person:
    # def __getattribute__(self, name):
    #     """ Happens when Person('me').name """
    #     print(f"Now getting attr={name}")

    # def __getitem__(self, item_name: str):
    #     """ Happens when Person('me')['name']"""
    #     print(f'Now getting {item_name}')

    def __init__(self, name, age=100):
        """ Constructor"""
        self.name = name
        self.age = age

    def __eq__(self, other: 'Person'):
        """ Called when u do:

        Person('anthony') == Person('nolan')
        """
        return self.name == other.name

me = Person('anthony')
me.name  # call to getattribute
# me['name']  # call to getitem

# me.a_new_attribute  # this fails
me.a_new_attribute = 15

# getattr(object, attribute_name: str)
# setattr(object, attribute_name: str, attribute_value)
# Option A:
# imagine this came dynamically based on a web request
wanted_attributes = ('name', 'age')
for attribute in wanted_attributes:
    value = getattr(me, attribute)
    print(f"{value=}")

# also could do this:
# Option B:
value = me.name
value = me.age

# You want to get all the attributes that start with a
for attr in dir(me):
    value = getattr(me, attr)
    print(f"attr={value}")

another_me = Person('anthony')
# print(another_me['this_doesnt_exist?...'])

print('All methods of Person')
print(dir(me))

nolan = Person('nolan')

print(me == nolan)  # false
print(me == another_me) # true
print(me is another_me)  # false, 2 separate memory locations

print(f"{id(me)=} {id(another_me)=}")

first, second, *third = [1, 2, 3, 4, 5]
first == 1
second == 2
third = [3, 4, 5]


my_number = 15
print(f"The variable's value is: {my_number=}")

import time
import functools
from datetime import datetime

def timer(func):
    """ This is a decorator"""
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        # Behavior before function
        start = datetime.now()

        return_value = func(*args, **kwargs)

        # try:
        #     return_value = func(*args, **kwargs)
        # except KeyError as e:
        #     print(f"Exception! {str(e)}")
        #     return_value = 'wtf?...'

        # Behavior after function
        end = datetime.now()
        print(f"{func.__name__} took {end - start}")
        return return_value
    return wrapper_func

@timer
def say_hello(name) -> None:
    # time.sleep(5)
    print(f"Hello, {name}")

say_hello('Anthony')
# >>> 'say_hello took 5 seconds'


# Python things:
# decorators
# context managers
# generators

# for Nolan TODO:
# multiprocessing / multithreading / asyncio
# file IO

class TimeBlock:
    def __init__(self, msg: str):
        self.msg = msg

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self):
        took = (datetime.now() - self.start).seconds
        print(f"...took {took} seconds!")

# class open:
#     def __init__(self, filename: str):
#         self.filename = filename

#     def __enter__(self):
#         os.open_file(self.filename)

#     def __exit__(self):
#         os.close_file(self.filename)

# with open('myfile.txt') as f:
#     txt = f.read()