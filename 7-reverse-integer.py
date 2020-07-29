# Given a 32-bit signed integer, reverse digits of an integer
# Example 1. Input: 123 Output 321

# https://leetcode.com/problems/reverse-integer/

class Solution:

    def swapPosition(self, list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    def reverse(self, x: int) -> int:
        list_of_numbers = [str(it) for it in str(x)]
        return_value = ""
        if list_of_numbers[0] == "-":
            result = list_of_numbers[::-1]
            result = result[-1:] + result[:-1]
            for i in result:
                return_value += str(i)
            if int(return_value) > 2147483647 or int(return_value) < -2147483647:
                return 0
            else:
                return int(return_value)
        else:
            result = list_of_numbers[::-1]
            for i in result:
                return_value += str(i)
            if int(return_value) > 2147483647 or int(return_value) < -2147483647:
                return 0
            else:
                return int(return_value)


test = Solution()
print(test.reverse(-892))


# Completed on 07-28-2020
# Took 4 Submissions on LeetCode
