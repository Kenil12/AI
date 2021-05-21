import datetime
t0 = datetime.datetime.now()
# graph A
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


p = list()
print("\nTRAVERSAL PATH:- ")
def DFS(node,dpe,t,md,colist):
    print(node)
    colist.append(node)
    if node==dpe:
        return True
    if md<=0:
        p.append(colist)
        return False
    for node in t[node]:
        if DFS(node,dpe,t,md-1,colist):
            return True
        else:
            colist.pop()
    return False

def iterativeDDFS(node,dpe,t,md):
    for i in range(md):
        colist = list()
        if DFS(node,dpe,t,i,colist):
            return True
    return False

if not iterativeDDFS('S','G',t,4):
    print("Path is not available")
else:
    print("\n\nexact:- ")
    print(p.pop())

t1 = datetime.datetime.now()
t = t1-t0
print("Time difference is ",t.microseconds) 