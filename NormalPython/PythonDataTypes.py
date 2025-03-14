# Python Data Types

# Numeric Types
integer_value = 10
float_value = 10.5
complex_value = 1 + 2j

# Sequence Types
string_value = "Hello, World!"
list_value = [1, 2, 3, 4, 5]
tuple_value = (1, 2, 3, 4, 5)

# Mapping Type
dict_value = {"name": "John", "age": 30}

# Set Types
set_value = {1, 2, 3, 4, 5}
frozenset_value = frozenset([1, 2, 3, 4, 5])

# Boolean Type
bool_value = True

# Binary Types
bytes_value = b"Hello"
bytearray_value = bytearray(5)
memoryview_value = memoryview(bytes(5))

# None Type
none_value = None

# Displaying the types
print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(string_value))
print(type(list_value))
print(type(tuple_value))
print(type(dict_value))
print(type(set_value))
print(type(frozenset_value))
print(type(bool_value))
print(type(bytes_value))
print(type(bytearray_value))
print(type(memoryview_value))
print(type(none_value))

import random


# Generate random number from 1 to 100
print("Random number from 1 to 100 is " + str(random.randrange(1, 101)))


#type conversion in python
#int to float
x = 1
print(float(x))
b=1.0
print(int(b))
c=1.0
print(str(c))
