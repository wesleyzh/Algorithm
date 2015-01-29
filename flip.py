'''
You are given a binary array with N elements: d[0], d[1], ... d[N - 1]. 
You can perform AT MOST one move on the array: choose any two integers [L, R], and flip all the elements between (and including) the L-th and R-th bits. L and R represent the left-most and right-most index of the bits marking the boundaries of the segment which you have decided to flip.

What is the maximum number of '1'-bits (indicated by S) which you can obtain in the final bit-string? . more info on 1point3acres.com

'Flipping' a bit means, that a 0 is transformed to a 1 and a 1 is transformed to a 0 (0->1,1->0). 
Input Format 
An integer N 
Next line contains the N bits, separated by spaces: d[0] d[1] ... d[N - 1] 

Output: 
S 

Constraints: 
<= N <= 100000 
d can only be 0 or 1f -google 1point3acres
<= L <= R < n 
. 1point3acres.com/bbs
Sample Input: 

0 0 1 0 0 1 0 . 1point3acres.com/bbs

Sample Output: 


Explanation: 

We can get a maximum of 6 ones in the given binary array by performing either of the following operations: 
Flip [1, 5] ==> 1 1 1 0 1 1 1 0
'''

class Solution:
    
    #parameter A, a list of binary bit
    def flip(self, A):
        
        localScore = 0  #initilize the local score for current L, R
        localLeft = 0   #initilize local search left bound
        localRight = 0  #initilize local search right bound
        globalScore = 0 #initilize the best score found so far
        globalLeft = 0  #initilize global best left bound
        globalRight = 0 #initilize global best right bound
        onesFlip = 0    #ones after flip between L, R
        onesUnFlip = 0  #ones outside L, R
        
        for i in xrange(0, len(A)):
            
            diff = 1 if A[i] == 0 else -1
            
            if localScore + diff >= diff:
                localScore = localScore + diff
                localRight += 1
            else:
                localScore = diff
                localLeft = i
                localRight = i
                
            if globalScore < localScore:
                globalScore = localScore
                globalLeft = localLeft
                globalRight = localRight
                
            
        for i in xrange(0, globalLeft):
            onesUnFlip += 1 if A[i] == 1 else 0
            
        for i in xrange(globalRight+1, len(A)):
            onesUnFlip += 1 if A[i] == 1 else 0        
            
        for i in xrange(globalLeft, globalRight+1):   #count the zeros between L and R
            onesFlip += 1 if A[i] == 0 else 0        
            
            
        return onesFlip + onesUnFlip
    

s = [1, 0, 0, 1, 0, 0, 1, 0 ]

solution = Solution()
print solution.flip(s)
        
        