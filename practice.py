def calculateGmean(a,b):
    Gmean = (a*b)/(a+b)
    print(Gmean)          

def isgreater(a,b):
    if a > b:
        print("a is greater than b")
    elif a < b:
        print("b is greater than a")
    else:
        print("a and b are equal")

a = 9
b = 8
isgreater(a,b)
calculateGmean(a,b)

c = float(input("Enter first number "))
d = float(input("Enter second number "))
isgreater(c,d)
calculateGmean(c,d)