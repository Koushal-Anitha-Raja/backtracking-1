class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #using for loop method
         # the resultant array
        result = [[]]
        #iterate through the nums array
        for num in nums:
            #size variable for each level
            size = len(result)
            for i in range(size):
                # assigning the result of i value in the temp 
                temp = result[i][:] 
                temp.append(num)
                #appending the value to temp
                result.append(temp) 

        #the final result array        
        return result 
        