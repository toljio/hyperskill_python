# the object_list has already been defined
# write your code here
from collections.abc import Hashable
h = {}
k = 0
for o in object_list:
    if isinstance(o, Hashable):
        if o in h.keys():
            h[o] += 1
        else:
            h[o] = 1
for i in h:
    if h[i] > 1:
        k += h[i]
print(k)
