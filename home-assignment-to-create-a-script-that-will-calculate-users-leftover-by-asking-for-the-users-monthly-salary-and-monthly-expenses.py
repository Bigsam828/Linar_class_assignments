print("Welcome to the monthly leftover calculator")


i=input("Please input your monthly income")             #colllecting user's monthly income

e1=input("Now please enter your accomodation expenses") #collecting user's monthly expenses
e2=input("please enter your feeding expenses")
e3=input("please enter your transportation expenses") 
e4=input("please enter your electricity expenses")   

print("Nice")

currency=input("Now please input currency")             #collecting user's earning currency  

I=int(i)                                                #converting user's input from string to interger data type

E=int(e1)+int(e2)+int(e3)+int(e4)  

                                             #converting user's input from string to interger data type
l=(I-E)                                                 #calculating user's total monthly leftover

print("Your monthly leftover is",l,currency)            #printing user's monthly leftover)500