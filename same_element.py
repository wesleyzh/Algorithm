'''
一个等差数列，一个等比数列，给初值，等差的值，初值，等比的值，和数组上界，求两个数组里公共元素个数
'''

class Solution:
    #parameter a, fisrt value of arithmetic progression
    #parameter b, difference of arithmetic progression
    #parameter c, first value of geometric progression
    #parameter d, difference of geometric progression
    def same_element(self, a, b, c, d, ub):
        
        ap = [a]  #list of arithmetic progression
        gp = [c]  #list of geometric progression
        
        value = a
        while (value <= ub):
            
            value = value+b
            ap.append(value)
            
        
        value = c
        while (value <= ub):
                        
            value = value*d
            ap.append(value)     
            
        
        numlist1 = ap + gp  #merge the two list
        
        numlist2 = set(numlist1)  #remove duplicated elements
        
        num_same = len(numlist1) - len(numlist2)
        
        return num_same
    

solution = Solution()

astart = 1
adiff = 1
gstart = 1
gdiff = 2

ub = 10

print solution.same_element(astart, adiff, gstart, gdiff, ub)
