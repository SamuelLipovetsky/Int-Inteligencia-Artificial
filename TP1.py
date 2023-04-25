

import sys
sys.setrecursionlimit(15000000)
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
                    self.dict[string_list][swap_string_list]=c
                    stack.append(swap_string_list)
                    
    def swap(self,list,a,b):
        
        temp =list[a]
        list[a]=list[b]
        list[b]=temp
        return list




def main():
    obj = adjacencyDict([1,2,3,4,5,5,6,7,8])
    obj.generatePermutationsList(8)
    obj.populateAdjList([1,2,3,4,5,6,7,8])
    print(len(obj.dict.keys()))
    # print(obj.dict)
    print(obj.permList)

main()