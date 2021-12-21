#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        number = i
        if number % 15 == 0:
            print("FizzBuzz", end=' ')
        elif number % 3 == 0:
            print("Fizz", end=' ')
        elif number % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
