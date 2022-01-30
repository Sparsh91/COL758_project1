import numpy as np
import sys
"""
    A graph generator that takes two inputs n and p with p in [1/n , 1]
    It outputs m in the first line the number of edgese and then every line it will print 
    an edge u,v denoting u -> v
"""
def G(n,p):
    edges = []
    file1 = open("g1.txt", "w")
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue
            has_an_edge = np.random.binomial(1,p)
            if(has_an_edge):
                edges.append((i,j))
    file1.write(str(n))
    file1.write('\n')
    file1.writelines(str(len(edges)))
    file1.write('\n')
    for i in edges:
        file1.writelines(str(i[0])+" "+str(i[1]))
        file1.write('\n')
    file1.close()
    return
# n = int(sys.argv[1])
# p = float(sys.argv[2])
# G(n,p)
