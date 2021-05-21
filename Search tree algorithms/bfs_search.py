from queue import Queue;
import collections
import datetime



def bsf(t):
    visited = {}
    level = {}
    daddu = {}
    tpath = []
    q = Queue()

    for node in t.keys():
        visited[node] = False
        daddu[node] = None
        level[node] = -1

    s = "S"
    visited[s] = True
    level[s] = 0
    q.put(s)

    while not q.empty():
        u = q.get()
        tpath.append(u)

        for v in t[u]:
            if not visited[v]:
                visited[v] = True
                daddu[v] = u
                level[v] = level[u] + 1
                q.put(v)

    print("Traversal path:- ", tpath)

    v = "G"
    path = []
    while v is not None:
        path.append(v)
        v = daddu[v]
    path.reverse()
    print("Exact Path:- ", path)

t0 = datetime.datetime.now()
#  Graph A
# t = {
#     'S' : ['A', 'B'],
#     'A' : ['B', 'D'], 
#     'B' : ['C', 'D'],
#     'C' : ['G', 'D'],
#     'D' : ['G'], 
#     'G' : []
# }

# graph B  
t = {
    'S' : ['A', 'B', 'C'],
    'A' : ['D'], 
    'B' : ['D', 'E'],
    'C' : ['E'],
    'D' : ['G', 'C'],
    'E' : ['G', 'A'], 
    'G' : []
}

bsf(t)
t1 = datetime.datetime.now()
t = t1-t0
print("Time difference is ",t.microseconds) 