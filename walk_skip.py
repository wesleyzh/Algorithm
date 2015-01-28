'''
给你一个数组，里面有正数负数。然后你从坐标0开始走。每次走i+a[i]步，如果超过数组范围，你就停止了。如果在数组之间你可以继续走。然后返回你走不到的坐标数量。

Source: Twitter OA
'''

class Solution:
    
    #parameter A, a list of integer
    def skip(self, A):
        
        lb = 0          #lower bound of the array
        up = len(A)-1   #up bound of the array
        
        visited = [0]    
        
        position = 0 

        while (True):
            
            position = position + A[position]  # move to the next position
            
            if position > up or position < lb:
                break
            
            visited.append(position)   #record the the position has been visited
            
        visit = list(set(visited))  #remove the duplicated position
        
        
        return up+1-len(visit) #return the number of positions unvisited
        
        #skip = []
        #for index in xrange(lb, up+1):
            #if index not in visited:
                #skip.append(index)   #record the unvisited index
        
        #return len(skip)
    
    
a = [1,3,2,-1,2,3,40]

solution = Solution()
print solution.skip(a)
        
        