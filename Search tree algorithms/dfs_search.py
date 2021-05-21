import datetime

def dfs(t):
    c = {}
    p = {}
    output = []
    for node in t.keys():
        c[node] = "W"
        p[node] = None
        trav_time = [-1, -1]
    def dfs_u(u):
        c[u] = "G"
        output.append(u)

        for v in t[u]:
            if c[v] == "W":
                p[v] = u
                dfs_u(v)
        c[u] = "B"
    dfs_u("S")
    print(output)
    v = "G"
    path = []

    while v is not None:
        path.append(v)
        v = p[v]
    path.reverse()
    print (path)
t0 = datetime.datetime.now()
#graph A
# t = {
#     "A":["B", "D"],
#     "B":["C", "D"],
#     "C":["D", "G"],
#     "D":["G"],
#     "G":[],
#     "S":["A", "B"]
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

print("Both traversal path and exact path are shown below respectively:- ")
dfs(t)
t1 = datetime.datetime.now()
t = t1-t0
print("Time difference is ",t.microseconds) 