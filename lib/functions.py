#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("yusra")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("programmer")

def add(num1, num2):
    result = num1 + num2
    return result

number1 = 10
number2 = 15
results = add(number1, number2)
print("The sum is", results)

def halve(number):
    result = number / 2
    return result
    