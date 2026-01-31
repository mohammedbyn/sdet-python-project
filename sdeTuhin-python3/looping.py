for i in range(5):
  print(i)

fruits = ["Apple","Mango","Orange"]

for fruit in fruits:
     print(fruit)

i = 1
while i <=5 :
    print(i)
    i += 1


result = ""

for i in range(1, 6):
    result += str(i) + " "

print("one line output = "+result.strip())


print("output_range1_6 = ", *range(1, 6))
print(*range(0, 5))  # → 1, 2, 3, 4


result = ""

for i in range(1, 6):
    result += str(i) + " "

print("forLoop result = "+ result.strip())

print(range(5))
for i in range(0, 5):
    print(i)

# Looping Through Arrays / Collections

numbers = [1, 2, 3]
for num in numbers:
    print("array = ", + num)
    print(numbers)

    print(numbers[0])

# while loop

"""
java:
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
python: remove let and all brakets for python

python:
"""
i = 0
while i < 3:
    print("whileLoop = ", i)
    i += 1

#  #  // Use Case: Calculate and display the sum of numbers from 1 to 100.

sum = 0;
for i in range(1, 100+1):
    sum += i

print("total sum of loop for 100 iteration = ",sum)

# print even numbers between 1 and 20

evens = []
for e in range(1, 21):
    if(e % 2 == 0):
        evens.append(e)

print("Even Number Array1 = ", evens)

even2 = [ i for i in range(1, 21) if i % 2 == 0]
print("Even Numbers Array2 = ", even2)
print("Even Numbers in One Line  =  ", *even2)

for i in range(2, 7, 2):
    print(i)   #  output 2 4 6


# odd number
for o in range(1, 5, 2):
    print(o)   #  1 3

odds = []
for o in range(1, 10):
    if(o % 2 != 0):
        odds.append(o)
print("odd numbers = ",odds)

# odd number without using if
odd1 = []
for o1 in range(1, 5, 2):
    odd1.append(o1)
print("odd num array--> no if = ", odd1)   #  1 3

# even number without using if

eNum = " "
for en in range(2, 5, 2):
    eNum += str(en) + " "
print("evenNum-->no if = ", eNum.strip())

eNum1 = []
for en1 in range(2, 9, 2):
    eNum1.append(en1)
print("evenNum1 Array --> no if = ", eNum1)

nums = [10, 20, 30]

for index, value in enumerate(nums):
    print(index, " : ",value)


evenNums = []
oddNums  = []

for i in range (1, 7):
    if i % 2 == 0:
        evenNums.append(i)
    else:
        oddNums.append(i)

    print("Even Numbers = ", evenNums)
    print("Odd Numbers  =  ", oddNums)

# Reverse counting numbers from 5 to 1 using range
reverse = "  "
for r in range(5, 0, -1):
    reverse  += str(r) + "  "

print('reverse numbers from 5 to 1  =  ', reverse)

# // Multiplication Table print the multiplication table
# // of a given number 5 between 1 to 5
#  f" "

print('===multiplication table===')
print("-------------------------------")

givenNumber = 5
for mul in range(1, 6):
    print(f"{mul} X {givenNumber}  =  {mul * givenNumber}")


## Example of f"string {variables} " ---->  f "   "

name = 'Cathy'
age  =  22
print(f"My name is {name} and I am {age} years old.")

"""
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == "admin123":
        print("Login successful")
        break

    attempts += 1
    print("Invalid password")

if attempts == max_attempts:
    print("Account locked")
"""