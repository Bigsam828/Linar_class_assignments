#welcoming the user to the calculator
print("Welcome to samuel's quadratic equation solver")

print("To solve your quadratic equation, please follow the steps below")

#collecting data values
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))
#the steps followed below, in solving a quadratic equations are from the general quadratic equation formula i.e: x= (-b +\- ((b^2 - 4ac)^1/2))/2a
terma=b**2
term_b=a*c
termb=4*term_b
termc=-1*b
termd=2*a
term_e=terma-termb
terme=term_e**0.5
termf1=termc+terme
termf2=termc-terme
x1=termf1/termd
x2=termf2/termd
if term_e<0:
    print("your answer is a complex number")
if term_e==0:
    print("your answers are real and equal numbers")
if term_e>0:
    print("your answers are real and unequal numbers")
print("X=",x1)
print("X=",x2)

