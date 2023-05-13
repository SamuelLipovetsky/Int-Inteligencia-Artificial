import heapq


class greedySearch():

    def __init__(self, dict, start, end):
        self.adj_list = dict
        self.start = start
        self.end = end
        self.path = []
        self.result = []
        self.expasions=0

    def merge(self,arr, left, mid, right):
        i, j = left, mid + 1
        temp = []
        count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count += mid - i + 1
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
            
        while j <= right:
            temp.append(arr[j])
            j += 1
            
        for i in range(left, right+1):
            arr[i] = temp[i - left]
        
        return count

    def mergeSort(self,arr, left, right):
        count = 0
        
        if left < right:
            mid = (left + right) // 2
            count += self.mergeSort(arr, left, mid)
            count += self.mergeSort(arr, mid+1, right)
            count += self.merge(arr, left, mid, right)
    
        return count

    def countInversions(self,arr):
        return self.mergeSort(arr, 0, len(arr)-1)
    
 

    def getPath(self):

        queue = [(0, [self.start])]

        visited = set()

        best_path_cost = {self.start: 0}
        # best_path_cost_return = {self.start: 0}
        best_path = {self.start: [self.start]}

        while queue:

            path_cost, path = heapq.heappop(queue)
            self.expasions+=1
            node = path[-1]

            if node == self.end:
                self.path = path
                self.result =sum(self.adj_list[path[i]][path[i+1]] for i in range(len(path)-1))
                return
            if node not in visited:

                visited.add(node)

                best_path_cost[node] = path_cost
                # best_path_cost_return[node] = path_cost
                best_path[node] = path

                for neighbor, cost in self.adj_list[node].items():
                  
                    inversions_neigh = self.countInversions(neighbor.split(","))
                    heuristic =0

                  
                    # heuristic = (4-(inversions_node-inversions_neigh))
                    # print(inversions_node,inversions_neigh,heuristic)
                    heuristic = inversions_neigh
                    if neighbor not in visited:
                        
                        
                        new_path_cost = path_cost + heuristic
                        
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (new_path_cost, new_path))

                    
                    elif path_cost +heuristic < best_path_cost[neighbor]:

                        best_path_cost[neighbor] = path_cost + heuristic
                        

                        best_path[neighbor] = path + [neighbor]
                      
                        new_path_cost = path_cost +  heuristic
                        new_path = path + [neighbor]
                        heapq.heappush(queue, (new_path_cost, new_path))

        return None

    def printPath(self, printPath):
        print(self.result, len(self.path)-1,self.expasions)
        if printPath:
            for i in self.path:
                print((' '.join(str(x) for x in i)).replace(",", ""))
