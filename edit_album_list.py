#!/usr/bin/env python3

def edit():
    choice = (input("Options: add:album, remove:album, display\nWhat would you like to do? "))

    if choice[:3] == 'add':

        print("Enter done when you are finished adding albums (no need for add: prefix)")
        album_file = open("albums.txt", 'a')
        album_to_add = choice[4:]
        album_file.write(album_to_add + '\n')

        while 1:

            next_a = input()
            if next_a == 'done':
                break

            album_file.write(next_a + '\n')

    elif choice[:7] == 'display':

        album_file = open("albums.txt")
        for line in album_file:
            print(line)

    else:
        print("NOT YET SUPPORTED, EXITING")
        album_file = open("albums.txt")
        line_list = []
        for line in album_file:
            line_list.append(line)

    album_file.close()
    return
