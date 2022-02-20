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
        back.grid_forget()

    def add_arrange():
        display.pack()
        textFrame.pack(pady=100)
        scroll.pack_forget()
        txt.pack_forget()
        display.configure(text="What would you like to add?\n(please provide album names in a name - artist format)",
                          font=("Arial", 15))
        choice2.configure(text="Add", width=3, command=add_act)
        usrbox.grid(row=1, column=1, padx=10)
        choice1.grid_forget()
        choice2.grid(row=1, column=2, padx=10)
        choice3.grid_forget()
        back.configure(command=editList)
        back.grid(row=1, column=3)


    def add_act():
        display.pack()
        textFrame.pack(pady=100)
        scroll.pack_forget()
        txt.pack_forget()
        toAdd = usrbox.get()
        edit_album_list.add(toAdd)
        usrbox.delete(0, END)
        display.configure(text="Added " + toAdd, font=("Arial", 12))
        usrbox.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        back.configure(command=editList)
        back.grid(row=1, column=3)


    def remove_arrange():
        display.configure(text="What would you like to remove?\n(please provide album names in a name - artist format)",
                          font=("Arial", 15))
        choice2.configure(text="Remove", width=7, command=remove_act)
        usrbox.grid(row=1, column=1, padx=10)
        choice1.grid_forget()
        choice2.grid(row=1, column=2, padx=10)
        choice3.grid_forget()
        back.configure(command=editList)
        back.grid(row=1, column=3)

    def remove_act():
        toRemove = usrbox.get()
        edit_album_list.remove(toRemove)
        usrbox.delete(0, END)
        display.configure(text="Removed " + toRemove, font=("Arial", 12))
        choice2.configure(text="Remove", width=7)
        usrbox.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        back.configure(command=editList)
        back.grid(row=1, column=3)

    def show_all():
        choice3.grid_forget()
        choice1.grid(row=1, column=1, padx=10)
        back.grid(row=1, column=2, padx=10)
        choice2.grid(row=1, column=3, padx=10)
        back.configure(command=editList)
        scroll.pack(side=RIGHT, fill=Y)
        display.pack_forget()
        textFrame.pack(pady=10)
        buttonFrame.pack(pady=10)
        txt.pack()
        txt.insert(END, edit_album_list.display())

    def makeSelection():
        display.configure(text=select_album.select_album())

    def editList():
        display.pack()
        textFrame.pack(pady=100)
        display.configure(text="What would you like to do to the list?")
        choice1.configure(text="Add an item", width=16, command=add_arrange)
        choice2.configure(text="Remove an item", width=16, command=remove_arrange)
        choice1.grid(row=1, column=1, padx=10)
        choice2.grid(row=1, column=2, padx=10)
        choice3.grid(row=1, column=3, padx=10)
        scroll.pack_forget()
        back.configure(command=original)
        back.grid(row=2, column=2, pady=10)
        usrbox.grid_forget()
        scroll.pack_forget()
        txt.pack_forget()

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
    choice3 = Button(buttonFrame, text="View it", width=16, bg="#E6D4A3", command=show_all)
    choice1.grid(row=1, column=1, padx=10)
    choice2.grid(row=1, column=2, padx=10)
    usrbox = Entry(buttonFrame, width=30, bg="#E6D4A3", )
    back = Button(buttonFrame, text="Back", bg="#E6D4A3", width=6)
    scroll = Scrollbar(textFrame, troughcolor ="#E6D4A3")
    txt = Text(textFrame, yscrollcommand=scroll.set, height=15, fg="#E6D4A3", bg="#1E1E1E", bd=0)
    scroll.configure(command=txt.yview)

    root.mainloop()


if __name__ == "__main__":
    main()
