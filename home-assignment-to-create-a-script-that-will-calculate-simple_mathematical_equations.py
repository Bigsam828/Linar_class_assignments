# creating  a script to calculate the value of P in the equation P=3+(4v^a)
'''print("To calaculate P=3+(42v^a)")
v= int(input("Input the value v"))

a= int(input("input the value a"))
Term_a=pow(v,a)
Term_b=4*Term_a
P=3*Term_b
print(P)/5/aa'''


# creating  a script to calculate the value of  in the equation ax^2+bx+c
a=int(input("input a"))
b=int(input("input b"))
c=int(input("input c"))

Terma=b**2
Term_a=4*a*c
Term_b=Terma-Term_a
Termb=Term_b**0.5
Term_i=Term_b*-1
Termi=(Term_i**0.5)and "i"
Termc=2*a
Termd=-1*b
if Termb>0 == True: x2 = (Termd+Termb)/Termc
elif Termb>0 == False: x1 = (Termd-Termb)/Termc

print("x1=",x2)
print("x2=",x2)

#Creating a script to calculate the value of Y In Y=L-F^w[((sL)/F )+((20/F)^n)]/20^w +F**0.5

#assigning values to the variables in the equation and conveting the the from stirng to the interger data type, using the int functiom

L=int(input("input L"))
f=int(input("input f"))
w=int(input("input w"))
s=int(input("input s"))
n=int(input("input n"))
#breaking the equation into parts, assigning them variable names (a,b,c,d,e)
a=f**w

b=(s*L)/f

c=(20/f)**n

d=20**w

e=f**0.5

#using operators to merge the parts of the equation  to form the orignal equation

g=b+c

h=d+e

i=a*g

j=i/h

#collecting the final value(answer)
Y=L-j

#printing the result
print(Y)