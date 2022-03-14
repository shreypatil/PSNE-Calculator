import numpy as np


def get_data_from(file_path) :
    
    f = open(file_path, 'r')
    
    lines = f.readlines()
    assert len(lines) == 3, "Input must have 3 lines"
    
    player_count = int(lines[0])
    
    strat_count = lines[1].split(' ')
    assert len(strat_count) == player_count, "Number of strategies must be specified for each Player"
    
    element_count = player_count
    dim = [player_count]
    for i in strat_count :
        dim.append(int(i))
        element_count *= int(i)
    
    elements = lines[2].split(' ')
    assert len(elements) == element_count, " Incorrect number of Utilities Provided"
    
    strat_matrix = np.empty(element_count)
    
    for idx, val in enumerate(elements) :
        strat_matrix[idx] = float(val)
    
    
    return strat_matrix.reshape(tuple(dim))
        
    
    f.close()