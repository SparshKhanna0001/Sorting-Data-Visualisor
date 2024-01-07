
import turtle
import tkinter as tk

root = tk.Tk()  # Create the main Tkinter window

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()  # Display the canvas within the Tkinter window

turtle_screen = turtle.TurtleScreen(canvas)  # Create Turtle screen using the canvas
turtle_screen.bgcolor("lightgreen")
t = turtle.RawTurtle(turtle_screen)
t.shape("turtle")


def button_action():
    t.forward(100)  # Perform Turtle actions directly within the button function

tk_button = tk.Button(root, text="Move Turtle", command=button_action)
tk_button.pack()  # Place the button within the Tkinter window

# Remove turtle.done() as Tkinter handles the main loop
# turtle.done()  # This line was causing the separate window

def get_array_elements():
    array_elements = []
    while True:
        element = tk.simpledialog.askstring("Enter Array Element", "Enter an element (or press Cancel to finish):")
        if element is None:  # User canceled
            break
        try:
            element = float(element)  # Attempt to convert to float (modify if needed)
            array_elements.append(element)
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Please enter a valid number.")

    message = "You entered: " + ", ".join(str(x) for x in array_elements)
    tk.messagebox.showinfo("Array Elements", message)

# Create a button to trigger the input process
input_button = tk.Button(root, text="Enter Array Elements", command=get_array_elements)
input_button.pack()

#root.mainloop()  # Start the Tkinter event loop to handle interactions#

import tkinter as tk

# ... your existing Tkinter code, including window creation and layout ...

# Entry box for array elements
array_entry = tk.Entry(root, width=30)
array_entry.pack()  # Place the entry box within your layout

# Label for displaying messages
message_label = tk.Label(root, text="")
message_label.pack()  # Place the label below the entry box

# Function to handle array input and display messages
def get_array_elements():
    element_string = array_entry.get()
    try:
        array_elements = [float(value) for value in element_string.split(",")]
        # ... Process or store the array as needed ...
        message = "You entered: " + ", ".join(str(x) for x in array_elements)
        message_label.config(text=message)
    except ValueError:
        message_label.config(text="Invalid input. Please enter comma-separated numbers.", foreground="red")

# Button to trigger input and message display
input_button = tk.Button(root, text="Enter Array Elements", command=get_array_elements)
input_button.pack()  # Place the button within your layout

# Function to create a rounded button with specified text and command
def create_rounded_button(text, command):
    button = tk.Button(root, text=text, command=command, width=15, height=2)  # Adjust width and height as needed
    button.config(
        relief="flat",  # Remove default border
        bg="skyblue",  # Set background color
        activebackground="lightblue",  # Set color on hover
        fg="white",  # Set text color
        font=("Arial", 10, "bold")  # Set font style
    )
    button.bind("<Enter>", lambda event: button.config(bd=3))  # Add border on hover
    button.bind("<Leave>", lambda event: button.config(bd=0))  # Remove border on leave
    return button


root.mainloop()
