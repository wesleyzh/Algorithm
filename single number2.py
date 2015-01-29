"""
Given an array of integers, every element appears three times except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Analysis:
Time Complextiy 
Space Complexity
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        once = 0       #finally contains the bits appear once
        twice = 0      #finally contains the bits appear twice
        thirdTimes = 0 #finally contains the bits appear three times
        for i in A:
            twice |= once & i #record bits appear twice
            once ^= i         #record bits appear once
            thirdTimes = once & twice #record bits appear three times
            once &= ~thirdTimes  #remove bits appear three times
            twice &= ~thirdTimes #remove bits appear three times
            
        return once