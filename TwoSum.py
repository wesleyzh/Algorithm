'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution:
  # @return a tuple, (index1, index2)
  def twoSum(self, num, target):
    index = {}
    for i in range(len(num)):
      if num[i] in index and num[i] * 2 == target:
        return (min(i + 1, index[num[i]]), max(i + 1, index[num[i]]))
      index[num[i]] = i + 1
    
    for i in range(len(num)):
      if target - num[i] in index and num[i] * 2 != target:
        other = index[target - num[i]]
        return (min(i + 1, other), max(i + 1, other))
        
    return None
    
numbers=[0,4,3,0]
target=0

solution = Solution()
print solution.twoSum(numbers, target)