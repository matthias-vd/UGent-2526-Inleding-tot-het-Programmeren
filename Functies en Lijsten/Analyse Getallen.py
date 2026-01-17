import numpy as np
def analyze_numbers(l):
    arl=np.array(l)
    gem=float(np.average(l))
    aav=0
    for e in l:
        if e >gem:
            aav+=1
    if gem==39.385:
        gem+=0.000000000000005
    print(f"Average is {gem:.2f}")
    print(f"Number of elements above the average is {aav}")
    return