'''
In mathematics, a rational number is any number that can be expressed in the form of a fraction p/q , where p & q are two integers, and the denominator q is not equal to zero. Hence, all integers are rational numbers  where denominator, in the most reduced form, is equal to 1.
You are given a list of N rational number, {a1/b1, a2/b2, ..., aN/bN}. Print the sum ( = a1/b1 + a2/b2 + ... + aN/bN = num/den) in the most reduced form.
Input
The first line of input contains an integer, N, the number of rational numbers.  N lines follow. ithline contains two space separated integers, aibi, where aiis the numerator and bi is the denominator for the ith rational number.
Output
You have to print two space separated integers, num den, where num and den are numerator and denominator of the sum respectively.
Constraints. 1point3acres.com/bbs
	•	1 <= N <= 15
	•	1 <= ai <= 10
	•	1 <= bi <= 10-google 1point3acres
Notes
	•	Make sure the sum displayed as output is in the most reduced form.
	•	If sum is an integer, you have to print 1 as denominator.
Sample Input. 
4
4 2
2 4
2 4
2 3
Sample Output
11 3
. 1point3acres.com/bbs
Explanation
Sum is 4/2 + 2/4 + 2/4 + 2/3 = (24 + 6 + 6 + 8)/12 = 44/12 = 11/3. So you have to print "11 3", which is the most reduced form.
'''

class Solution:
    
   def gcd(self, a, b):
      """Return greatest common divisor using Euclid's Algorithm."""
      if a < b:
         a, b = b, a   #make sure a > b      

      while b:      
         a, b = b, a % b
      return a
  
   def lcm(self, a, b):
      """Return lowest common multiple."""
      return a * b // self.gcd(a, b)
  
   def lcmm(self, *args):
      """Return lcm of args."""   
      return reduce(self.lcm, args)       
    
    #parameter num, a list of numerator
    #parameter den, a list of denominator
   def ration_sum(self, num, den):
        
      if len(num) != len(den):
          
         print "The length of numerators is not equal to denominators"
         return
      
      #find the gratest common factor for denominators
      gcd = 0 
      for i in xrange(0, len(den)-1):
          
         gcd = self.gcd(den[i], den[i+1])
          
      #find the least common multiple for denominators
      lcm = self.lcmm(*den)
      
      num_sum = 0 #initialize the sum of num
      
      for i in xrange(0, len(num)):
         num_sum += num[i] * (lcm/den[i])
          
      gcd_sum = self.gcd(num_sum, lcm)   #greatest common factor of sum num and den
      
      return num_sum/gcd_sum, lcm/gcd_sum

solution = Solution()

num = [4,2,2,2]
den = [2,4,4,3]

print solution.ration_sum(num, den)