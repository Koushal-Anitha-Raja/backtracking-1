
#Time_Complexoty: O(n)
#Space_Complexity: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#choooe nochoose
        self.nums = nums # declaring the nums
        self.result = [] # creating the resultant array
        self.backtrack(0,[]) # calling the backtrack function recursively with 0 and empty array
        return self.result # returning the result
    
    def backtrack(self,i,subset):
        if i == len(self.nums): # if i is equal to length of nums
            self.result.append(subset[:]) # appending the subset array into result
            return
        
        self.backtrack(i+1,subset) # calling backtrack function with incrementing i by 1
        subset.append(self.nums[i]) # appending the nums of ith element to subset array
        self.backtrack(i+1,subset) # calling backtrack function with incrementing i by 1
        
        subset.pop() # popping the subset array
