def give_name(name):
    print("Your name is: "+ name)
def give_age(age):
    print("Your age is:",age)
name = input("What is your name? ")
give_name(name)
while True:
    age = int(input("How old are you? "))
    if age > 0 and age < 120:
        give_age(age)
        break
    else:
        print("Try again!!")
        print("New input: ")

