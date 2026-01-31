"""
Python Numbers
There are three numeric types in Python:

int
float
complex
"""

# Int

i_typ0 = 12345678909876  # int positive value
i_typ1 = -3355870  # int negative value
print("positive numbers = ", i_typ0)
print("Negative numbers = ", i_typ1)

print(type(i_typ0))
print(type(i_typ1))

# Float

f_typ0 = 1.0
f_typ1 = -35.79
f_typ2 = 12e4
f_typ3 = 35e93

print("value = ", f_typ0, " : type = ", type(f_typ0))
print("value = ", f_typ1, " : type = ", type(f_typ1))
print("value = ", f_typ2, " : type = ", type(f_typ2))
print("value = ", f_typ3, " : type = ", type(f_typ3))

# complex

c_typ0 = 1j
c_typ1 = 3 + 5j
c_typ2 = -5j
print(type(c_typ0))
print("value = ", c_typ0, " : type = ", type(c_typ0))
print("value = ", c_typ1, " : type = ", type(c_typ1))
print("value = ", c_typ2, " : type = ", type(c_typ2))

# Casting
# return int

return_int_val0 = int(1.0)  # return int value = 1
return_int_val1 = int(3.50)  # return int value = 3
return_int_val2 = int("5")  # return int value = 5
return_int_val3 = int(25e5)  # return int value = 2500000

print(return_int_val0)
print(return_int_val1)
print(return_int_val2)
print(return_int_val3)

return_float_val0 = float(1)  # return float  1.0
return_float_val1 = float("2.8")  # return float 2.8
return_float_val2 = float(-5)  # return float -5.0
return_float_val3 = float("3")  # return float 3.0

print(return_float_val0)
print(return_float_val1)
print(return_float_val2)
print(return_float_val3)

# return str
print("'" + str(1) + "'")  # return str '1'
print(str(2.5))  # return str 2.5
print(type(str(1)))
print(type(str(2.5)))

# string: string is a list as each letter / char is a string.
# string is an array and list. List represent an array

s0_ver = "Hello, World!"
print(len(s0_ver))

print (list(s0_ver))
for x in "Hello, World!":
  print(x)
   

s_ver = "python"

s2 = list(s_ver)
print(s2)

# string: Multiline comments and Multiline string value using 3 double quote
"""
This is a comment
written in
more than just one line

"""
# Multiline Strings
# You can assign a multiline string to a variable by using three (3) """ double quotes:
# You can use three double quotes:

multiline_str_3dbl_quotes = """ ("I can assign multiline string text values
                             into a single variable with using three double
                             quotes. It hold string data type. This string variable 
                             useful when multiline error message validation require
                             for the negative testing.")
                            """
print("multiline string values:   " + multiline_str_3dbl_quotes)
print(type(multiline_str_3dbl_quotes))

import array as arr

myArray = arr.array("i", [1, 2, 3, 4, 5, 6])
print(myArray)
print(type(myArray))

ar = [1, 2, 3]
imp = arr.array("i", ar)
print(imp)
for i in range(0, 3):
    print(imp[i], end=" ")
# float
import array
myArr=array.array('f', [1.0, 2.5, 3.7])
print(myArr)

a = arr.array('f', [1, 2, 3])
print(list(a))
print(a)
for i in range(0, 3):
    print(a[i], end=" ")
print('             ')
print("new output starting from here ")
for f in range(0, 3): print(a[f])

for f in range(0, 3):
    print(a[f], '\n')

