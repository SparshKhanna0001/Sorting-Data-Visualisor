import turtle 
import tkinter as tk


def create_bar(x, y, width, height, fill_color, outline_color="black", canvas =0):
    """
    Creates a rounded rectangle with the given specifications.

    Args:
        x: The x-coordinate of the starting position.
        y: The y-coordinate of the starting position.
        width: The width of the rectangle.
        height: The height of the rectangle.
        fill_color: The color to fill the rectangle with.
        outline_color: The color of the outline (default: black).
    """
    if canvas == 1:    
        screen = turtle.TurtleScreen(canvas)
        pen = turtle.RawTurtle(screen)
    else:
        pen = turtle.Turtle()
    pen.speed(0)  # Fastest speed
    pen.pensize(1)  # Thicker outline

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.fillcolor(fill_color)
    pen.begin_fill()

    # Draw rounded corners using a series of arcs
    for _ in range(2):

        pen.forward(width - 10)  # Adjust for corner arcs
        pen.circle(2, 90)  # Create a quarter-circle arc
        pen.forward(height -10)
        pen.circle(2, 90)
    
    pen.end_fill()
    pen.hideturtle()


def draw_arrow(x, y, direction, canvas=0):

    if canvas == 1:    
        screen = turtle.TurtleScreen(canvas)
        screen.setup(width=600, height=400, startx=0, starty=0) 
        arrow = turtle.RawTurtle(screen)
    else:
        arrow = turtle.Turtle()

    arrow = turtle.Turtle()
    arrow.speed(0)
    arrow.color("green")
    arrow.pensize(3)
    arrow.penup()
    arrow.goto(x, y)
    arrow.pendown()

    if direction == 'y':
        arrow.setheading(180)
        arrow.left(135)
        arrow.forward(20)
        arrow.backward(20)
        arrow.right(90)
        arrow.forward(20)
        arrow.backward(20)
        arrow.left(45)
    elif direction == 'x':
        arrow.setheading(90)
        arrow.left(135)
        arrow.forward(20)
        arrow.backward(20)
        arrow.right(90)
        arrow.forward(20)
        arrow.backward(20)
        arrow.left(45)

    arrow.hideturtle()

def create_axes(screen_width, screen_height, canvas = 0):
    """Creates the X and Y axes on the Turtle screen."""
    
    if canvas == 1:    
        screen = turtle.TurtleScreen(canvas)
        pen = turtle.RawTurtle(screen)
    else:
        pen = turtle.Turtle()
    
    pen.speed(0)  # Set speed to fastest
    pen.pensize(2)  # Set axis line thickness

    # Draw X-axis (horizontal)
    pen.penup()
    pen.goto(-screen_width // 2, -175)  # Start at left edge of screen
    pen.pendown()
    pen.goto(screen_width // 2, -175)  # End at right edge of screen
    draw_arrow(screen_width//2,-175,'x')


    # Draw Y-axis (vertical)
    pen.penup()
    pen.goto(-260, -200)  # Start at bottom edge of screen

    pen.pendown()
    pen.goto(-260, 200 // 2)  # End at top edge of screen
    draw_arrow(-260, 200 // 2,'y')

    # Label the axes)
    pen.penup()
    pen.goto(screen_width // 2 - 20, -205)
    pen.write("X", align="right", font=("Monospace", 15, "bold"))
    pen.goto(-290, screen_height // 2 - 15)
    pen.write("Y", align="left", font=("Monospace", 15, "bold"))

    pen.hideturtle()  # Hide the pen turtle

def position_definition(height_color: dict, width=70, bars=5):
    x,y, space_between = -165, -177, (width//3)
    
    #checking for main window
    if __name__!="__main__":
        canvas= 1
    else:
        canvas = 0    
    for i in range(bars):
        create_bar(x, y, width, list(height_color.keys())[i],height_color[list(height_color.keys())[i]], canvas)
        x = x + space_between+ width

if __name__=='__main__':
    
    turtle.penup()
    turtle.goto(0,200)
    turtle.pendown()
    turtle.write("Alert: Incorrect prompt!", align="center", font=("Arial", 12, "bold"))
    turtle.penup()
    turtle.hideturtle()

    turtle.textinput("Array Elements", prompt='Enter Here')
    create_axes(600,400)
    array = [100, 150, 250, 300,174.2]
    color = ("maroon", "magenta", "turquoise", "chocolate", "skyblue", "gold")
    my_dict = dict(zip(array, color))
    position_definition(my_dict)
    
    turtle.done()

"""
    create_bar(20,40,100,45,color='orange')
    create_bar(-10,-15,100,45,color='skyblue')
"""