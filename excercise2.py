#exercise 2...
#make a program where user input the time and according to time the code response..
a = int(input("enter the number"))
b = input("Enter your name")
if a < 12:
    print(" Good Morning , " + b)
elif a > 12:
    print("Good Afternoon , " + b)
elif a > 6:
    print("Good Evening , " + b)
elif a > 8:
    print("Evening is over , " + b + "Good Night , " + b)
