'''
How many zeros in factorial of N

'''

class Solution:
    
    
    #parameter N, integer number
    def zero_count(self, N):
        
        count = 0
        
        for i in xrange(1, N+1, 1):
            
            if i%5 == 0:    #find out the 
                count += 1 
                
                
        return count
    

S = 10
solution = Solution()
print solution.zero_count(S)