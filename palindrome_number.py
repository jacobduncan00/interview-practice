# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        numAsList = [str(it) for it in str(x)]
        reverse = numAsList[::-1]
        if numAsList == reverse:
            return True
        else:
            return False


test = Solution()
print(test.isPalindrome(121))

# Completed on 08-09-2020
# Took 1 Submission on LeetCode
        
