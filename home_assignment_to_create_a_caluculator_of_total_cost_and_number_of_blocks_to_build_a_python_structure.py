#welcoming the user to the calculator
print("Welcome to AJS civil construction company cost calculator ")
print("To calculate the total cost and number of blocks required to construct a python structure, please follow the steps below")

#colllecting the length and breadth of the four rooms and the toilet
length_room_a=(round(float(input("please enter room a length in feet")))+0.5)
breadth_room_a=(round(float(input("please enter room a breadth in feet")))+0.5)

length_room_b=(round(float(input("please enter room b length in feet")))+0.5)
breadth_room_b=(round(float(input("please enter room b breadth in feet")))+0.5)

length_room_c=(round(float(input("please enter room c length in feet")))+0.5)
breadth_room_c=(round(float(input("please enter room c breadth in feet")))+0.5)

length_room_d=(round(float(input("please enter room d length in feet")))+0.5)
breadth_room_d=(round(float(input("please enter room d breadth in feet")))+0.5)

length_toilet=(round(float(input("please enter toilet length in feet")))+0.5)
breadth_toilet=(round(float(input("please enter toilet breadth in feet")))+0.5)

#assigning a costant value to the height of all the rooms(a constant height)
height_room_a,height_room_b,height_room_c,height_room_d,height_toilet="144","144","144","144","144" #144 is inches and is equivalent to the 12ft given in the question

#assining values to the length, breadth and height of the building blocks
length_block_a=15
breadth_block_a=6
height_block_a=9
length_block_b=20
breadth_block_b=10
height_block_b=12

#calculating the number of blocks required to build a wall
no_blocks_to_fill_height_of_room=16                                  #16 is gotten by dividing the room height: 144 inches, by the block height: 9 inches

#calculating the perimeter of the base of room a
base_perimeter_room_a=(length_room_a+breadth_room_a)*2                  #i'm adding 1 to give an additional block too correct the error that will arise as a result rounding the numbers

#calculating the total number of blocks required to fill the peimeter of the base of room a
no_blocks_to_fill_base_perimeter=(base_perimeter_room_a*12)/15     #i am multiplying by 12 to convert it to inches, since the length and breadth were collected in feet. i am dividing by 15, which is the block height to find the total number of blocks needed to fill the base perimeter

#calculating the total number of blocks required to build room a
no_blocks_room_a=no_blocks_to_fill_base_perimeter*no_blocks_to_fill_height_of_room

#calculating the perimeter of the base of room b
x=length_room_b+breadth_room_b
base_perimeter_room_b=x*2

#claculating the number of blocks to fill the base perimeter of room b
no_blocks_to_fill_base_perimeter_b=((base_perimeter_room_b*12)/15)

#calculating the total number of blocks required to build room b
no_blocks_room_b=no_blocks_to_fill_base_perimeter_b*no_blocks_to_fill_height_of_room

#calculating the perimeter of the base of room c
y=length_room_c+breadth_room_c
base_perimeter_room_c=y*2

#claculating the number of blocks to fill the base perimeter of room c
q=base_perimeter_room_c*12
no_blocks_to_fill_base_perimeter_c=q/15                                 #i am multiplying by 12 to convert it to inches, since the length and breadth were collected in feet. i am dividing by 15, which is the block height to find the total number of blocks needed to fill the base perimeter

#calculating the total number of blocks required to build room c
no_blocks_room_c=no_blocks_to_fill_base_perimeter_c*no_blocks_to_fill_height_of_room

#calculating the perimeter of the base of room d
z=length_room_d+breadth_room_d
base_perimeter_room_d=z*2

#claculating the number of blocks to fill the base perimeter of room d
r=base_perimeter_room_d*12
no_blocks_to_fill_base_perimeter_d=r/15                                 #i am multiplying by 12 to convert it to inches, since the length and breadth were collected in feet. i am dividing by 15, which is the block height to find the total number of blocks needed to fill the base perimeter

#calculating the total number of blocks required to build room d
no_blocks_room_d=no_blocks_to_fill_base_perimeter_d*no_blocks_to_fill_height_of_room

#calculating the perimeter of the base of toilet
s=length_toilet+breadth_toilet
base_perimeter_toilet=s*2

#claculating the number of blocks to fill the base perimeter of toilet
t=base_perimeter_toilet*12
no_blocks_to_fill_base_perimeter_toilet=t/15                                 #i am multiplying by 12 to convert it to inches, since the length and breadth were collected in feet. i am dividing by 15, which is the block height to find the total number of blocks needed to fill the base perimeter

#calculating the total number of blocks required to build toilet
no_blocks_toilet=no_blocks_to_fill_base_perimeter_toilet*no_blocks_to_fill_height_of_room

#summing all the no of blocks for the room to get the number of blocks for the house
no_blocks_for_house=round(no_blocks_room_a+no_blocks_room_b+no_blocks_room_c+no_blocks_room_d+no_blocks_toilet)

#getting the total cost by multiplying the total number of blocks for the house by their cost

total_cost_A=round(no_blocks_for_house*600)

#creating another block of code to calculate using the dimensions of block b
no_blocks_to_fill_height_of_room2=12

#calculating the total number of blocks required to fill the peimeter of the base of room a
no_blocks_to_fill_base_perimeter=(base_perimeter_room_a*12)/20           #i am multiplying by 12 to convert it to inches, since the length and breadth were collected in feet. i am dividing by 15, which is the block height to find the total number of blocks needed to fill the base 
print("The total number of blocks needed",no_blocks_for_house)      
print( "and the total cost for build your python structure is",total_cost_A,"naira" )
if total_cost_A>=10000:
    reply=input("Oga you sure say you get money ?")

elif reply>="yes":
    print("ODOGWU")

