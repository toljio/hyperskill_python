import copy
obj = [[1, 2, 3], [1,6]]

def detect_copy():
    copy_obj = copying_machine(obj)
    print(obj, copy_obj)
    if copy_obj is copy.copy(copy_obj):
       return 'shallow copy'
    return 'deep copy'