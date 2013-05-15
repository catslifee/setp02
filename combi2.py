import itertools
def combinatoria2(set,n_c):
    perm = itertools.combinations(set, n_c)
    L_perm = []    
    for X in perm:
        L_perm.append(X)  
    print (L_perm)
