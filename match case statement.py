#MATCH CASE  statement..
# A Match case statement will compare a given variable's value to different shapes or in easy words to comapare with all the patterns until it will fits any one of them..
x = input("enter the value of x")

match x:#The match / case statement in Python is used for pattern matching — it’s like a more powerful version of if-elif-else..
#It was added in Python 3.10.
    case 1:
        print("one")
    case 2:
        print("two")
    case _:#underscore means the default(like else)..if anyone case not match the default case will be match automatically..
        print("something else")
#Cleaner and more readable than many if...elif...else statements..
#✅ Can match values, types, structures (like lists, tuples, dicts)..


# example with if else satement..

x=3
match x:
    case n if n < 0:# n is the name of case..
        print("Negative number")# if  x is lees then 0 ans will be negative..
    case n if n == 0: # if x==0 output will be zero..
        print("Zero")
    case n if n > 0:# if x greater then 0 output will be positive
        print("Positive number")