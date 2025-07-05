"""
A function: Multiples of 3 => Fizz , Multiples of 5 => Buzz , Multiples of 15 => FizzBuzz ,
Multiples of 7 => Boom ,Multiples of 3 , 5 and 7  => FizzBuzzBoom
"""
def fizzbuzz_plus(n):
    for i in range(1, n+1):
        str1 = ""
        if i % 3 == 0:
            str1+= "Fizz"
        if i % 5 == 0:
            str1+= "Buzz"
        if i % 7 == 0:
            str1 += "Boom"
        if str1 == "":
            str1 += str(i)
        print(str1)
n = int(input("Your N digits are upto: "))
fizzbuzz_plus(n)
