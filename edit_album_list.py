#!/usr/bin/env python3

def edit():

    choice = (input("Options: add:album, remove:album, display\nWhat would you like to do? "))

    if choice[:3] == 'add':
        
        print("Enter done when you are finished adding albums (no need for add: prefix)")
        album_list = open("albums.txt", 'a')
        albm_to_add = choice[4:]
        album_list.write(albm_to_add + '\n')

        while 1:
            
            next_a = input()
            if next_a == 'done':
                break
            
            album_list.write(next_a + '\n')

    elif choice[:7] == 'display':
        
        album_list = open("albums.txt")
        for line in album_list:
            print(line)
            
    else:
        print("NOT YET SUPPORTED, EXITING")

    album_list.close()
    return