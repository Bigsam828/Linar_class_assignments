#This is a script to calculate the total cost and number of blocks required to construct a python structure
#A python structure is any builiding which has 4 rooms and a toilet
import math
#welcoming the user to the calculator
print("Welcome to AJS civil construction company cost calculator")
name=input("Please enter your name")

print("To calculate the total cost and number of blocks required to construct a python structure, please follow the steps below")
#colllecting the length and breadth of the four rooms and the toilet
length_room_a=(float(input("please enter room a length in feet")))
breadth_room_a=(float(input("please enter room a breadth in feet")))
length_room_b=(float(input("please enter room b length in feet")))
breadth_room_b=(float(input("please enter room b breadth in feet")))
length_room_c=(float(input("please enter room c length in feet")))
breadth_room_c=(float(input("please enter room c breadth in feet")))
length_room_d=(float(input("please enter room d length in feet")))
breadth_room_d=(float(input("please enter room d breadth in feet")))
length_toilet=(float(input("please enter toilet length in feet")))
breadth_toilet=(float(input("please enter toilet breadth in feet")))

#collecting the building block type from the user
cost_of_a_building_block=input('What type of building block, do you want to use? a: 600naira, b: 1000naira, c: calculate both for me. Enter either a or b or c ')

#creating a condition to calculate the total number of blocks based on the users preferrence
if cost_of_a_building_block == 'a' or cost_of_a_building_block == 'b' or cost_of_a_building_block == 'c':
 
    #assigning a costant value to the height of all the rooms(a constant height)
    height_rooms=height_room_a=height_room_b=height_room_c=height_room_d=height_toilet=144 #144 is inches and is equivalent to the 12ft given in the question
    
    #assining values to the length, breadth and height of the building blocks in inches
    length_block_a=15
    breadth_block_a=6
    height_block_a=9
    length_block_b=20
    breadth_block_b=10
    height_block_b=12

    #calulating the number of blocks required to fill the height of the room
    no_blocks_to_fill_height_of_room1=math.ceil(height_rooms/height_block_a)
    no_blocks_to_fill_height_of_room2=math.ceil(height_rooms/height_block_b)

    #creaitng a function to calculate the number of blocks required for a room
    def no_blocks_for_a_room(x,y,q,h) :
        '''T function calculates the total number of blocks required to construct a room 
        by finding the total number of blocks required to consturct one level of blocks in
        a wall, then finding the total number of blocks required to construct a wall , by 
        multiplying the total numnber of block required to construct a level, by the number
        of blocks required to fill the wall's height. It does the same preocess again but
        this time using the breadth of the room, and finally finds the total number of blocks
        required to build the room, by adding product of the length wall and 2, to the
        product of the breadth wall of the room and 2.
        This function takes 4 parameters which are represented by x,y,q,h
        note that the values used to represent the parameters are not in any way related to 
        the names of the values they are representing and are just used to fill in the parameters 
        in the function defintion because the real parameter names are quite long.
        The original parameter names and the values representing them are stated below
        x = length of room
        y = breadth of room
        q = length of building block
        h = no of blocks required to fill the height of the room
        '''
        length_of_room=x 
        breadth_of_room=y 
        length_of_building_block=q 
        no_of_blocks_required_to_fill_the_height_of_the_room= h 

        a = math.ceil(length_of_room / length_of_building_block)
        b = math.ceil(breadth_of_room/length_of_building_block)
        c = a*no_of_blocks_required_to_fill_the_height_of_the_room
        d = b*no_of_blocks_required_to_fill_the_height_of_the_room
        e=2*(c+d)
        return e

    #calculating the total number of blocks for the rooms using the first block by calling the created function
    no_blocks_for_room_a1=no_blocks_for_a_room(x=length_room_a,y=breadth_room_a,q=length_block_a,h=no_blocks_to_fill_height_of_room1)
    no_blocks_for_room_b1=no_blocks_for_a_room(x=length_room_b,y=breadth_room_b,q=length_block_a,h=no_blocks_to_fill_height_of_room1)
    no_blocks_for_room_c1=no_blocks_for_a_room(x=length_room_c,y=breadth_room_c,q=length_block_a,h=no_blocks_to_fill_height_of_room1)
    no_blocks_for_room_d1=no_blocks_for_a_room(x=length_room_d,y=breadth_room_d,q=length_block_a,h=no_blocks_to_fill_height_of_room1)
    no_blocks_for_toilet1=no_blocks_for_a_room(x=length_toilet,y=breadth_toilet,q=length_block_a,h=no_blocks_to_fill_height_of_room1)
    
    #Calculating the total number of blocks to build the house using the first block, by suming the number of blocks for the rooms
    no_blocks_to_build_house1=no_blocks_for_room_a1 + no_blocks_for_room_b1 + no_blocks_for_room_c1 + no_blocks_for_room_d1 + no_blocks_for_toilet1
    #calculating the total number of blocks for the rooms using the second block by calling the created function
    no_blocks_for_room_a2=no_blocks_for_a_room(x=length_room_a,y=breadth_room_a,q=length_block_b,h=no_blocks_to_fill_height_of_room2)
    no_blocks_for_room_b2=no_blocks_for_a_room(x=length_room_b,y=breadth_room_b,q=length_block_b,h=no_blocks_to_fill_height_of_room2)
    no_blocks_for_room_c2=no_blocks_for_a_room(x=length_room_c,y=breadth_room_c,q=length_block_b,h=no_blocks_to_fill_height_of_room2)
    no_blocks_for_room_d2=no_blocks_for_a_room(x=length_room_d,y=breadth_room_d,q=length_block_b,h=no_blocks_to_fill_height_of_room2)
    no_blocks_for_toilet2=no_blocks_for_a_room(x=length_toilet,y=breadth_toilet,q=length_block_b,h=no_blocks_to_fill_height_of_room2)
    no_blocks_to_build_house2=no_blocks_for_room_a2 + no_blocks_for_room_b2 + no_blocks_for_room_c2 + no_blocks_for_room_d2 + no_blocks_for_toilet2
    
    #Calculating the total number of blocks to build the house using the first block by suming the number of blocks for the rooms
    no_blocks_to_build_house2=no_blocks_for_room_a2 + no_blocks_for_room_b2 + no_blocks_for_room_c2 + no_blocks_for_room_d2 + no_blocks_for_toilet2
    total_Cost_1=no_blocks_to_build_house1*600
    total_cost_2=no_blocks_to_build_house2*1000
    if cost_of_a_building_block == 'a':
        print(f'Dear {name}, the number of blocks required to construct a python structure with the given dimension, using 600 naira building blocks is{no_blocks_to_build_house1} and total cost is {total_Cost_1}naira')

    elif cost_of_a_building_block == 'b': 
        print(f'Dear {name}, the number of blocks required to construct a python structure with the given dimension, using 1000 naira building blocks is{no_blocks_to_build_house2} and total cost is {total_cost_2}naira')

    elif cost_of_a_building_block == 'c':
        print(f'Dear {name}, the number of blocks required to construct a python structure with the given dimension, using 600 naira building blocks is {no_blocks_to_build_house1} and total cost is {total_Cost_1}naira')
        print(f'Dear {name}, the number of blocks required to construct a python structure with the given dimension, using 1000 naira building blocks is {no_blocks_to_build_house2} and total cost is {total_cost_2}naira')

else :
    print('Enter a correct option')

