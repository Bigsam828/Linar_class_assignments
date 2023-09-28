#doing stirng slicing by using the 'islice' function from the 'itertools' module
import itertools
string = "Geek for Geeks"

print(".joinitertools.islice(string,3,3)")


#finding the length of tuple (note that i have done the same for other collection-data-types i.e list, set and dictionary)
x= ("apps","banana","cherry")
print(len(x))

#finding the datatype of a collection 
x=("popopo")
print(type(x),end="")
x=dict(())
print(type(x))

print()

#testing how to unpack values from a tuple ,also using the asterik to unpack multiple values into a single variable name

fruits= tuple(("apple","banana","mango","raspberry","cherry"))
print(type(fruits))
(a1,a2,*a3,a4)=fruits
print(a1)
print(a2)
print(a3)
print(a4)
[*a4]=fruits
print(a4)

#looping through a tuple
