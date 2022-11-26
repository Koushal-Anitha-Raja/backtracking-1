#Time_Complexity: O(n)
#Space_Complexity: O(n)
class Solution:

    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
        
        
        
    #for loop based recursion 
        self.result=[]
        #backtrack function
        self.backtrack(candidates,target,0,[])
        #returning the final result
        return self.result
    
    #passing the parameters to function
    def backtrack(self,candidates,currsum,pivot,path):
        #if the target is acheived append it to result
        if currsum==0:
            self.result.append(path[:])
            return
            #if the currsum is les than zero
        if currsum<0 :
            return 
        
       #from the first to last element
        for i in range(pivot,len(candidates)):
            #action
            path.append(candidates[i])
            #recursion
            self.backtrack(candidates,currsum-candidates[i],i,path)
            
            #backtrack
            path.pop()
