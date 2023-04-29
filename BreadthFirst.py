from collections import deque

class breadthFirst():
    
    def __init__(self, dict, start,end):
        self.graph =dict
        self.start =start
        self.end =end

    def getPath(self):
        queue = deque([self.start])
        visited = {self.start: None}
        # print(self.start,self.end)
        while len(queue)>0:
        
            v = queue.popleft()
           
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
        print(self.size ,len(self.path)-1)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",",""))

