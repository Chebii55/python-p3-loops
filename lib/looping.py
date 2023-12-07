#!/usr/bin/env python3

def happy_new_year():
    x=10
    while (x > 0):
        print(x)
        x-=1
    print("Happy New Year!")

def square_integers(int_list):
    new_array=[area *area for area in int_list]
    return new_array

def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
        num += 1
    
