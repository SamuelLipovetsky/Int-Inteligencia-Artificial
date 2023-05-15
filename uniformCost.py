import heapq


class uniformCostSearch():

    def __init__(self, dict, start, end):
        self.adj_list = dict
        self.start = start
        self.end = end
        self.path = []
        self.result = []
        self.expansions = 0

    def getPath(self):

        queue = [(0, [self.start])]

        visited = set()

        best_path_cost = {self.start: 0}

        best_path = {self.start: [self.start]}

        while queue:

            path_cost, path = heapq.heappop(queue)
            self.expansions += 1
            node = path[-1]

            if node == self.end:
                self.path = path
                self.result = path_cost
                return

            if node not in visited:

                visited.add(node)

                best_path_cost[node] = path_cost
                best_path[node] = path

                for neighbor, cost in self.adj_list[node].items():
                    if neighbor not in visited:

                        new_path_cost = path_cost + cost
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (new_path_cost, new_path))
                    elif path_cost + cost < best_path_cost[neighbor]:

                        best_path_cost[neighbor] = path_cost + cost
                        best_path[neighbor] = path + [neighbor]

                        new_path_cost = path_cost + cost
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (new_path_cost, new_path))

        return None

    def printPath(self, printPath):
        print(self.result, len(self.path)-1)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",", ""))
