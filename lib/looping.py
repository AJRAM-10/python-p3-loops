#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
        print("Happy New Year!")

def square_integers(int_list):
    stupid_list = list()
    for i in int_list:
        stupid_list.append(i**2)
    return stupid_list

def fizzbuzz():
    
    for i in range(101):
        if i > 0 and (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif i > 0 and i % 3 == 0:
            print("Fizz")
        elif i > 0 and i % 5 == 0:
            print("Buzz")
        elif i > 0:
            print(f"{i}")