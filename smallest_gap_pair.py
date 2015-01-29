'''
给一个数组，找到数组里，两两元素之间差的绝对值最小的pair, 打印所有pair

'''

class Solution:
    
    #parameter A, a list of numbers
    def search_small_gap_pair(self, A):
        
        A.sort()  #sort the list
        
        gap = {}
        sgap = float("inf")
        
        for i in xrange(0, len(A)-1):
            
            gap[A[i], A[i+1]] = abs(A[i] - A[i+1])  #record the gap by gap
            
            
            if abs(A[i] - A[i+1]) < sgap:
                
                sgap = abs(A[i] - A[i+1])
                
                
        
        for key, value in gap.items():    #print all the pairs that have the smallest gap
            if value == sgap:
                print key
                
        return


S = [1,10, 2, 20, 100, 0]
solution = Solution()
solution.search_small_gap_pair(S)



                