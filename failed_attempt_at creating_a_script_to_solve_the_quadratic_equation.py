import cmath
# creating  a script to calculate the value of P in the equation ax^2+bx+c
a=int(input("input a"))
b=int(input("input b"))
c=int(input("input c"))

Terma=b**2
Term_a=4*a*c
Term_b=Terma-Term_a
#Termb=Term_b**(1/2)
print(Term_b)
strterm_b = str(Term_b)
newterm_b = strterm_b[0]
#print(newtermb)
#RealTerm_b = float(newterm_b)
if newterm_b == '-':
    Termb = cmath.sqrt(Term_b)
    strtermb = str(Termb)
    newtermb = strtermb[:-1]
    #print(newtermb)
    RealTermb = float(newtermb)
    print(Termb)
    print(type(Termb))

else:
    RealTermb = Term_b**0.5



Term_i=Term_b*-1
Termi=(Term_i**0.5)#and "i"
Termc=2*a
Termd=-1*b
#if Term>0 == True:
if RealTermb>0: 
    x1 = (Termd+RealTermb)/Termc
    x2 = (Termd-RealTermb)/Termc
    print(f"x1= {x1}")
    print(f"x2= {x2}")
else:
    x1 = (Termd+Termi)/Termc
    x2 = (Termd-Termi)/Termc
    print(f"x1= {x1}i")
    print(f"x2= {x2}j")
'''

if (Termb == type(complex)): 
    x1 = (Termd+Termi)/Termc
    x2 = (Termd-Termi)/Termc
    print(f"x1= {x1}")
    print(f"x2= {x2}")
#elif (Termb>0) == False:
#    x1 = (Termd+Termi)/Termc
#    x2 = (Termd-Termi)/Termc
#    print(f"x1= {x1}")
#    print(f"x2= {x2}")

if Termb>0 == True: x2 = (Termd+Termb)/Termc
elif Termb>0 == False: x1 = (Termd-Termb)/Termc

print(f"x1= {x1}")
print(f"x2= {x2}")
'''
