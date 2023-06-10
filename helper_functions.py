import matplotlib.pyplot as plt
import numpy as np

#Takes in the initial large array, and the number of vals wanted in the returned array.
#Will delete extra vals off end if remainder present

#need to implement
#need to update code to work without locInList
def avg(lst: list[int], inc: int, locInList ):
    return sum(lst[locInList:locInList+inc])/inc

def shorten_list_to_averages(large_lst, num_vals_wanted):
    initial_arr_length = len(large_lst)
    group_size_to_avg = int(len(large_lst)/num_vals_wanted)
    shortened_list = []
    i = 0
    #print("SHIT - ", len(arr)/arrVals_per_val)
    while i+group_size_to_avg <= initial_arr_length:
        shortened_list.append(sum(large_lst[i:i+group_size_to_avg])/group_size_to_avg)
        i += group_size_to_avg
    return shortened_list



#Alternate methods, fuck around and find out
#
#large_lst = list(range(100))
#inc = 5
#METHOD 1
# return_lst = []
# for i in lst[0:len(lst)-inc:inc]:
#     average = avg(lst, inc)
#     return_lst.append(average)
#
#METHOD 2
#final_lst = [avg(large_lst, inc, i) for i in large_lst[0:len(large_lst)-inc:inc]]


