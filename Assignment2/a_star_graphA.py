import datetime

# heuristic function with equal values for all nodes
def h(n):
    H = {
        'S': 6,
        'A': 4,
        'B': 3,
        'C': 3,
        'D': 1,
        'G': 0
    }
    return H[n]



class Graph:
    print("Traversal path is : ")
    def __init__(self, adj_list):
        self.adjacency_list = adj_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited
        # closed_list is a list of nodes which have been visited
        open_list = {start_node}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {start_node: 0}

        # parents contains an adjacency map of all nodes
        parents = {start_node: start_node}

        while len(open_list) > 0:
            n = None

          
            for v in open_list:
                if n is None or g[v] + h(v) < g[n] + h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstruction the path from it to the start_node
            if n is stop_node:
                print(n)

                reconstruction_path = []

                while parents[n] != n:
                    reconstruction_path.append(n)
                    n = parents[n]

                reconstruction_path.append(start_node)

                reconstruction_path.reverse()

                print('Path found: {}'.format(reconstruction_path))
                return reconstruction_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
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
    'S': [('A', 3), ('B', 2)],
    'A': [('B', 1), ('D', 5)],
    'B': [('C', 2), ('D', 3)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 1)]
}



t0 = datetime.datetime.now()
graph1 = Graph(adjacency_list)

graph1.a_star_algorithm('S', 'G')
t1 = datetime.datetime.now()
t = t1-t0
print("Time taken is : ", t.microseconds)



