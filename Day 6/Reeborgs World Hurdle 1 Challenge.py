# Reeborgs World Hurdle 1 Challenge

# Use the below link to see the problem:

link="https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json"

# Code:
"""
#move()

def turn_around():
    turn_left()
    turn_left()
    

def turn_right():
    turn_around()
    turn_left()

# draw square
def draw_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
#draw_square()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    


for i in range(6):
    jump()
    
"""