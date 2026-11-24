import tkinter as tk

#Creating the Main Window
window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="white")

#Creating a Variable for the Expression
expression = ""

#Creating the Calculator Display
display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="#f0f0f0",
    fg="black",
    insertbackground="black",
    justify="right",
    bd=1,
    relief="solid"
)
display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=20
)

#Creating a Function for Keyboard Input Validation
def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"

#Synchronizing the Display and Expression Variable
def sync_expression(event):
    global expression
    expression = display.get()

#Connecting Keyboard Events
display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)

#Creating the Button Click Function
def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

#Creating the Clear Function
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

#Creating the Calculate Function
def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""

#Creating a Two-Dimensional List for the Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"]
]

#Creating a Frame
button_frame = tk.Frame(
    window,
    bg="white"
)
button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)

#Creating the Clear Button
clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18, "bold"),
    bg="#9b111e",  # Ruby red color
    fg="white",    # White text
    bd=0,
    command=clear
)
clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)

# Making and Positioning Buttons Using Nested
for row_index, row in enumerate(buttons, start=1):
    for col_index, value in enumerate(row):
        if value == "=":
            command = calculate
            color = "#00a86b"
            text_color = "white"
        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#ff9500"
            text_color = "white"
        else:
            command = lambda v=value: button_click(v)
            color = "#000080"  # Navy blue background for number buttons
            text_color = "white" # White numbers and text
            
        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg=text_color,
            bd=0,
            command=command
        )
        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

#Configuring Grid Rows and Columns
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
 
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

#Running the Application
window.mainloop()
