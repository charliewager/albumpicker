#!/usr/bin/env python3

import select_album
import edit_album_list


def main():
    while 1:
        choice = input("What would you like to do?\nEnter 1 for your album selection or 2 to edit album list: ")

        if int(choice) == 1:

            album = select_album.select_album()
            print(album)

        elif int(choice) == 2:

            edit_album_list.edit()

        else:
            print("Please enter 1 or 2, program will now quit")

        timetogo = input("Would you like to exit? (yes/no): ")
        if timetogo == 'yes':
            exit(0)


if __name__ == "__main__":
    main()
