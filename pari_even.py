'''
Write a function:
class Solution { public int solution(int[] A); }
that, given an array A consisting of N integers, returns the number of pairs (P, Q) such that 0 ≤ P < Q < N and (A[P] + A[Q]) is even. The function should return −1 if the number of such pairs exceeds 1,000,000,000.
For example, given array A such that:
A[0] = 2, A[1] = 1, A[2] = 5, A[3] = −6, A[4] = 9
the function should return 4, because there are four pairs that fulfill the above condition, namely (0,3), (1,2), (1,4), (2,4).
Assume that:. from: 1point3acres.com/bbs 
N is an integer within the range [0..1,000,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:
expected worst-case time complexity is O(N);. From 1point 3acres bbs
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''

class Solution:
    
    #parameter A, a list of integer
    def even_pair(self, A):
        
        count = 0
        
        for i in xrange(0, len(A)-1):
            for j in xrange(i+1, len(A)):
                
               
                if (A[i] + A[j]) % 2 == 0:
                    
                    print i,j
                    
                    count += 1 
        
        if count <  1000000000:           
            return count
        else:
            return -1
    
a = [2, 1, 5, -6, 9]
solution = Solution()

print solution.even_pair(a)

                    
                    