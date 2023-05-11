from heapq import *

class uniformCostSearch():
    
    def __init__(self, dict, start,end):
        self.graph =dict
        self.start =start
        self.end =end
        

    def getPath(self):
        queue = [self.start]
        visited = {self.start: None}
        # print(self.start,self.end)
        while len(queue)>0:
        
            v = heappop(queue)
        
            if v == self.end:
                path = []
                while v is not None:
                    path.append(v)
                    v = visited[v]

                self.size =sum(self.graph[path[i+1]][path[i]] for i in range(len(path)-1))
                
                        # self.size=new_size
                self.path = path[::-1] 
                break
        
            for i in self.graph[v].keys():
                neighbor = i
                if neighbor not in visited:
                    visited[neighbor] = v
                    heappush(queue,neighbor)
                    # queue.append(neighbor)

    
    def printPath(self, printPath):
        print(self.size ,len(self.path)-1)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",",""))
