
import random

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
    
    
def name_to_number(name):
    
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    
    
   


def rpsls(name): 
    
    player_number = name_to_number(name)   

    
    comp_number = random.randrange(0,5) 
    
    difference = (player_number - comp_number) % 5
    
   
    if difference == 0:
        result = "Player and computer tie!"
    elif difference == 1:    
        result = "Player wins!"
    elif difference == 2:
        result = "Player wins!"
    elif difference == 3:
        result = "Computer wins!"
    elif difference == 4:
        result = "Computer wins!"
    else: 
        result = "Oops! We ran into problem!! Try once more. "  

    
    comp_name = number_to_name(comp_number)
    
  
    
    print "Computer chooses ",comp_name
    print "Player chooses ",name
    print result
    print " "
    

rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




