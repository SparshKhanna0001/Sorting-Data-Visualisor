'''
sorting_algorithms = ["BubbleSort", "SelectionSort", "MergeSort", "RadixSort", "Heapsort", "QuickSort", "InsertionSort", "CountingSort"]
s = ['Bubble', 'Selection', 'Merge', 'Radix', 'Heap', 'Quick', 'Insertion', 'Counting']

for i in range(len(sorting_algorithms)):
    print(f'btn{i+1} = create_rounded_button("{sorting_algorithms[i]}", {s[i]} )')

print()
print()

z = 0
r = 0
while z < 3:
    for i in range(3):
        print(f'btn{i+r}.grid(row={z}, column={i+1})')
    
    z += 1
    r += 3
'''
'''
btn1.pack(side="left", fill="both", expand=True)  # Place button1 at the top, expanding horizontally
btn3.pack(side="right",fill="y")#, fill="y")  # Place button3 to the right, expanding vertically
btn2.pack(side="left",expand=True, fill="both", padx=2, pady=2)  # Place button2 to the left, 
'''

for i in range(3):
    for j in range(3):
        print(f"btn{(j+1)*(i+1)}.grid(row={i+4},column={j+1})")