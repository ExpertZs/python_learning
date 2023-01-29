#To print any string
import random

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

#2D list
matrix = [
    [1, 5, 8],
    [8, 5, 6],
    [-5, -6, 8]
]
print(matrix)
print(matrix[2][1])
matrix[2][1]=6
print(matrix[2][1])
print(matrix)

for row in matrix:
    for item in row:
        print(item)

#List method
numbers = [15, 8, 6, 4, 2, 47, 41, 4]
print(numbers)
numbers.append(-6)              #Insert a new item in the last in list
print(numbers)
numbers.insert(3,3)             #Insert a new item in the mentioned index in list
print(numbers)
numbers.remove(41)              #Remove a item from the list
print(numbers)
numbers.index(47)               #Checking existence of an item in the  list
print(numbers)
numbers.pop(2)                  #Remove an item of mentioned index from the list
print(numbers)
print(numbers.count(4))         #Checking number of occurence of an item in the list
print(41 in numbers)            #Checking existence of an item in the list
numbers2 = numbers.copy()       #Copy the existing list
numbers.clear()                 #Remove all items from the list
print(numbers)
print(numbers2)
numbers2.sort()                 #Sorting the list
print(numbers2)
numbers2.reverse()              #sorting in decending order
print(numbers2)
        #Removing duplicate item from the list
numbers=[2, 6, 3, -5, -2, 6, -5, -2, 2, 3]
unique=[]
for item in numbers:
    if item not in unique:
        unique.append(item)
print(f"After removing duplicate value {unique}")

#Tuples                 #Tuples are immuteable. You can only access the item of tuples but can not change it
numbers =(2,6,7)
print(numbers[2])

#Unpacking

        #For tuples
coordinate = (2,5,4)
x, y, z = coordinate
print(x)
print(y)
print(z)
        #For list
numbers = [1, 9, 3]
x, y, z = numbers
print(x)
print(y)
print(z)

#Dictionaries
customer = {
    "name": "Zahidul",
    "age" : 27,
    "phone": "+8801754898514"
}
print(customer["phone"])
customer["birthdate"]= "28-11-1996"
print(customer)
print(customer.get("name"))
print(customer.get("address"))

        #Receiving phone number in digit and return in words
digit_mapping ={
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
#phone = input("Enter your Phone number ")
#output = ""
#for charecters in phone:
 #   output += digit_mapping.get(charecters, "!!" )+ " "
#print(output)

#Emoji converter

#message = input("> ")
#words = message.split(" ")
#output= " "
#emojis ={
 #   ":)": "😂",
  #  "(:": "😢"
#}

#for word in words:
 #   output+= emojis.get(word, word) + " "
#print(output)

#Function
def greet_user(first_name, last_name):                  #Parameter
    print(f"Good mornning {first_name} {last_name}")
    print("Welcome to the world of python")


print("Hello")
greet_user("Zahidul", "Islam")                          #Argument
greet_user(last_name="shakib", first_name="Sadman")     #Keyword Argument
print("Thanks")

#Return Statement
def square(number):
    return number * number


result = square(6)
print(result)

#Creating reusable function example of emoji converter

def emoji_converter(message):
    words = message.split(" ")
    output= " "
    emojis ={
        ":)": "😂",
        ":(": "😢"
    }
    for word in words:
        output+= emojis.get(word, word) + " "
    return output


#message = input("> ")
#result= emoji_converter(message)
#print(result)

#Exception
try:
    age =22 # int(input("Age: ")) #To avoid receiving input from user
    income = 25000
    risk = income/age
    print(age)

except ZeroDivisionError:
    print("Can not divided by zero")

except ValueError:
    print("Invalid Value")

#Class
class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("move")


point1 = Point()
point1.x = 10
print(point1.x)
point1.move()

#Constructor
class Person:
    def __init__(self, name):               #constructor
        self.name = name
    def talk(self):
        print(f"Hello, I am {self.name}")


person = Person("Zahidul")
person.talk()
person1 = Person("Sakib")
person1.talk()

#Inheritance
class Animal:
    def walk(self):
        print("walk")
    def drink(self):
        print("drink")


class Cat(Animal):
    def meaw(self):
        print("Meaw")

class Dog(Animal):
    def berking(self):
        print("Berking")


cat = Cat()
cat.meaw()
cat.walk()
cat.drink()


#Module in Python
import utils                    #Import all function of the mentioned module

#from utils import find_max      #import a specific function from the mentioned module

numbers = [6,-4, 55, 66, 8, 66, 62, 44, 22, 101, 11, 123]
maximum = utils.find_max(numbers)
print(maximum)

#Package
import ecommerce.shipping                               #import whole module from package
from ecommerce import shipping                          #import whole module from package with from syntax
from ecommerce.shipping import calculate_shipping       #import specific funcion from mentioned module

calculate_shipping()

#Generating Random values
import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second


dice= Dice()
print(dice.roll())


