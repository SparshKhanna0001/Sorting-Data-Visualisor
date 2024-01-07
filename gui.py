import turtle
import tkinter as tk    
from SortingAlgorithms.sorting import BubbleSort, SelectionSort, RadixSort, Heapsort, QuickSort, InsertionSort, CountingSort

#global arguments- 
color = ("maroon", "magenta", "turquoise", "chocolate", "skyblue", "gold")
array_elements= []

root = tk.Tk()  # Create the main Tkinter window
root.resizable(0,0)
root.title("Sorting Algorthm Visualisor")

canvas = tk.Canvas(root, width=600, height=600, highlightthickness=0)  # Display the canvas within the Tkinter window

"""Turtle Functions"""

screen = turtle.TurtleScreen(canvas)
pen  = turtle.RawTurtle(screen)
pen.speed(0)
pen.hideturtle()

import turtle

# ... (Tkinter boilerplate setup) ...

# Create a RawTurtle object
pen = turtle.RawTurtle(screen)

# Hide the turtle (optional)
pen.hideturtle()

# Set the font and color
pen.color("black")
pen.font = ("Roman", 50, "bold")  # Adjust font as needed

# Text to display
text = "1. Enter Five Numbers, all not more than 10.\n2. Then Click the Button To validate your input.\n3. Then Select the Type Of Sorting Algorithm.\n4. Wait and Watch\n\nFor again soprting the list of numbers provided, press <Reset> button AND then <SUBMIT> button."

# Move the pen to the specified starting coordinates
pen.penup()
pen.goto(-280, 150)  # Adjusted coordinates for desired starting position

# Write the text at the current position
pen.write(text)  # No alignment specified, so it will start from the current position


def create_bar(x, y, width, height, fill_color,turtleObj=pen,outline_color="black"):
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
    turtleObj.pensize(1)  # Thicker outline
    turtleObj.setheading(0)
    turtleObj.penup()
    turtleObj.goto(x, y)
    turtleObj.pendown()

    turtleObj.fillcolor(fill_color)
    turtleObj.begin_fill()

    # Draw rounded corners using a series of arcs
    for _ in range(2):

        turtleObj.forward(width - 10)  # Adjust for corner arcs
        turtleObj.circle(2, 90)  # Create a quarter-circle arc
        turtleObj.forward(height -10)
        turtleObj.circle(2, 90)
        
    turtleObj.end_fill()
    turtleObj.hideturtle()

def draw_arrow(x, y, direction,turtleObj):

    turtleObj.speed(0)
    turtleObj.color("green")
    turtleObj.pensize(3)
    turtleObj.penup()
    turtleObj.goto(x, y)
    turtleObj.pendown()

    if direction == 'y':
        turtleObj.setheading(180)
        turtleObj.left(135)
        turtleObj.forward(20)
        turtleObj.backward(20)
        turtleObj.right(90)
        turtleObj.forward(20)
        turtleObj.backward(20)
        turtleObj.left(45)
    elif direction == 'x':
        turtleObj.setheading(90)
        turtleObj.left(135)
        turtleObj.forward(20)
        turtleObj.backward(20)
        turtleObj.right(90)
        turtleObj.forward(20)
        turtleObj.backward(20)
        turtleObj.left(45)

    turtleObj.hideturtle()
    turtleObj.color("Black")

def create_axes(turtleObj):
    """Creates the X and Y axes on the Turtle screen."""

    turtleObj.speed(0)  # Set speed to fastest
    turtleObj.pensize(2)  # Set axis line thickness
    # Draw X-axis (horizontal)
    turtleObj.penup()
    turtleObj.goto(-225, -175)  # Start at left edge of screen
    turtleObj.pendown()
    turtleObj.goto(285, -175)  # End at right edge of screen
    draw_arrow(287,-175,'x',turtleObj)


    # Draw Y-axis (vertical)
    turtleObj.penup()
    turtleObj.goto(-200,200)  # Start at bottom edge of screen

    turtleObj.pendown()
    turtleObj.goto(-200,-200)  # End at top edge of screen
    draw_arrow(-200,200,'y', turtleObj)

    # Label the axes)
    turtleObj.penup()
    turtleObj.goto(280, -205)
    turtleObj.write("X", align="right", font=("Monospace", 15, "bold"))
    turtleObj.goto(-285,185)
    turtleObj.write("Y", align="left", font=("Monospace", 15, "bold"))

    turtleObj.hideturtle()  # Hide the pen turtle

position_definition_ids = []

def position_definition(height_color: dict, turtleObj, width=70, bars=5):
    x, y, space_between = -165, -174, (width // 3)

    for i in range(bars):
        element_id = create_bar(x, y, width, list(height_color.keys())[i], height_color[list(height_color.keys())[i]], turtleObj)
        position_definition_ids.append(element_id)
        x = x + space_between + width
    return position_definition_ids
        #    turtle.done()

# Function to delete position_definition elements
def delete_position_definition_elements():
    for element_id in position_definition_ids:
        canvas.delete(element_id)

# Entry box for array elements
array_entry = tk.Entry(root, width=30)

# Label for displaying messages
message_label = tk.Label(root, text="")

# Function to handle array input and display messages
def get_array_elements():
    global array_elements

    element_string = array_entry.get()
    try:
        array_elements = [float(value) for value in element_string.split(",")]
        for i in array_elements:
            if i > 10:
                raise ValueError

        # ... Process or store the array as needed ...
        message = "You entered: " + ", ".join(str(x) for x in array_elements)

        message_label.config(text=message, foreground="black")
    except ValueError:
        message_label.config(text="Invalid input. Please enter comma-separated numbers.", foreground="red")

# Button to trigger input and message display
input_button = tk.Button(root, text="Submit 5 numers less than 10 ...", command=get_array_elements)

# Define the function to reset the array_elements to an empty list
def reset_array():
    global array_elements
    array_elements = []  # Reset the array_elements to an empty list

# Create the reset button
reset_button = tk.Button(root, text="Reset...", command=reset_array)
reset_button.grid(row=2, column=4)  # Adjust the row and column as needed

# Function to create a rounded button with specified text and command
def create_rounded_button(text, command):
    button = tk.Button(root, text=text, command=command, width=15, height=2)  # Adjust width and height as needed
    button.config(
    relief="flat",  # Remove default border
    bg="#ed3309",  # Set background color
    activebackground="#f55f3d",  # Set color on hover
    fg="white",  # Set text color
    font=("Monospace", 10, "bold")  # Set font style
    )
    button.bind("<Enter>", lambda event: button.config(bd=3))  # Add border on hover
    button.bind("<Leave>", lambda event: button.config(bd=0))  # Remove border on leave
    return button

def stds_pocesses():
    canvas.delete("all")
    create_axes(pen)

def Bubble():
    global color
    global array_elements  # Access the global array_elements variable
    global sorter

    def bubble_sort_callback():
        delete_position_definition_elements()
        my_dict = dict(zip((value*37.5 for value in array_elements), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Continue sorting if needed or perform any other action
        
    # Create an instance of BubbleSort
    sorter = BubbleSort.BubbleSort(bubble_sort_callback)
    
    # Trigger BubbleSort algorithm and visualization update
    sorter.sort(array_elements)

# ... (rest of your code remains unchanged) ...

def Selection():
    global color
    global array_elements
    global sorter

    def selection_sort_callback(sorted_array):
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in sorted_array), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed

    # Create an instance of SelectionSort
    sorter = SelectionSort.SelectionSort()

    # Trigger SelectionSort algorithm and visualization update
    sorter.sort(array_elements, selection_sort_callback)


def Merge():
    global color
    global array_elements
    global sorter

    def merge_sort_callback():
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in array_elements), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed

    # Create an instance of MergeSort
    sorter = MergeSort.MergeSort()
    sorter.register_callback(merge_sort_callback)

    # Trigger MergeSort algorithm and visualization update
    array_elements = sorter.sort(array_elements)

def Radix():
    global color
    global array_elements
    global sorter

    def radix_sort_callback(arr):
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in arr), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed

    # Create an instance of RadixSort
    sorter = RadixSort.RadixSort()

    # Trigger RadixSort algorithm and visualization update with the callback
    sorter.sort(array_elements, radix_sort_callback)


def Heap():
    global color
    global array_elements
    global sorter

    def heapsort_callback():
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in array_elements), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed
        
    # Create an instance of Heapsort
    sorter = Heapsort.Heapsort(heapsort_callback)
    
    # Trigger Heapsort algorithm and visualization update
    sorter.sort(array_elements)

def Quick():
    global color
    global array_elements
    global sorter

    def quick_sort_callback(sorted_array):
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in sorted_array), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed

    # Create an instance of QuickSort
    sorter = QuickSort.QuickSort()

    # Trigger QuickSort algorithm and visualization update
    sorter.sort(array_elements, quick_sort_callback)


def Insertion():
    global color
    global array_elements
    global sorter

    def insertion_sort_callback():
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in array_elements), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed
        
    # Create an instance of InsertionSort
    sorter = InsertionSort.InsertionSort(insertion_sort_callback)
    
    # Trigger InsertionSort algorithm and visualization update
    sorter.sort(array_elements)


def Counting():
    global color
    global array_elements
    global sorter

    def counting_sort_callback():
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in array_elements), color))
        stds_pocesses()
        position_definition(my_dict, pen)
        # Additional steps can be added here if needed
        
    # Create an instance of CountingSort
    sorter = CountingSort.CountingSort(counting_sort_callback)
    
    # Trigger CountingSort algorithm and visualization update
    sorter.sort(array_elements)


def Bucket():
    global color
    global array_elements
    global sorter

    def bucket_sort_callback():
        delete_position_definition_elements()
        my_dict = dict(zip((value * 37.5 for value in array_elements), color))
        stds_pocesses()
        position_definition(my_dict, pen)
    # Additional steps can be added here if needed

    # Create an instance of BucketSort
    sorter = BucketSort.BucketSort(bucket_sort_callback)

    # Trigger BucketSort algorithm and visualization update
    sorter.sort(array_elements)



btn1 = create_rounded_button("BubbleSort", Bubble )
btn2 = create_rounded_button("SelectionSort", Selection )
btn3 = create_rounded_button("MergeSort", Merge )
btn4 = create_rounded_button("RadixSort", Radix )
btn5 = create_rounded_button("Heapsort", Heap )
btn6 = create_rounded_button("QuickSort", Quick )
btn7 = create_rounded_button("InsertionSort", Insertion )
btn8 = create_rounded_button("CountingSort", Counting )
btn9 = create_rounded_button("Bucket Sort", Bucket)


"""
Packing the elements
"""

canvas.grid(row=1,column=1)

array_entry.grid(row=2,column=0)  # Place the entry box within your layout
input_button.grid(row=2, column=1)
message_label.grid(row=2,column=2)  # Place the label below the entry box

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn4.grid(row=4,column=2)
btn5.grid(row=5,column=0)
btn6.grid(row=5,column=1)
btn7.grid(row=5,column=2)
btn8.grid(row=6,column=1)


if __name__=="__main__":
    root.mainloop()