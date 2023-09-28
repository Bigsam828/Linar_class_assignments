# creating a code to calaculate the equation 5a+(3b)^2

print("To calculate 5a+(3b)^2")                 #printing an introductory message

a= input(" Please input value a")               #collecting the value of the variable a 

b=input("Please input value b")                 #collecting the value of the variable b

A= int(a)                                       #converting the "a" from 'string' to 'interger' data type datatype, while representing 'a' with 'A'

B=int(b)                                        #converting the "b" from 'string' to 'interger' data type datatype, while representing 'b' with 'B'

C= A*5                                          #representing a part of the equation with C and using operators to calculate 

D=3*B                                           #representing a part of the equation with B and using operators to calculate

Y= pow(D,2)                                     #using the power function to exponentiate D to the power of 2

X=C+Y                                           #using opertors to sum up the whole equation

print(X)                                        #priting out the final value