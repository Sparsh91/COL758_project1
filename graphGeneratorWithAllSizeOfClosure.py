import sys

def graph(n):
    edges = []
    for i in range(n-1):
        edges.append((i,i+1))
    print(len(edges))
    for i in edges:
        print(i[0],i[1])

graph(int(sys.argv[1]))