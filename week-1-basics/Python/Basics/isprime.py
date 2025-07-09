"""
Write a function is_prime(n) that returns True if n is a prime number, else False.
Then create another function print_primes(limit) that prints all prime numbers from 2 to limit.
"""
import math
def is_prime(n):
    if n <= 1 :
        return False
    if n == 2 :
        return True
    if n % 2 == 0 :
        return False
    for i in range(3, int(math.sqrt(n)) + 2 , 2):
        if n % i == 0:
            return False
    return True
def print_primes(limit):
    for i in range(2, limit+1):
        if is_prime(i):
            print(i , end =" ")
n = int(input("Your N digits are upto: "))
print("Is the number prime?",is_prime(n))
print("Number of numbers prime upto N: ")
print_primes(n)