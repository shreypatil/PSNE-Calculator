import numpy as np

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

def main() :
    
    utility_matrix, player_count, strat_count = get_input()
    print(utility_matrix)

if __name__ == '__main__':
    main()
    