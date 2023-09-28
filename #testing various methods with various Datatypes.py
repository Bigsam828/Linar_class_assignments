#testing various methods with various Data types
#creating a function to confirm that a correct gender is entered and thus determine wether Mr or Mrs will be used when giving output
def gender_check():
    '''this function creates a set of condtions for a situation in which a user enters an invalid gender'''
    if gender== 'male':
        x='Mr' 
    elif gender== 'female':
        x='Mrs'
    elif gender_isalpha==False:
        print('there isn\'t supposed to be a number in your answer')
        print('please restart the program and input a valid gender')
    else:
        print('please resatrt the program and input a valid gender')
    print(x)
    return x

#creating a function to confirm that a valid phone number is entered
def no_check():
    if phone_no_valid:
        phone=phone_no
    
    else :print('Enter a valid answer after restarting the program')



#ade=ade.isalpha().strip()name_isalpha= name.isalpha()

#if ade:
#    print('ade is a boy')


#collecting user name
name=input('input a name')

#removing spaces at the beginning and end of the string, using the strip() method
name=name.strip()

#using the capitalize() method in case the user doesn't enter a name with the first letter captalized as a proper noun should be
name= name.capitalize()

#collecting the user's gender
gender=input('input your gender')

#removing spaces at the beginnning and end of the string
gender=gender.strip()

#using the  () method to make the gender entered suitable for comaprison so that the code will function irrespective of whatever case the gender is entered
gender=gender.casefold()
print(gender)

#confirming that the value entered by the user is an alphabetical string 
gender_isalpha=gender.isalpha()

#using the function defined earlier to carry out various actions, based on whatever the user enters 
gender_check()

#collecting the user's phone number
phone_no= input('input your phone number')

#confirming that the value entered is made up numbers, using the isalnum() method
phone_no_valid= phone_no.isalnum()
no_check()

addresses=input('please input your home address')

#using the strip method to remove spaces before and after the value
addresses=addresses.strip()

#using the title() method to convert the address into title case as the adress names are expected to be proper nouns
address=addresses.title()

#creating a string to use the format method on
address=('so you live at {} in Igando, Lagos right ?')

#using the format() method on the string
address=address.format(addresses)


#using the strip method in case the user enters a name with spaces before or after the name

""" all the various methods used in this script
.strip()
.capitalize()
.isalpha()
.isalnum()
.title()
.foramt()
.casefold"""