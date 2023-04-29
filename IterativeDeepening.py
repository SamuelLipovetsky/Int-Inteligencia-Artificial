from collections import deque

class iterativeDeepening():
    
    def __init__(self, dict, start,end,size):
        # print(size)
        self.graph =dict
        self.start =start
        self.end =end
        self.bFactor = (size-1)*(size)/2


    def getPath(self):
        for depth in range(1,10000):
            n_nodes=0
            queue = deque([self.start])
            visited = {self.start: None}
            # print(self.start,self.end)    
           
            nodesPerDepth= sum([pow(self.bFactor,i) for i in range(depth)])

            while len(queue)>0 and n_nodes<nodesPerDepth:
                n_nodes+=1
                v = queue.popleft()

                if v == self.end:
                    print(depth,"----")
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
        print(self.size ,len(self.path)-1)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",",""))

