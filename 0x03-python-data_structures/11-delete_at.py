#!/usr/bin/pytho3

def delete_at(my_list=[],idx=0):
    """delete an item at a specific position in a lis
t"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del(my_list[idx])
        return my_list