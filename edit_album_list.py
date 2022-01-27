#!/usr/bin/env python3

def add():
    print("Enter done when you are finished adding albums (please provide album names in a name - artist format):")
    album_file = open("albums.txt", 'a')

    while 1:

        next_addition = input()
        if next_addition == 'done':
            break

        album_file.write(next_addition + '\n')

    album_file.close()


def remove():

    print("Enter done when you are finished removing albums (provide names in the same format you added them in):")
    album_file = open("albums.txt")
    line_list = []
    for line in album_file:
        line_list.append(line)

    album_file.close()

    to_remove = []
    count = 0
    individual = input()
    while individual != 'done':
        to_remove.append(individual)
        individual = input()

    updated_list = []
    for line in line_list:
        lastIDX = len(line) - 1

        action = 0
        for removal in to_remove:
            if line[:lastIDX] == removal:
                action = 1

        if action == 0:
            updated_list.append(line)
        else:
            count += 1

    i = 0
    for line in updated_list:

        if i == 0:
            album_file = open("albums.txt", "w")
            album_file.write(line)
            album_file.close()

        else:
            album_file = open("albums.txt", "a")
            album_file.write(line)
            album_file.close()

        i += 1

    print("removed ", count, " items in total")


def edit():
    choice = (input("Options: add, remove, display\nWhat would you like to do? "))

    if choice[:3] == 'add':

        add()

    elif choice[:7] == 'display':

        album_file = open("albums.txt")
        for line in album_file:
            print(line)

        album_file.close()

    elif choice[:6]:

        remove()

    else:
        print("please enter either add, remove, or display")
    return
