import matplotlib.pyplot as plt
import numpy as np

#Takes in the initial large array, and the number of vals wanted in the returned array.
#Will delete extra vals off end if remainder present

#need to implement
#need to update code to work without locInList
def avg(lst: list[int]):
    return sum(lst)/len(lst)

def shorten_list_to_averages(large_lst, num_vals_wanted):
    initial_arr_length = len(large_lst)
    group_size_to_avg = int(len(large_lst)/num_vals_wanted)

    shortened_lst = []
    for i in range(0, initial_arr_length, group_size_to_avg):
        sub_lst_to_avg = large_lst[i:i + group_size_to_avg]
        average = avg(sub_lst_to_avg)
        shortened_lst.append(average)
    return shortened_lst


#Alternate methods, fuck around and find out

#METHOD 1


#METHOD 2
#final_lst = [avg(large_lst, inc, i) for i in large_lst[0:len(large_lst)-inc:inc]]


