while True:
    #importing the random module
    import random
    #collecting user name
    def name():
        global user_name
        user_name = input('Enter your name')
        user_name.strip()
        user_name.capitalize()
    

    #welcoming the  user
    def welcome():
        print("WElCOME! WElCOME! WElCOME! \nWelcome to my game of Rock Paper Scissors \nIn this game there are two modes: \n \t Singleplayer and \n \t Multiplayer")
        print("Singleplayer: In singleplayer, you play against the computer")
        print('Multiplayer : You play against a fellow living opponent, taking turns.\nBut due to some issues, the multiplayer mode is not available yet, and will be implemented in a future update')

    #displaying the rules
    def rules():
        print('THE RULES')
        print('The Rules of the game are simple: \nEach player picks from one of three options: Rock, Paper, and Scissors \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock')
        print('there are multiple rounds in each match.\nAt the end of a round, the winner is awarded a point.\nplayers will play until one of them reaches three points ')
        print('OBJECTIVE:\nGet a score of three, before the game ends.\nGoodluck ;)')

    #creating a function perform the whole gamimg process
    def game_process():
        #creating a dictionary to store the three options for the computer
        choice = {0:'rock', 1: 'paper', 2:'scissors'}

        #creating variables to store the scores of the computer and the user
        u_s = 0                                                   #u_s here is an abbreviation for user score
        c_s = 0                                                   #c_s here is an abbreviation for computer score
        #creating a loop to make decisions(determine the winner based on the choices of the user and the computer)
        while True:  

            #creating a loop to collect users choice and ensure that an appropriate value is entered
            while True:
                #helping the commputer make its  choice(this is a random choice)
                c_v = choice[ (random.randint(0,2)) ]                                   #c_v here is an abbreviation for computer value i.e the choice of the computer
            
                #handling the various errors which could arise
                try:
                    #collecting the users choice
                    u_v = input('Enter your choice')                                 #u_v here is an abbreviation for user value i.e the choice of the user
                    #making the input suitable for comparison
                    u_v.casefold()
                    #breaking the loop if the correct value is entered
                    if u_v=='rock':
                        break
                    elif u_v=='paper':
                        break
                    elif u_v=='scissors':
                        break
                    #sustaining the loop in case the wrong answer is entered
                    else:
                        print('Error, enter a correct answer')
                #retaining the loop in case a value error is discovered
                except ValueError:
                    Print('Enter a correct response')

            if c_v == u_v:            
                print(f'Computer picked {c_v}')                                          
                print('This is a tie')
            elif c_v == 'rock':
                print(f'Computer picked {c_v}')   
                if u_v =='paper':
                    print('You win this round')
                    u_s+=1
                    
                else:
                    print('Computer wins this round')
                    c_s+=1
                    
            elif c_v == 'paper':
                print(f'Computer picked {c_v}')   
                if u_v =='scissors':
                    print('You win this round')
                    u_s+=1
                    
                    
                else:
                    print('Computer wins this round')
                    c_s+=1
                    
            elif c_v == 'scissors':
                print(f'Computer picked {c_v}')   
                if u_v =='rock':
                    print('You win this round')
                    u_s+=1
                    
                else:
                    print('Computer wins this round')
                    c_s+=1
            if (u_s == 3 or u_v ==3):
                break
            
            #printing the score at the end of the round\
            print(f'The scores are \n \t {user_name}:{u_s}\n \t Computer:{c_s}')
        if c_s > u_s :
            print('HA HA HA !!! Ccomputer wins YOU BE OTU :) ')
        else:
            print('Congrats you won')

    def fullgame():
        name()
        welcome()
        rules()
        game_process()

    
    fullgame()

    while True:
        restart = input('Do you want to continue the game Y/N')
        restart.strip()
        restart.casefold()
        if restart == 'y':
            break
        elif restart =='n':
            break
        else : 
            print('Invalid response, recheck options')


    if  restart == 'y':
        print('OK')
        fullgame()
    else :
        print('Goodbye')
        break

                

        