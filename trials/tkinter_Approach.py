import turtle
import tkinter as tk

root = tk.Tk()  # Create the main Tkinter window
root.resizable(0,0)

canvas = tk.Canvas(root, width=600, height=400)
  # Display the canvas within the Tkinter window

# Entry box for array elements
array_entry = tk.Entry(root, width=30)

# Label for displaying messages
message_label = tk.Label(root, text="")

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
input_button = tk.Button(root, text="Enter To Continue ...", command=get_array_elements)

# ... rest of your Tkinter code ...

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

def  Bubble():
    pass

def Selection():
    pass

def Merge():
    pass

def Radix():
    pass

def Heap():
    pass

def Quick():
    pass

def Insertion():
    pass

def Counting():
    pass

def Bucket():
    pass


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

canvas.grid(row=0,column=1)

array_entry.grid(row=1,column=1)  # Place the entry box within your layout
input_button.grid(row=2, column=1)
message_label.grid(row=3,column=1)  # Place the label below the entry box

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btn2.grid(row=5,column=0)
btn4.grid(row=5,column=1)
btn6.grid(row=5,column=2)
btn3.grid(row=6,column=0)
btn6.grid(row=6,column=1)
btn9.grid(row=6,column=2)

if __name__=="__main__":
    print(root.winfo_width())
    root.mainloop()

