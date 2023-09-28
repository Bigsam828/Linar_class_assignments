'''print(range)

range = [2,3 ,45,6,4,5]
for age in range:
    print(age)
    print('you are a teeenager')


for age in range(13,20):
    print(age)
    print('you are a teenager')
    
sum=0
for value in range(1,6):
    #5=5+4
    sum +=value            
    print(sum)
'''
def no_of_iterations():
    if  x==0:
        suf=st
    elif x==1:
        suf=nd
    elif x==2:
        suf=rd

#creating a function to calculate the sum of a given set of numbers
def avg(n):
    '''this function calculate the sum of a given set of numnbers
    the function only accepts a parameter which must be the number
    of interger values which the user wants to calculate the sum of.
    
    The actual values are collected by the function, when the function
    is called'''
    x=0
    i=0
    while x < n:
        print(x)
        num=int(input(f'enter number'))
        i+=num
        if x==n: 
            return i
            break
        x+=1
    return i 

print(avg(10))


def find_average(values):

    ''' This function helps to calculate the 
    sum of a given set of values. the difference
     is that all the values are specified as parameter find_average(list:[values])
    the arguments to be entered must
    be a list of intergers'''
    l= len(values)
    result = 0
    x=0
    for v in values:
        result += v
        x+=1
        if x==l:
            return result

print(f'Average= {find_average([5,6, 7, 8])}')
'''for x in range( 100,1,-9):
   
    def find_average(values):
        result = 0
        for v in values:
            result += v
            return result
            
    print("AVERAGE", find_average([5,6, 7, 8]))

    print (x)'''