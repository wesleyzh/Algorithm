'''
A zero-indexed array A consisting of N integers is viven. We visit the indexs of the array in the following way. In the first step we visit the index 0; in every subsequent step we move from the visited index K to the index:
M = K + A[K];
provided M is within the array bounds. Otherwise, K is the last index visited. Write a funciton:
int solution(int A[], int N);. From 1point 3acres bbs
that, given an array A, returns the number of indexes that cannot be visited by the described procedure.
For example, for the array:
A[0] = 1
A[1] = 2
A[2] = 3
only index 2 cannot be visited, so the answer is 1.
For the array:
A[0] = 3
A[1] = -5
A[2] = 0
A[3] = -1
A[4] = -3
indexes 1 and 4 cannot be visited, so the answer is 2.
Assume that:
N is an integer within the range [0...200,000];
each element of array A is an integer within the range [-1,000,000...1,000,000]
Complexity:
expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N*log(N)), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
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
            
            if position in visited:
                break
            else:
                visited.append(position)   #record the the position has been visited
            
        visit = list(set(visited))  #remove the duplicated position
        
        
        return up+1-len(visit) #return the number of positions unvisited
        
        #skip = []
        #for index in xrange(lb, up+1):
            #if index not in visited:
                #skip.append(index)   #record the unvisited index
        
        #return len(skip)
    
    
a = [3, -5, 0, -1, -3]

solution = Solution()
print solution.skip(a)
        
        