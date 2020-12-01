import numpy as np
import pandas as pd
a = pd.read_csv('.././a.csv').to_numpy(dtype='int', na_value=-1)
for t in a:
    for b in a:
        for c in a:
            if t[0] + b[0] + c[0] == 2020:
                x = t[0]*b[0]*c[0]
print (x)
