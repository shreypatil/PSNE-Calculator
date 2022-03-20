import numpy as np

# import tracemalloc
# import time

#################################################################
# For performance

# def tracing_start():

#     tracemalloc.stop()
#     print("nTracing Status : ", tracemalloc.is_tracing())
#     tracemalloc.start()
#     print("Tracing Status : ", tracemalloc.is_tracing())

# def tracing_mem():

#     first_size, first_peak = tracemalloc.get_traced_memory()
#     peak = first_peak/(1024*1024)
#     print("Peak Size in MB - ", peak)

#################################################################


def get_input():
    
    player_count = int(input().strip())
    
    strat_count = input().strip().split(' ')
    assert len(strat_count) == player_count, "Number of strategies must be specified for each Player"
    
    element_count = player_count
    dim = []
    transpose_axes = []
    matrix_dtype = ""

    for idx, val in enumerate(strat_count) :
        dim.append(int(val))
        transpose_axes.append(idx)
        element_count *= int(val)
        matrix_dtype += "f,"

    dim.reverse()
    transpose_axes.reverse()
    # print(transpose_axes)
    

    elements = input().strip().split(' ')
    assert len(elements) == element_count, " Incorrect number of Utilities Provided"
    
    matrix_sz = element_count // player_count
    
    strat_matrix = np.empty(matrix_sz, dtype=matrix_dtype[:-1])
    # print(strat_matrix.dtype)

    i = 0
    while i < matrix_sz :
        j = i*player_count
        strat_matrix[i] = tuple(np.float_(elements[j:j+player_count]))
        i += 1
    
    reshaped = strat_matrix.reshape(tuple(dim))
    return reshaped.transpose(transpose_axes), player_count

#################################################################

def disp_vwds(utility_for_player):
    """Function displays very weakly dominant strategies (given utilities for this player)"""
    
    max_array = np.max(utility_for_player, axis=0)
    # print(max_array)

    vwds_array = []
    for index in range(len(utility_for_player)):
        if (max_array == utility_for_player[index]).all():
            vwds_array.append(index)
    
    print(len(vwds_array), end=" ")

    for index in vwds_array:
        print(index + 1, end = " ")

    print()

def vwds(utility_matrix, player_count):
    """Finds and displays very-weakly dominant strategies for each player"""

    offset = 0

    for i in range(player_count):
        transpose_axes = [i]
        for j in range(0, i):
            transpose_axes.append(j)
        for j in range(i + 1, player_count):
            transpose_axes.append(j)

        disp_vwds(utility_matrix.getfield("f", offset).transpose(transpose_axes))

        offset += 4


#################################################################
# PSNE Calculation

def replace_at_index(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix+1:]




def ismax(matrix, idx, pos, axis) :
    
    for i in range(matrix.shape[axis]) :
        # replace_idx = len(matrix.shape) - axis - 1
        jj = replace_at_index(idx, axis, i)
        if matrix[jj][pos] > matrix[idx][pos] :
            return False
        
    return True


     

def psne(matrix, player_count) :
    
    psnes = set()
    temp = set()
    
    for idx, _ in np.ndenumerate(matrix) :
        
        if ismax(matrix=matrix, idx=idx, pos=0, axis=0) :
            psnes.add(idx)
            
    
    for axis in range(1, player_count) :
        
        for idx in psnes :
            if ismax(matrix=matrix, idx=idx, pos=axis, axis=axis) :
                temp.add(idx)
        
        psnes = temp
        temp = set()
        
        
    return psnes

def print_psnes(psnes: set) :
    
    print(len(psnes))
    
    for psne in psnes : 
        sarr = [str(a + 1) for a in psne]
        print(' '.join(sarr))


#################################################################
def main() :
    
    # tracing_start()
    # start = time.time()


    utility_matrix, player_count = get_input()
    print_psnes(psne(matrix=utility_matrix, player_count=player_count))
    vwds(utility_matrix, player_count)
    

    # end = time.time()
    # tracing_mem()
    # print("time elapsed {} milli seconds".format((end-start)))

if __name__ == '__main__':
    main()
    
