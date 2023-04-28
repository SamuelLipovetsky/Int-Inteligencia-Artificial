from copy import deepcopy
from BreadthFirst import breadthFirst

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
                    self.dict[poped_ele][swap_string_list] = c
                    stack.append(swap_string_list)

    # simple swap function
    def swap(self, list, a, b):
        # needs to copy bc python always pass immutable objs as refence
        list = deepcopy(list)
        temp = list[a]
        list[a] = list[b]
        list[b] = temp
        return list


def main():
    obj = adjacencyDict([1, 2, 3, 4, 5])
    obj.generatePermutationsList(5)

    obj.populateAdjList([1, 2, 3, 4, 5])

    obj1 = breadthFirst(obj.dict, [5, 3, 2, 4, 1])
    print(obj1.search([5, 3, 2, 4, 1], [1, 2, 3, 4, 5]))
    obj1.trace_path('1,2,3,4,5','5,3,2,4,1')


main()
