#Leetcode/Single Number 
"""Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Analysis:
Time Complexity O(n), Space Complexity O(1)
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) != 0 :
            single = A[0]
            for i in A[1:]:
                single ^= i   #xor operation
        else: 
            print "The list is empty."
            single = float("inf")
        
        return single

list = [1,1,2,2,3]
sol = Solution()
single_number = sol.singleNumber(list)

print single_number