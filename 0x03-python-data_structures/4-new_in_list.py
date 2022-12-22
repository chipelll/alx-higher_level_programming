#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return (my_new_list)
    for i, v in enumerate(my_list):
        if i == idx:
            my_new_list[idx] = element
            return (my_new_list)
