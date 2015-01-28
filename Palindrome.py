"""
A string is a palindrome if it has exactly the same sequence of characters when read left-to-right as it has when read right-to-left. For example, the following strings are palindromes:
    "kayak",
    "Rats live on no evil star",
    "Able was I ere I saw Elba".
    A string A is an anagram of a string B if A can be obtained from B by rearranging the characters. For example, in each of the following pairs one string is an anagram of the other:
    "mary" and "army",
    "rocketboys" and "octobersky",

Write a function:
    class Solution { public int isAnagramOfPalindrome(String S); }
    that, given a non-empty string S consisting of N characters, returns 1 if S is an anagram of some palindrome and returns 0 otherwise.
Assume that:
N is an integer within the range [1..100,000];
string S consists only of English lower-case letters (a-z).

For example, given S = "dooernedeevrvn", the function should return 1, because "dooernedeevrvn" is an anagram of the palindrome "neveroddoreven". Given S = "aabcba", the function should return 0.

Complexity:
    expected worst-case time complexity is O(N);
    expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
"""

class Solution:
    
    #parameter A, a string
    def isanagrampalindrome (self, A):
        
        words = list(A)   #transform string to a list of word
        
        numbers = [] #transform word to number
        
        for word in words:
            numbers.append(ord(word))
            
        one = 0
        for i in numbers:
            one ^= i
            
        if one==1 and len(A)%2 == 1:     #one odds and the length is odd
            return 1    
        elif one==0 and len(A)%2 == 0:   #no odds and the length is even
            return 1
        else:
            return 0
 
S = "dooernedeevrvn"
solution = Solution()
print solution.isanagrampalindrome(S)


S = "aabcba"
solution = Solution()
print solution.isanagrampalindrome(S)

        
        