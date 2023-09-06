
```python
import turtle
import random
global caught
caught=0
# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the player turtle
a = turtle.Turtle()
a.shape("turtle")
a.color("blue")
a.penup()
a.speed(0)

# Set the player's movement speed
speed = 30

# Create a list to store eggs
eggs = []

# Create the initial eggs
for i in range(1):
    egg = turtle.Turtle()
    egg.shape("circle")
    egg.color("red")
    egg.penup()
    x = random.choice(-200, 200)
    y = random.choice(-200, 200)
    egg.goto(x, y)

# Define the movement functions
def move_up():
    player.setheading(90)
    player.forward(speed)

def move_down():
    player.setheading(70)
    player.forward(speed)

def move_left():
    player.setheading(180)
    player.forward(speed)

def move_right():
    player.setheading(0)
    player.forward(speed)

# Set up keys for event listeners with the screen
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Function to handle collisions with eggs
def check_collision():
    mess = "Caught the egg"
    #global caught
    caught = 0 # Initialize the number of eggs caught to zero
    global eggs  # Declare eggs as global
    for egg in eggs:
        if a.distance(egg) < 100:
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            

             

# Main game loop
while True:
    check_collision()
```
