"""
Task 1
Create an application with a graphical interface that:

Should have a box that says "Enter Name" where the user can enter a name
There should be a button labeled "Confirm" which, when pressed, would cause the program to print "Hello, {name}!" below the field.

Task 2
Improve the program for Task 1 so that it:

Would print a greeting not only when the key was pressed, but also when the Enter key was pressed

Task 3
Create a leave button for the program that when pressed would close the program.
"""

from tkinter import *

# GAME WINDOW CREATION
main_window = Tk()
main_window.geometry("500x500")
main_window.title("This is a program")

# FRAME
top_frame = Frame(main_window)
bottom_frame = Frame(main_window)
left_frame = Frame(main_window)
right_frame = Frame(main_window)


# FUNCTIONS

def print_welcome_message():
    entered = user_name_entry_field.get()
    results["text"] = f"Hello, your name is {entered}"


def print_when_press_enter():
    results["text"] = "'Press ENTER to confirm' functionality not implemented yet. Just press the confirm button."


# OBJECTS


user_name_entry_label = Label(main_window, text="Enter your name: ")
user_name_entry_field = Entry(main_window)
results = Label(main_window, text="")

user_name_print_confirm_button = Button(main_window, text="Confirm", command=print_welcome_message)

main_window.bind("<Return>", lambda event: print_when_press_enter())

leave_button = Button(main_window, text="Leave", command=main_window.destroy)

# PACKING
top_frame.pack()
user_name_entry_label.pack()
user_name_entry_field.pack()
user_name_print_confirm_button.pack()
leave_button.pack(side="bottom", fill=X)
results.pack()

bottom_frame.pack()
left_frame.pack()
right_frame.pack()

# MAIN GAME LOOP

main_window.mainloop()
