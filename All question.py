All Question 

Q1.Print name, age, college and branch

name = input("Enter your name:tejas ")
age = input("Enter your age:18 ")
college = input("Enter your college name:RBU ")
branch = input("Enter your branch:ECS ")
print("\n--- Student Details ---")
print(f"Name:    {name}")
print(f"Age:     {age}")
print(f"College: {college}")
print(f"Branch:  {branch}")



Q2.Take name as input and greet the user

name=input("hello!tejas")
print(f"hello,{name}!It's nice to meet you")



Q3.Take name as input and greet the user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")



Q4.Perform all arithmetic operations on two numbers

num1=float(intput("enter the number 1")
num2=float(intput("enter the number 2")
addition       = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2
division       = num1 / num2
# Display the results
print(f"Numbers: {num1} and {num2}\n")
print(f"Addition (+):          {addition}")
print(f"Subtraction (-):       {subtraction}")
print(f"Multiplication (*):    {multiplication}")
print(f"Division (/):          {division}")



Q5.Calculate area of a circle

import math
radius = float(input("Enter radius: "))
area =3.14*pi * radius * radius
print("Area of circle:", area)



Q6.Calculate simple interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si = (p * r * t) / 100
print("Simple Interest:", si)



Q7.Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)



Q8.Calculate total and percentage of 5 subjects

s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))
s4 = float(input("Enter marks of subject 4: "))
s5 = float(input("Enter marks of subject 5: "))
total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
print("Total:", total)
print("Percentage:", percentage, "%")



Q9.Swap two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("First number:", a)
print("Second number:", b)



Q10.Convert seconds into hours, minutes and seconds

seconds = int(input("Enter total seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)



Q11.Check whether a number is positive, negative or zero

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



Q12.Check whether a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")





