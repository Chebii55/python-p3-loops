#!/usr/bin/env python3

def happy_new_year():
    x=10
    while (x > 0):
        print(x)
        x-=1
    print("Happy New Year!")

def square_integers(int_list):
    listLength = len(int_list)
    i=0
    for i in range(listLength):
        int_list[i] *=int_list[i]
    return (int_list)

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
    
