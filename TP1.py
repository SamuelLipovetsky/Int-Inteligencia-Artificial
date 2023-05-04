from copy import deepcopy
from BreadthFirst import breadthFirst
from IterativeDeepening import iterativeDeepening
import time
import sys 
# This class generates a dictionary that works as an adjacency List
class adjacencyDict():
    def __init__(self, list):
        self.dict = {}
        self.list = list

    # generates a list that represents what elements needs to be swaped
    def generatePermutationsList(self, size):
        self.permList = []
        for i in range(size):
            for j in range(i+1, size):
                self.permList.append((i, j, 2 if j-i == 1 else 4))

    # Use the swap list to generate all possible permutations of any list and populates the Adj list
    def populateAdjList(self, list):
        stack = []
        temp_list = list
        #python cannot hash lists , so all lists are treated as strings when necessary 
        string_list = ','.join(str(x) for x in temp_list)
        stack.append(string_list)
        while len(stack) > 0:
            poped_ele = stack.pop()
            poped_list = poped_ele.split(",")
            if poped_ele not in self.dict.keys():
                self.dict[poped_ele] = {}
                for i in self.permList:
                    a,b,c = i
                    swap_list = self.swap(poped_list, a, b)
                    swap_string_list = ','.join(str(x) for x in swap_list)
                    self.dict[poped_ele][swap_string_list]=c
                    stack.append(swap_string_list)
        

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


def main():

    algType = sys.argv[1]
    size = int(sys.argv[2])
    start =[]
    
    for i in range(3,int(size)+3):
        start.append(sys.argv[i])
    
    # adjList = adjacencyDict( start)
    # adjList.generatePermutationsList(size)
    # adjList.populateAdjList(start)

    if algType=="B":
        start_ = time.time()
        obj = breadthFirst(','.join(str(x) for x in start), ','.join(str(x) for x in sorted(start)),len(start))
        obj.getPath()
        obj.printPath( sys.argv[-1] =="PRINT")
        end_ = time.time()
        print(end_ - start_)
    
    # if algType=="I":
    #     start_ = time.time()
    #     obj = iterativeDeepening(adjList.dict, ','.join(str(x) for x in start), ','.join(str(x) for x in sorted(start)),size)
    #     obj.getPath()
    #     obj.printPath( sys.argv[-1] =="PRINT")
    #     end_ = time.time()
    #     print(end_ - start_)


main()
