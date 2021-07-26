# Reeborgs World Hurdle 3 Challenge

# Use the link to see the problem:
link="https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json"


# Solution code:
"""

def turn_around():
    turn_left()
    turn_left()
    

def turn_right():
    turn_around()
    turn_left()

def draw_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while at_goal()==False:
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
        
"""