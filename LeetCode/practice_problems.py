import pandas as pd
import numpy as np

x = [1, 5, 9, 0]
y = [3, 0, 2, 9]

def calc_intersection(list_1, list_2):
    return set(list_1).intersection(set(list_2))

if __name__ == '__main__':
    result = calc_intersection(x,y)
    print(result)
    print(type(result))