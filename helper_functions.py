import matplotlib.pyplot as plt
import numpy as np

#Takes in the initial large array, and the number of vals wanted in the returned array.
#Will delete extra vals off end if remainder present
def shorten_list_to_averages(arr, num_vals_wanted):
    initial_arr_length = len(arr)
    shortened_list = []
    arrVals_per_val = int(initial_arr_length/num_vals_wanted)

    i = 0
    #print("SHIT - ", len(arr)/arrVals_per_val)
    while i+arrVals_per_val <= initial_arr_length:
        shortened_list.append(sum(arr[i:i+arrVals_per_val])/arrVals_per_val)
        i += arrVals_per_val
    return shortened_list

