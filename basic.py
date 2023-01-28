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

