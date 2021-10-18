# Import the random function and generate both a random number between 0 an 1 as well as a random number between 1 and 10
import random


def print_random_num(number):
   print(f'Random number fro one to ten: {number}')


random_num = random.random()
print(random_num)
random_num = random.randrange(1,10)
print(random_num)
# Use the datetime library together with the random number to generate a random, unique value.
import datetime
unique_value = str(random_num) + str(datetime.datetime.now())
print(unique_value)