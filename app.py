print("hello world ")
print("*" * 10)
print("*" * 7)
print("*" * 4)
print("*" * 2)
print("Hello World")
x = 1
print(x)
name = "john"
b = 2
print(name)
print(x + b)
a = 3
q = 10

"""
    python string manipulation
"""
print("========string manipulation========")

course = "Python Programming"
for c in course:
    print(' ',c, end=" ")
    if c == " ":
        break
print('      ')

for i in course:
    print(i)
    if i == " ":
        break

print("========string start from left or first char========")
print(len(course))  # 18
print(course[0])  # P ( of Python )
print(course[5])  # n ( of Python )


print(course[0:3])  # Pyt
print(course[:3])  # Pyt
for c in course[0:3]:
    print(c)
""""
  loop output 
    P
    y
    t
"""
print(course[0:])  # Python Programming
print(course)
if (course[0:]) == course:
    print(True)

print("========string start from right or last char========")

print(course[-1])  # g (of Programming)
print(course[-7])  # r (of Programming)
print(course[0 - 3])  # i (of Programming)
print(course[-6:-2])  # [-6 = start] [ -2 = remove last 2 ] output= ammi

print(course[-2:])  # ng (of Programming)
print(course[-4:])  # ming (of Programming)
print(course[-11:])  # Programming
print(course[-len(course) :])  # Python Programming


"""
reverse string in python
"""
print("===start reversed string in python==")
my_string = "python"

# using slicing step -1

my_reversed_string = my_string[::-1]
print("Reversed string of python = " + my_reversed_string)

count = len(my_reversed_string)
print(count)
for rc in my_reversed_string:
    print(rc)

#  Using  join() + reversed() builtin function

reversed_string = "".join(reversed(my_string))
# or ''.join(reversed(my_string))
print(
    "Reversed string of python using join + (reversed) functions = " + reversed_string
)

# using for loop

loop_reversed_str = ""  # Initialize an empty string to hold reversed result
for ch in my_string:
    loop_reversed_str = ch + loop_reversed_str
    print("Reversed string implemented by for loop of python = " + loop_reversed_str)

    for i in loop_reversed_str:
        print(i)
        if i == "o":
            break
