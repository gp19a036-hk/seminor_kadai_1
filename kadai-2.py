import numpy as np
a = np.array((1, 2, 3, 4))
b = np.array((4, 3, 2, 1))

dist = np.sqrt(np.sum(np.square(a-b)))

print(dist)