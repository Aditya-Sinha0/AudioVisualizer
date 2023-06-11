import matplotlib.pyplot as plt
import numpy as np

def avg(lst: list[int]):
    return sum(lst)/len(lst)

#Takes in the initial large array, and the number of vals wanted in the returned array.
def shorten_list_to_averages(large_lst, num_vals_wanted):
    initial_arr_length = len(large_lst)
    group_size_to_avg = int(len(large_lst)/num_vals_wanted)

    shortened_lst = [avg(large_lst[i:i + group_size_to_avg]) for i in range(0, initial_arr_length, group_size_to_avg)]
    return shortened_lst

    """ 
    Leaving this here for readability purposes - it is the same as lines 12/13 but without the list comprehension
    shortened_lst = []
    for i in range(0, initial_arr_length, group_size_to_avg):
        sub_lst_to_avg = large_lst[i:i + group_size_to_avg]
        average = avg(sub_lst_to_avg)
        shortened_lst.append(average)
    return shortened_lst
    """

