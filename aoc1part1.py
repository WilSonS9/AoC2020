import numpy as np
import pandas as pd
a = pd.read_csv('../a.csv').to_numpy(dtype='int', na_value=-1)
for t in np.nditer(a):
    for b in np.nditer(a):
        if t + b == 2020:
            x = t*b
print (x)
