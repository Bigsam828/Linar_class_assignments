#I am writing a script to calculate the total coat of a given amount of coaster cartons to be ordered by a customer

# Here i am welcoming the user to the calculator
print('Welcome to AJS coaster carton purchase software ')
print('This function calculates the total of a preferred quantity of coaster cartons')

# I am defining a function to calculate the total cost of a given quantity of coaster biscuits 
#by asking for their desired type,size,quantity
def coaster_cost():
    '''this function calculates the total of a preferred quantity of coaster cartons 
    by requesting for coaster type, size and quantity
    it does not require any parameter and all the needed values are colected within 
    the function'''
    #collecting the coaster type from the user and assigning it to the variable coaster_type
    coaster_type=input('Please enter your coaster type ?( Enter either 50 or 20)')

    # Making the variable coaster size global so it can be called outside of the function 
    global coaster_size
    
    # Collecting the desired coaster carton size from the user and assigning it to the variable coaster_size
    coaster_size=input('please enter your coaster carton size ?( Enter either small,medium or large)')

    def calculations ():
        '''this is a function to calculate the total cost of the number of coaster biscuits, using the three values collected above'''
        # Making the variable coaster_quantity global so it can be called outside of the function 
        global coaster_quantity

        # Collecting the desired coaster quantity from the user and assigning it to the variable 'coater_quantity'.NB: The 'coaster_quantity' here means the total number of cartons ordered
        coaster_quantity=float(input('please enter your desired quantity ?( Enter in numbers the quantity rounded off to .5 becsue we only sell in carton and half carton)'))
      
        # Making the variable 'cost_of_coaster' a global variable so it can be called outside of the function and utilized(printed and summed) NB: You made this mistake when you were first wrting 
        # this script and it gave you a lot of difficulty in gettiing the code to work. It is important to globalize the variable containing the final answer as it would be called repeatedly later in the code
        global  cost_of_coaster
        # Multiplying the coaster quantity by the price per carton and assigning the product to the variable 'cost_of_coaster'
        cost_of_coaster=coaster_quantity*x
        
        # Returning the cost of coaster. NB: The 'cost_of_coaster' here means the total cost of the number of cartons order
        return cost_of_coaster
    
    # There are different prices for different carton sizes and so i am creating a condition to assign different prices to the variable 'x' dpendent on whatever size the user selects 
    # These are the first, second and third conditions. There is an else condition below, should the user enter a wrong input
    # The variable 'x' here represents price per carton 
   
    if coaster_size=='small':
        x=4000
        calculations()
        
    elif coaster_size=='medium':
        x=5500
        calculations()

    elif coaster_size=='large':
        x=7000
        calculations()
     
        
    else :
        print('please restart the program and enter a valid answer')

    # Returning the cost of coaster. NB: The 'cost_of_coaster' here means the total cost of the number of cartons order
    return cost_of_coaster
# Calculating the first price 
# By calling the function

x1=coaster_cost()
'''
you can uncomment the following commands to test for issues, if your code is not working you can use it to narrow down the location of a bug when theres an error in the code
print(x1)
print(coaster_quantity)
print(coaster_size)
print(cost_of_coaster)'''

#asking the user if they want to continue purchasing
a=input('do you still intend to order more goods (Input either yes or no)')

#setting a condition to print out the total cost of the quantity of goods they ordered, and the quantity they ordered, if they choose not to continue
if a == 'no': 
    print(f' you ordered for {coaster_quantity} {coaster_size} coaster cartons and the cost is = {x1} naira')

#setting another condition to recall the function if they choose to continue/make another order
elif a == 'yes':

    # Assigning the quantity and coaster size to a variable to store them for later use. since the user is not ready to stop purchasing 
    first_quantity_and_size = f'{coaster_quantity} {coaster_size} coaster cartons'

    #calculating for the second time
    x2 = coaster_cost()

    #asking the user if they want to continue purchasing
    a2 = input('do you still intend to order more goods (Input either yes or no)')

    #setting a condition to print out the total cost of the quantity of goods they ordered, and the quantity they ordered, if they choose not to continue
    if a2 == 'no':
        print(f" you/'ve ordered for {first_quantity_and_size}, {coaster_quantity} {coaster_size} coaster cartons, and the cost is = {x1+x2} naira")

    #setting another condition to recall the function if they choose to continue/make another order
    elif a2 == 'yes':

        # Assigning the quantity and coaster size to a variable to store them for later use. Since the user is not ready to stop purchasing 
        second_quantity_and_size= f'{coaster_quantity} {coaster_size} coaster cartons'
        
        #calculating for the third time
        x3 = coaster_cost()

        #asking the user if they want to continue purchasing
        a3 = input('do you still intend to order more goods (Input either yes or no)')

        #setting a condition to print out the total cost of the quantity of goods they ordered, and the quantity they ordered, if they choose not to continue
        if a3 == 'no':
            print(f'you\'ve ordered for {first_quantity_and_size}, {second_quantity_and_size}, {coaster_quantity} {coaster_size} coaster cartons and the cost is = {x1+x2+x3} naira')
        
        #setting a condition in case the user chooses to continue
        elif a3 == 'yes':
            
            # Assigning the quantity and coaster size to a variable to store them for later use. Since the user is not ready to stop purchasing
            third_quantity_and_size= f'{coaster_quantity} {coaster_size} coaster cartons'
            
            #calculating for the fourth time
            x4 = coaster_cost()

            #asking the user if they want to continue purchasing
            a4 = input('do you still intend to order more goods (Input either yes or no)')

            #setting a condition to print out the total cost of the quantity of goods they ordered, and the quantity they ordered, if they choose not to continue
            if a4 == 'no':
                print(f" you/'ve ordered for {first_quantity_and_size} , {second_quantity_and_size} ,{third_quantity_and_size}, {coaster_quantity} {coaster_size} coaster cartons and the cost is = {x1+x2+x3+x4} naira")
            
            #setting a condition in case the user chooses to continue
            elif a4 == 'yes':

                # Assigning the quantity and coaster size to a variable to store them for later use. Since the user is not ready to stop purchasing
                fourth_quantity_and_size= f'{coaster_quantity} {coaster_size} coaster cartons'

                #calculating for the fourth time
                x5 = coaster_cost()

                #asking the user if they want to continue purchasing
                a5 = input('do you still intend to order more goods (Input either yes or no)')
               
                #setting a condition to print out the total cost of the quantity of goods they ordered, and the quantity they ordered, if they choose not to continue
                if a5 == 'no':
                    print(f" you/'ve ordered for {first_quantity_and_size} , {second_quantity_and_size} ,{third_quantity_and_size}, {fourth_quantity_and_size}, {coaster_quantity} {coaster_size} coaster cartons and the cost is = {x1+x2+x3+x4+x5} naira")

                #setting a condition in case the user chooses to continue           
                elif a5 == 'yes':

                    # Assigning the quantity and coaster size to a variable to store them for later use. Since the user is not ready to stop purchasing
                    fifth_quantity_and_size= f'{coaster_quantity} {coaster_size} coaster cartons'

                    #calculating for the fifth time
                    x6 = coaster_cost()

                    #asking the user if they want to continue purchasing
                    a6 = input('Do you still intend to order more goods (Input either yes or no)')
                    
                    #setting a condition to print out the total cost of the quantity of goods they ordered, and the quantity they ordered, if they choose not to continue
                    if a6 == 'no':
                        print(f" You/'ve ordered for {first_quantity_and_size} , {second_quantity_and_size} ,{third_quantity_and_size}, {fourth_quantity_and_size}, {fifth_quantity_and_size}, {coaster_quantity} {coaster_size} coaster cartons and the cost is = {x1+x2+x3+x4+x5+x6} naira")

                    #setting a condition in case the user chooses to continue
                    elif a6 == 'yes':

                        # Printing a message telling the user this is the end of the script, instead of calculating for the sixth time
                        print(f'You have gotten to the maximum number of orders. You can stop here or simply restart the program')

                        # Asking the user wether to print the final answer 
                        final_answer=input('Print out final answer?(Input either \'yes\' or \'no\')')

                        # Creating a condition in case they choose to continue
                        if final_answer=="yes":

                            # Printing the total cost and the quantity and sizes for the six orders the user has made 
                            print (f" You/'ve ordered for {first_quantity_and_size} , {second_quantity_and_size}, {third_quantity_and_size}, {fourth_quantity_and_size}, {fifth_quantity_and_size}, {coaster_quantity} {coaster_size} coaster cartons and the cost is = {x1+x2+x3+x4+x5+x6} naira")
                       
                        # Creating a condition in case they choose not to continue
                        elif final_answer=='no':
                            
                            # Printing a farewell message
                            print('ok Goodbye ') 

                        # Setting a final condition in case the user chooses to the wrong answer
                        else :
                            # Printing a message telling the user that a wrong input has been entered
                            print('you input a wrong answer. Please restart the program or exit')


 