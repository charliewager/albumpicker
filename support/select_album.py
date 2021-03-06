#!/usr/bin/env python3

import random


def select_album():
    albums_file = open("list.txt")

    album_list = []
    for line in albums_file:
        album_list.append(line)

    length = len(album_list)
    if length == 0:
        return "ADD ITEMS TO THE LIST FIRST"

    random.seed()
    idx = random.randint(0, (length - 1))

    albums_file.close()

    item = album_list[idx]
    dashIDX = item.rfind('-')
    if dashIDX > 35:
        firstHalf = item[:(dashIDX - 1)]
        secondHalf = item[(dashIDX + 1):]
        return firstHalf + '\n' + secondHalf

    return album_list[idx]
