from collections import deque


class breadthFirst():
    def __init__(self, dict, start):
        self.dict = dict
        self.start = start
        self.path ={}

    def search(self, start, target):

        target = ','.join(str(x) for x in target)
        start = ','.join(str(x) for x in start)
        queue = deque([(start, 0)])
        visited = set()

        while len(queue) > 0:

            node, d = queue.popleft()

            if node in visited:
                continue
            visited.add(node)
            if node == target:
                return d
            
            for i in self.dict[node].keys():
                if i not in visited:
                    self.path[i]= node
                queue.append((i, d+self.dict[node][i]))

    def trace_path(self,start,target):
        tracer = target
        # print(self.path['1,2,3,4,5'])
        # print(self.path['5,2,3,4,1'])
        # print(self.path[''])
        # print(self.path['4,2,3,5,1'])
        while tracer!=start:
            print(tracer)
            tracer=self.path[tracer]
            
