import numpy as np


def get_data_from(file_path) :
    
    f = open(file_path, 'r')
    
    lines = f.readlines()
    assert len(lines) == 3, "Input must have 3 lines"
    
    player_count = int(lines[0])
    
    strat_count = lines[1].split(' ')
    assert len(strat_count) == player_count, "Number of strategies must be specified for each Player"
    
    element_count = player_count
    dim = []
    transpose_axes = [player_count]

    for idx, val in enumerate(strat_count) :
        dim.append(int(val))
        transpose_axes.append(idx)
        element_count *= int(val)
    
    dim.append(player_count)
    transpose_axes.reverse()

    elements = lines[2].split(' ')
    assert len(elements) == element_count, " Incorrect number of Utilities Provided"
    
    strat_matrix = np.empty(element_count)
    
    for idx, val in enumerate(elements) :
        strat_matrix[idx] = float(val)
    
    reshaped = strat_matrix.reshape(tuple(dim))
    return reshaped.transpose(transpose_axes)
    
    f.close()