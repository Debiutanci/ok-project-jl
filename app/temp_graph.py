from collections import defaultdict
  

class TempGraph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.all_paths = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def print_all_paths_util(self, u, d, visited, path):
        visited[u]= True
        path.append(u)
        if u == d:
            self.paths.append(path)
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    self.print_all_paths_util(i, d, visited, path)
        path.pop()
        visited[u]= False

    def print_all_paths(self, s, d):
        visited = [False]*(self.v)
        path = []
        self.print_all_paths_util(s, d, visited, path)
        return self.all_paths
  

# g = TempGraph(4)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(2, 0)
# g.addEdge(2, 1)
# g.addEdge(1, 3)
# s = 2 ; d = 3
# print ("Following are all different paths from % d to % d :" %(s, d))
# g.printAllPaths(s, d)
