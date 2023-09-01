import tkinter as tk


def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to store and display the input and result
screen = tk.StringVar()
screen.set("")

# Entry widget for user inputs
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# button frame
button_frame = tk.Frame(root)
button_frame.pack()

# calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# grid buttons
row, col = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text,
                       padx=20, pady=20, font="lucida 15 bold")
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", click)

# run main event loop
root.mainloop()
