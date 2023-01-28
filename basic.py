#To print any string
print('Hey, This is Md. Zahidul Islam')
#Practice Print
print('0----')
print(' ||||')
print('*' * 10)

#Variables in  python
name = 'Jhon Smith'
age = 20
is_newPatient = True
print(name, age, is_newPatient)

#Receiving input from user
#user_name = input('What is your name? ')
#print('Hi ' + user_name)
    #Ask two question 1. name 2. favourite color and print like - Zahid likes Blue
#person_name= input('What is your name? ')
#favourite_color = input('What is your favourite color? ')
#print(person_name + ' likes ' + favourite_color)


#Type conversion
#birth_year= input('Enter your birth year ')
#age = 2023 - int(birth_year)
#print(age)

    #Ask a user's weight in pound and print in kilogram
#user_weight_lbs = input('Weight in lbs ')
#weight_kg = int(user_weight_lbs) * 0.45
#print(weight_kg)

#String repesentation and functionalities
course = 'python for beginers'
print(course)
course = "python's course for beginer"
print(course)
course = 'python course for "beginer"'
print(course)
message = ''' Hi Mr. Z
This is checking multiline string as email 


Thanks
Python Programmer
'''
print(message)
string_index_testing = "Progrmming is fun"
print(string_index_testing[0])      #To print 1st charecter of string
print(string_index_testing[-1])     #To print last charecter of string
print(string_index_testing[-2])     #To print second last charecter of string
print(string_index_testing[0:3])    #To print charecters in the index from 0 to 2 of string
print(string_index_testing[0:])     #To print all charecter of string
print(string_index_testing[2:])     #To print all charecters from index 2 in the string
print(string_index_testing[:])      #To print all charecter of string
print(string_index_testing[1:-1])   #To print all charecters in the index from 1 to second last of string


#Formatted strings
first_name ='Zahidul'
last_name = 'Islam'
message = first_name + ' [' + last_name + '] is a coder'        #Printing in a manual formatted string
formatted_message = f'{first_name} [{last_name}] is a coder'    #Printing formatted string with method
print(message)
print(formatted_message)

#String Methods
message= 'Python for Beginners'
print(message)
print(len(message))
print(message.upper())
print(message.lower())
print(message.find('n'))
print(message.replace("Beginners", 'Absolute Beginners'))
print(message.replace('n', 'k'))
print("Python" in message)

#Arithmetic operator in python
print(10 + 3)           #Addition
print(10 - 3)           #Subtruction
print(10 * 3)           #Multiplication
print(10 / 3)           #Division to get float result
print(10 // 3)          #Division to get int result
print(10 % 3)           #Reminder
print(10 ** 3)          #Exponent which is power

number = 10
number += 5             #Augmented assignment operator
print(number)

#Operator Precedence
number = (10 + 3) * 2 ** 2        #Parenthesis> Exponential > multiplication/devision > addition/subtruction
print(number)

#Math Functions
number = 5.4
print(round(number))
print(abs(-5.4))

import math
number1 = 3
number2 =4
print(math.ceil(number))
print(math.floor(number))
print(math.factorial(number1))
print(math.fabs(-5.6))

print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

#If statement

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.2 * price
else:
    down_payment = 0.1 * price
print(down_payment)

#Logical Operator
has_high_income = False
has_good_credit = True
has_criminal_record= False
if has_high_income or has_good_credit:              #Logical OR operator
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if has_good_credit and not has_criminal_record:     #logical AND operator with logical NOT operator
    print("eligible for loan")
else:
    print("not eligible for loan")
#Comparison operator
name = 'Zahidul'
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be maximum 50 characters")
else:
    print("Name looks good")

#While loop
index = 1
while index<=5:
    print("*" * index)
    index +=1
print("completed")

#For loops
for item in ["Python", "JaVA", "c"]:
    print(item)

for item in range(2, 20, 2):        #range(starting point, endpoint , step)
    print(item)
#Imagine A shopping cart and we have to calculate total amount of price of all items holded to the cart
prices = [2, 25, 35, 5, 10, 6, 7]
total = 0
for price in prices:
    total+=price
print(f"Total: {total}")

#Nested loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

#Using nested loop print "F" shape of x
numbers = [5, 2, 5, 2, 2]
for number_count in numbers:
    output = " "
    for x in range(number_count):
        output+= "x"
    print(output)
#List in python
numbers =[2, 9, 10, 41, 6, 1, 2, 5, 8]
maximum= numbers[0]
for number in numbers:
    if number> maximum :
        maximum = number
print(f"Maximum : {maximum}")











