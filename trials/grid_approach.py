
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=1, column=1)
btn5.grid(row=1, column=2)
btn6.grid(row=1, column=3)
btn7.grid(row=2, column=1)
btn8.grid(row=2, column=2)
btn9.grid(row=2, column=3)
btn1.pack(side="top", fill="x")  # Place button1 at the top, expanding horizontally
btn3.pack(side="right",fill="y")#, fill="y")  # Place button3 to the right, expanding vertically
btn2.pack(side="left",expand=True, fill="both", padx=2, pady=2)  # Place button2 to the left, without expansion
# ... and so on for other buttons ...
