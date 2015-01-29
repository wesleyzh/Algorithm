'''
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an arrya A:

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

7 is not an equilibrium index, because it is not a valid index of array A.

Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
'''

class Solution:
    
    #parameter A, a list of numbers
    def equilibrium_index(self, A):
        
        total_sum = 0 #initialize the total sum of all elements in A
        
        left_sum = 0  #initialize the total sum of all elements in A
        
        for a in A:
            total_sum += a   #find the total sum of all elements in A
            
        for i in xrange(0, len(A) - 1):  #search the equilibrium index until the first found
            
            total_sum -= A[i]           #total sum is the right sum of index greater than i now
            
            if left_sum == total_sum:
                return i
           
            left_sum += A[i]
        
        return -1
    

solution = Solution()
s = [-7, 1, 5, 2, -4, 3, 0]

print solution.equilibrium_index(s)

            
            
            
            