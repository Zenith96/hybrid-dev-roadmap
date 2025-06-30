def right_triangle(n):
    for i in range(1,n+1):
        print("*"*i)
def left_triangle(n):
    for i in range(1,n+1):
        print(" " * (n - i)+ "*"*i)
def center_triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*((2*i)-1)+" "*(n-i))

N = int(input("Number of rows : "))
#right_triangle(N)
#left_triangle(N)
center_triangle(N)
