"""
Variables are containers for storing data values.
A variable is created the moment you first assign a value to it.
Python has no command for declaring a variable.
Variables do not need to be declared with any particular type,
and can even change type after they have been set.

"""

x = 5
y = 5 + 5

print(x)
print(y)
print(10 + 10)

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

a = 10  # # no type declared a contains int and changed string
print(a)
a = "John"  #  an overwrite a
print(a)
print(a)


# #uper case and lower case sensitivity
b = 5
B = "Cathy"  #  b and B are 2 different variables
print(b)
print(B)

# generate / get  the type using type() method

ver1 = 5.0
ver2 = 5
ver3 = "Car"
ver4 = "Honda"
is_ver5 = True
is_not_ver = False
print("ver1 = ", type(ver1))
print("ver2 = ", type(ver2))
print("ver3 = ", type(ver3))
print("ver4 = ", type(ver4))
print("is_ver5 = ", type(is_ver5))
print("is_not_ver = ", type(is_not_ver))


"""
print("ver1 = ",type(ver1), end=" ")
print("ver2 = ",type(ver2), end=" ")
print("ver3 = ",type(ver3), end=" ")
print("ver4 = ",type(ver4), end=" ")
print("is_ver5 = ",type(is_ver5), end=" ")
print("is_not_ver = ",type(is_not_ver))

"""

# Casting
# If you want to specify the data type of  variable, this can be done with casting.

s = str("Cathy")
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)
print(s, x, y, z)

# get the type

s1 = "1"
s2 = "3"
s3 = s1 + s2
num0 = 10
num1 = 20
fNum = num0 / num1
is_str = True

print(type(s1))
print(type(s2))
print(type(s3))

print(type(num0))
print(type(num1))
print(type(fNum))
print(type(is_str))

# Python allows you to assign values to multiple variables in one line:
"""
o = "Orange"
b = "Banana"
c = "Cherry"
"""
# make 3 var in one line

o, b, ch = "Orange", "Banana", "Cherry"
print(o)
print(b)
print(ch)

o1 = o2 = o3 = "Orange"
print(o1)
print(o2)
print(o3)

# List

fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print(f1)
print(f2)
print(f3)
#  List and String Concatenation: ,(coma) + (plus), Extend or Join
addFruits = ["orange", "grape"]
print(fruits)
print(addFruits)
# (+) concatenate for List
# OR Add list elements  Using the extend() method: output will be same

combined_list = fruits + addFruits
print(combined_list)
fruits.extend(addFruits)  # using extend method first list will go to print method
print(fruits)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
# using extend method

list1.extend(list2)
print(list1)

"""
 remove 3rd bracket and coma from output of a list using " ".join  method
"""
word_list1 = ["My", "name", "is", "Alice."]
word_list2 = ["I", "am", "30", "years", "old."]
add_word_list = word_list1 + word_list2
print(add_word_list)

# using extend method
word_list1.extend(word_list2)
print(word_list1)

# now implement " ".join method for the 2 word list to remove [] and coma
word1 = ["My", "name", "is", "Alice."]
word2 = ["I", "am", "30", "years", "old."]
sentence1 = " ".join(word1)
print(sentence1)
sentence2 = " ".join(word2)
print(sentence2)
add_sentences = sentence1 + sentence2
print(add_sentences)

"""
Using f-strings (Formatted String Literals): 
This provides a concise and readable way to 
embed expressions inside string literals.
Embedding variables in a string
"""
name = "Alice"
age = 35
message = f"[using f] = My name is {name} and I am {age} years old."
print(message)
# using .format()
format_message = "[using .format ] = My name is {} and I am {} years old.".format(name, age)
print(format_message)

price = 49.99
quantity = 3
print(f"Total cost: ${price * quantity:.2f}")


print("=====start from here ===== concatenate for string")


# coma (,) plus ( + ) concatenate for string
x = "1. "  # string
y = "John"  #  string
a = " 30"  #  string
print(x, y, a)
print(x + y + a)  # string + string + string

is_string = True
is_int = False
print(is_string + is_int)  # output: 1  means false
print(is_string, is_int)

str1 = "Python"
str2 = "is"
str3 = "awesome"
print(str1, str2, str3)  # Python is awesome
print(str1 + str2 + str3)  # Python+is+awesome
print(str1 + " " + str2 + " " + str3)  # Python is awesome

print("start here ====concepts of global and local variables =====")

"""
global variable:Variables that are created outside of a function 
are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
local variable: Variables that are created inside of a function 
are known as local variables.

"""
 # global variable
g_var = "awesome"

def myfunc():
  print("Python is " + g_var)       #  g_var global variable is using inside this function

myfunc()
print("Python is " + g_var)  #  g_var global variable is using outside this function

#If you create a variable with the same name (of global var) inside a function,
# this variable will be local, and can only be used inside the function.

# Create a variable inside a function, with the same name as the global variable
# x is a global variable
x = "awesome"

def myfun():                             #
  x1 = "fantastic"
  print("Python is " + x1)

myfun()
print("Python is " + x)

x = "nice"
print("Python is " + x)
def myfunc():
  global x
  x = "fantastic"
  print("local: Python is " + x)

myfunc()

print("global: Python is " + x)
greet = " "
def getfunc():
   global greet
   greet  = "hello world"
   print(greet)


getfunc()

print(greet)

wd = 'awesome'
def myfunc():
  wd1 = 'fantastic'
  print("local: Python is " + wd1)

myfunc()
print('global: Python is ' + wd)

word = 'awesome'
def myfunc():
  global word
  word = 'fantastic'
myfunc()
print('global from func: Python is ' + word)

def myfunction() :
  return True

if myfunction():
  print("YES!")
else:
  print("NO!")







