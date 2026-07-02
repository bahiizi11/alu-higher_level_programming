#!/usr/bin/python3
"""Module that divides two lists element by element"""


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: the length of the resulting list

    Returns:
        A new list with all divisions
    """
    new_list = []
    for i in range(list_length):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(division)
    return new_list
