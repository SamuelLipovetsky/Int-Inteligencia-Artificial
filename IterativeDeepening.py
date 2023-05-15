from collections import deque


class iterativeDeepening():

    def __init__(self, dict, start, end):
        self.graph = dict
        self.start = start
        self.end = end
        self.expansions = 0

    def getPath(self):

        for depth in range(2, 1000):
            queue = deque([self.start])
            visited = {self.start: [None, 0]}
            while len(queue) > 0:

                v = queue.popleft()
                self.expansions += 1
                if v == self.end:
                    path = []
                    while v is not None:
                        path.append(v)
                        v = visited[v][0]

                    self.size = sum(self.graph[path[i+1]][path[i]]
                                    for i in range(len(path)-1))
                    self.path = path[::-1]
                    return
                if visited[v][1] < depth:
                    for i in self.graph[v].keys():
                        neighbor = i
                        if neighbor not in visited:
                            visited[neighbor] = [v, visited[v][1]+1]
                            queue.append(neighbor)

    def printPath(self, printPath):
        print(self.size, len(self.path)-1)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",", ""))
