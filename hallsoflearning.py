# -*- coding: utf-8 -*-
"""HallsofLearning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Htfx6Z2E1U7V0ETuaClM7F3iFN-4dVvM

Hello my name is Saheed Reid

Question 1. Store your name and age in variables and print.
"""

name:str
age:int
age = 17
name = "Saheed"
print(name)
print(age)

"""Question2. Given a list of numbers print only the even number"""

numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
  if numbers[i] % 2 == 0:
    print(numbers[i])

"""Question3. Write a function that returns the square of a number"""

number:int
number = 0
number = input("Enter a number: ")
square = (int(number)*int(number))
print(square)

"""Question 4. Create a dictionary with three fruits and their colors"""

def fruits(x):
  name_of_fruit1 = ""
  name_of_fruit1 = "Banana"
  name_of_fruit2 = ""
  name_of_fruit2 = "Orange"
  name_of_fruit3 = ""
  name_of_fruit3 = "Mango"
  color_of_fruit1 = ""
  color_of_fruit1 = "yellow"
  color_of_fruit2 = ""
  color_of_fruit2 = "orange"
  color_of_fruit3 = ""
  color_of_fruit3 = "red"

"""Question5. Create a function that does the following:"""

number = input("Enter a number: ")
def check_divisibility(number):
    if number % 4 == 0 and number % 5 == 0:
        print("YayNay")
    elif number % 4 == 0:
        print("Yay")
    elif number % 5 == 0:
        print("Nay")
    else:
        print(number)
print(number)