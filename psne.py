import numpy
import sys

from inout import get_data_from


def main() :
    
    assert len(sys.argv) == 2, "Must have exactly 1 File Path"
    matrix = get_data_from(sys.argv[1])
    print(matrix)

if __name__ == '__main__':
    main()
    