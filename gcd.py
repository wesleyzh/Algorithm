'''
Find the greatest common facot of two numbers
'''

class Solution:
    
    #parameters a and b are intergers
    
    def gcd(self, a, b):
        
        if a < b:
            a, b = b, a   #make sure a > b
            
        
        y = a % b
        
        if y == 0 :  # 
            return b
        
        else:
            
            a, b = b, y
            return self.gcd(a, b)
            

a = 10
b = 3

solution = Solution()
print solution.gcd(a,b)