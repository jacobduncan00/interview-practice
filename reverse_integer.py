# Given a 32-bit signed integer, reverse digits of an integer
# Example 1. Input: 123 Output 321

# https://leetcode.com/problems/reverse-integer/

class Solution:

    def reverse(self, x: int) -> int:
        list_of_numbers = [str(it) for it in str(x)]
        return_value_string = ""
        if list_of_numbers[0] == "-":
            result = list_of_numbers[::-1]
            result = result[-1:] + result[:-1]
            for i in result:
                return_value_string += str(i)
            return_value_int = int(return_value_string)
            if return_value_int > 2147483647 or return_value_int < -2147483647:
                return 0
            else:
                return return_value_int
        else:
            result = list_of_numbers[::-1]
            for i in result:
                return_value_string += str(i)
            return_value_int = int(return_value_string)
            if return_value_int > 2147483647 or return_value_int < -2147483647:
                return 0
            else:
                return return_value_int 


test = Solution()
print(test.reverse(-892))


# Completed on 07-28-2020
# Took 4 Submissions on LeetCode
