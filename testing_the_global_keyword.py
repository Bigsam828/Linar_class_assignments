'''this '''

#the global keyword converts a local variable(i.e a variable declared within a function) into a global variable(i.e a variable callable out side of the function) 
def sum():
    global x
    x=23
    return x
sum()
print(x)

x=25
print(x)

x=24
print(x)

sum()
print(x)
