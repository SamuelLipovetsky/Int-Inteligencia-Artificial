from collections import deque
from copy import deepcopy
class breadthFirst():
    
    def __init__(self, start,end,size):
        # self.graph =graph
        self.start =start
        self.end =end
        self.graph = {}
        self.generatePermutationsList(size)
        self.populateAdjList(start)

        print(self.permList)

    def generatePermutationsList(self, size):
        self.permList = []
        for i in range(size):
            for j in range(i+1, size):
                self.permList.append((i, j, 2 if j-i == 1 else 4))

    # Use the swap list to generate all possible permutations of any list and populates the Adj list
    def populateAdjList(self, list):
        if list not in self.graph.keys():
            self.graph[list] = {}
        for i in self.permList:
                    a,b,c = i
                    split_list = list.split(',')
                    if split_list[b] ==split_list[b]:
                        swap_list = self.swap(split_list, a, b)
                        swap_string_list = ','.join(str(x) for x in swap_list)
                        self.graph[list][swap_string_list]=c
                   
        # simple swap function
    def swap(self, list, a, b):
        # needs to copy bc python always pass immutable objs as refence
        list = deepcopy(list)
        if  1==1:
            temp = list[a]
            list[a] = list[b]
            list[b] = temp
            return list
        return list

    def getPath(self):
        queue = deque([self.start])
        visited = {self.start: None}
        # print(self.start,self.end)
        while len(queue)>0:
        
            v = queue.popleft()
            self.populateAdjList(v)
            if v == self.end:
                path = []
                while v is not None:
                    path.append(v)
                    v = visited[v]
                #goes over path list and sum all the distances
                self.size = sum(self.graph[path[i]][path[i+1]] for i in range(len(path)-1))
                self.path = path[::-1] 
                return
        
            for i in self.graph[v].keys():

                neighbor = i
                if neighbor not in visited:

                    visited[neighbor] = v
                    queue.append(neighbor)
        

    
    def printPath(self, printPath):
        # print(self)
        print(self.size ,len(self.path)-1)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",",""))

