"""
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

"""

"""

btn1 = create_rounded_button("BubbleSort", Bubble )
btn2 = create_rounded_button("SelectionSort", Selection )
btn3 = create_rounded_button("MergeSort", Merge )
'''
btn4 = create_rounded_button("RadixSort", Radix )
btn5 = create_rounded_button("Heapsort", Heap )
btn6 = create_rounded_button("QuickSort", Quick )
btn7 = create_rounded_button("InsertionSort", Insertion )
btn8 = create_rounded_button("CountingSort", Counting )
btn9 = create_rounded_button("Bucket Sort", Bucket)
'''
btn1.pack(side="left", fill="both", expand=True)  # Place button1 at the top, expanding horizontally
btn3.pack(side="right",fill="y")#, fill="y")  # Place button3 to the right, expanding vertically
btn2.pack(side="left",expand=True, fill="both", padx=2, pady=2)  # Place button2 to the left, 
"""
"""
sorting_algorithms = ["Bubble", "Selection", "Merge", "Radix", "Heap", "Quick", "Insertion", "Counting"]

def execute_algorithm(algorithm):
    # Function to execute the sorting algorithm
    print(f"Executing {algorithm} Sort")  # Replace this with actual sorting algorithm calls

def create_buttons(root):
    for algorithm in sorting_algorithms:
        button = tk.Button(root, text=algorithm + " Sort", bg="#ed3309", command=lambda algo=algorithm: execute_algorithm(algo))
        button.config(width=10, height=2, borderwidth=0, padx=5, pady=5, relief="flat")
        button.pack(side=tk.LEFT, padx=5, pady=5)

button_frame = tk.Frame(root)
button_frame.pack()

"""
"""
sorting_algorithms = [
    "BubbleSort", "SelectionSort", "MergeSort", 
    "RadixSort", "Heapsort", "QuickSort", 
    "InsertionSort", "CountingSort", "BucketSort"
]

def execute_algorithm(algo_name):
    print(f"Executing {algo_name[:-4]} sort...")  # Exclude "Sort" suffix

def create_buttons(root):
    for algo_name in sorting_algorithms:
        button = tk.Button(
            root,
            text=algo_name[:-4],  # Exclude "Sort" suffix
            bg="#ed3309",
            command=lambda algo=algo_name: execute_algorithm(algo)
        )
        button.configure(width=15, height=2, bd=3, font=("Arial", 10))
        button.pack(side=tk.TOP, padx=5, pady=5)

"""

"""
# Custom function to create and grid rounded buttons
def create_rounded_button(root, row, column, text, command, bg_color):
    canvas = tk.Canvas(root, width=120, height=40, bg=bg_color, bd=0, highlightthickness=0)
    canvas.grid(row=row, column=column, padx=10, pady=5)  # Use grid() for precise placement

    button_id = canvas.create_oval(5, 5, 115, 35, fill=bg_color, outline="")
    canvas.create_text(60, 20, text=text, fill="white", font=("Arial", 12, "bold"))

    def on_click(event):
        command()

    canvas.tag_bind(button_id, "<Button-1>", on_click)
    return canvas

# Create the buttons (replace placeholder functions with your implementations)
sorting_algorithms = ["Bubble", "Selection", "Merge", "Radix", "Heap", "Quick", "Insertion", "Counting"]
for row in range(3):
    for column in range(3):
        index = row * 3 + column
        if index < len(sorting_algorithms):
            algorithm = sorting_algorithms[index]
            create_rounded_button(root, row, column, algorithm, eval(algorithm), "#ed3309")
"""
#create_buttons(root)
#create_buttons(button_frame)
