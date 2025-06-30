"""
If n is even, divide it by 2 → n = n / 2
If n is odd, multiply by 3 and add 1 → n = 3n + 1
Keep going until n becomes 1.
"""
def collatz(n):
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # finally print 1

Num = int(input("Number: "))
collatz(Num)
