from collections import deque
import datetime

class Graph:
    print("Traversal path is : ")
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            'S': 14,
            'A': 7,
            'B': 10,
            'C': 4,
            'D': 2,
            'E': 4,
            'G': 0
        }
        return H[n]  

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited 
        # closed_list is a list of nodes which have been visited
       
        open_list = set([start_node])
        closed_list = set([])
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

       
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    
                    n = v

            if n is None:
                print('Path does not exist!')
                return None
            
            if n is stop_node:
                print(n)
                
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

          
            for (m, weight) in self.get_neighbors(n):
          
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

           
            print(n)
            open_list.remove(n)
            closed_list.add(n)
       
        
        print('Path does not exist!')
        return None
    

adjacency_list = {
    'S': [('A', 6), ('B', 5), ('C', 10)],    
    'A': [('D', 6)],
    'B': [('D', 6), ('E', 7)],
    'C': [('E', 6)],
    'D': [('C', 4), ('G', 4)],
    'E': [('A', 3), ('G', 6)]
    }    
     


t0 = datetime.datetime.now()
graph1 = Graph(adjacency_list)

graph1.a_star_algorithm('S', 'G')
t1 = datetime.datetime.now()
t= t1-t0
print("Time difference is ",t.microseconds) 
 

