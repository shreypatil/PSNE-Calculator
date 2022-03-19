import numpy as np
import tracemalloc
import time

#################################################################
# For performance

def tracing_start():

    tracemalloc.stop()
    print("nTracing Status : ", tracemalloc.is_tracing())
    tracemalloc.start()
    print("Tracing Status : ", tracemalloc.is_tracing())

def tracing_mem():

    first_size, first_peak = tracemalloc.get_traced_memory()
    peak = first_peak/(1024*1024)
    print("Peak Size in MB - ", peak)

#################################################################


def get_input():
    
    player_count = int(input().strip())
    
    strat_count = input().strip().split(' ')
    assert len(strat_count) == player_count, "Number of strategies must be specified for each Player"
    
    element_count = player_count
    dim = [player_count]
    transpose_axes = [player_count]

    for idx, val in enumerate(strat_count) :
        dim.append(int(val))
        transpose_axes.append(idx)
        element_count *= int(val)

    dim.reverse()
    transpose_axes.reverse()

    elements = input().strip().split(' ')
    assert len(elements) == element_count, " Incorrect number of Utilities Provided"
    
    strat_matrix = np.empty(element_count)
    
    for idx, val in enumerate(elements) :
        strat_matrix[idx] = float(val)
    
    reshaped = strat_matrix.reshape(tuple(dim))
    return reshaped.transpose(transpose_axes), player_count, strat_count

def disp_vwds(utility_for_player):
    """Function displays very weakly dominant strategies (given utilities for this player)"""
    strat = None
    other_weak_dom = None

    for i in range(len(utility_for_player)):    
        if strat is None:
            strat = i
            other_weak_dom = [] # Clear 
            continue

        if (utility_for_player[strat] >= utility_for_player[i]).all():
            if (utility_for_player[strat] == utility_for_player[i]).all():
                other_weak_dom.append(i)
            else:
                continue
        elif (utility_for_player[strat] <= utility_for_player[i]).all():
            if (utility_for_player[strat] == utility_for_player[i]).all():
                other_weak_dom.append(i)
            else:
                strat = i
                other_weak_dom = []
        else:
            strat = None
    
    if strat is None:
        print(0)
        return
    
    # other_weak_dom.append(strat)
    print(len(other_weak_dom) + 1, strat + 1, sep=" ", end=" ")
    
    for strategy in other_weak_dom:
        print(strategy + 1, end = " ")

    print()

def vwds(utility_matrix, player_count):
    """Finds and displays very-weakly dominant strategies for each player"""

    slice_string = ""
    for _ in range(player_count):
        slice_string += ":,"

    for i in range(player_count):
        transpose_axes = [i]
        for j in range(0, i):
            transpose_axes.append(j)
        for j in range(i + 1, player_count):
            transpose_axes.append(j)

        disp_vwds(eval(f"utility_matrix[{slice_string} i]").transpose(transpose_axes))

    # disp_vwds(utility_matrix[:,:,0])
    # disp_vwds(utility_matrix[:,:,:,0])
    # disp_vwds(utility_matrix[:,:,:,1].transpose((1,0,2)))
    # disp_vwds(utility_matrix[:,:,:,2].transpose((2,0,1)))

    # print(utility_matrix[:,:,1])

    # strategy_matrix_for_player(utility_matrix, player_count, strat_count, 1, slice_string)

def main() :
    
    tracing_start()
    start = time.time()

    utility_matrix, player_count, strat_count = get_input()
    print(utility_matrix)
    vwds(utility_matrix, player_count)

    end = time.time()
    tracing_mem()
    print("time elapsed {} milli seconds".format((end-start)*1000))

if __name__ == '__main__':
    main()
    