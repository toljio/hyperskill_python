import numpy as np

def custom_sum(arg1, arg2):
    if type(arg1) == np.ndarray and type(arg2) == np.ndarray:
        return arg1 + arg2
    elif type(arg1) == list or type(arg2) == list:
        return "One argument is a list"
    else:
        return "Both arguments are lists, not arrays"
