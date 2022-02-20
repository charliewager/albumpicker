#!/usr/bin/env python3

from support import select_album, edit_album_list
from tkinter import *


def main():

    def original():
        display.configure(text="What would you like to do?", font=("Arial Bold", 17))
        choice3.grid_forget()
        choice1.configure(text="Make a selection", width=16, command=makeSelection)
        choice2.configure(text="Edit the list", width=16, command=editList)
        choice1.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        back.pack_forget()

    def add_arrange():
        display.configure(text="What would you like to add?\n(please provide album names in a name - artist format)", font=("Arial", 15))
        choice2.configure(text="Add", width=3, command=add_act)
        usrbox.grid(row=1, column=1, padx=10)
        choice1.grid_forget()
        choice2.grid(row=1, column=2, padx=10)
        choice3.grid_forget()
        back.configure(command = editList)

    def add_act():
        toAdd = usrbox.get()
        edit_album_list.add(toAdd)
        usrbox.delete(0, END)
        display.configure(text="Added " + toAdd, font=("Arial", 12))
        usrbox.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        back.configure(command=editList)

    def remove_arrange():
        display.configure(text="What would you like to remove?\n(please provide album names in a name - artist format)", font=("Arial", 15))
        choice2.configure(text="Remove", width=7, command=remove_act)
        usrbox.grid(row=1, column=1, padx=10)
        choice1.grid_forget()
        choice2.grid(row=1, column=2, padx=10)
        choice3.grid_forget()
        back.configure(command = editList)

    def remove_act():
        toRemove = usrbox.get()
        edit_album_list.remove(toRemove)
        usrbox.delete(0, END)
        display.configure(text="Removed " + toRemove, font=("Arial", 12))
        choice2.configure(text= "Remove", width=7)
        usrbox.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        back.configure(command=editList)

    # def show_all():
    #     choice3.grid_forget()
    #     display.pack_forget()
    #     scroll = Scrollbar(textFrame)
    #     scroll.pack(side=RIGHT, fill=Y)
    #     out = Text(textFrame, font=('Arial', 13), bg="White", fg="#E6D4A3", width=54, height= 8, yscrollcommand=scroll.set)
    #     disp = edit_album_list.display()
    #
    #     for el in disp:
    #         out.insert(END, el)



    def makeSelection():
        display.configure(text=select_album.select_album())

    def editList():
        display.configure(text="What would you like to do to the list?")
        choice1.configure(text="Add an item", width = 16, command=add_arrange)
        choice2.configure(text="Remove an item", width = 16, command=remove_arrange)
        choice1.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        choice3.grid(row=1, column=3, padx=10)
        back.configure(command = original)
        back.pack(pady=10)
        usrbox.grid_forget()


    root = Tk()
    root.title("Album Picker")
    root.geometry('550x400')
    root.configure(background="#1E1E1E")
    textFrame = Frame(root, bg="#1E1E1E")
    textFrame.pack(pady=100)
    buttonFrame = Frame(root, bg="#1E1E1E")
    buttonFrame.pack()
    display = Label(textFrame, text="What would you like to do?", font=("Arial Bold", 17), fg="#E6D4A3", bg="#1E1E1E")
    display.pack()
    choice1 = Button(buttonFrame, text="Make a selection", width=16, bg="#E6D4A3", command=makeSelection)
    choice2 = Button(buttonFrame, text="Edit the list", width=16, bg="#E6D4A3", command=editList)
    choice3 = Button(buttonFrame, text="View it", width=16, bg="#E6D4A3")
    choice1.grid(row=1, column=1, padx=10)
    choice2.grid(row=1, column=2, padx=10)
    usrbox = Entry(buttonFrame, width=30, bg="#E6D4A3", )
    back = Button(root, text="Back", bg="#E6D4A3", width = 6)

    root.mainloop()


if __name__ == "__main__":
    main()
