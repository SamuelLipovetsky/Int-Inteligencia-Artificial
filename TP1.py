from collections import deque
class adjacencyDict():
    def __init__(self,list):
        self.dict={}
        self.list=list

    def generatePermutationsList(self,size):
        self.permList=[]
        for i in range(size):
            for j in range (i+1,size):
                self.permList.append((i,j,2 if j-i==1 else 4))
                
    def populateAdjList(self,list):
        stack = []
        temp_list =list 
        string_list = ','.join(str(x) for x in temp_list)
        stack.append(string_list)
        while len(stack)>0:
            poped_ele =stack.pop()
            poped_list = poped_ele.split(",")
            if poped_ele not in self.dict.keys():
                self.dict[poped_ele]={}
                for i in self.permList:
                    a= i[0]
                    b= i[1]
                    c= i[2]
                    swap_list= self.swap(poped_list,a,b)
                    swap_string_list = ','.join(str(x) for x in swap_list)
                    self.dict[poped_ele][swap_string_list]=c
                    stack.append(swap_string_list)
           

            

                    
    def swap(self,list,a,b):
        
        temp =list[a]
        list[a]=list[b]
        list[b]=temp
        return list


class breadthFirst():
    def __init__(self,dict,start):
        self.dict=dict
        self.start = start
        

    def search(self,start,target):
       
        target = ','.join(str(x) for x in target)
        start = ','.join(str(x) for x in start)
        queue = deque([(start,0)])
        visited= set()
        
        while len(queue)>0:
            node ,d =queue.popleft()
          
            if node in visited :
                continue
            visited.add(node)
            if node == target:
                return d
            
            print(self.dict[node])
            for i in self.dict[node].keys():
              
                    queue.append((i, self.dict[node][i]))


def main():
    obj = adjacencyDict([3,4,5])
    obj.generatePermutationsList(3)
    obj.populateAdjList([3,4,5])
    # print(obj.dict)
    # print(len(obj.dict.keys()))
    # for i in obj.dict.keys():
    #     print(obj.dict[i])
      
      
    obj1 =breadthFirst(obj.dict,[5,4,3])
    print(obj1.search([5,4,3],[3,4,5]))

main()