# LeetCode Algorithms "Find the index of the first Occerrence in a String"

class Solution:

    def strStr(self, haystack : str , needle : str) -> int:

        count = 0

        hs_len = len(haystack) - len(needle) + 1

        for _ in range(hs_len):

            if haystack[count:len(needle) + count] == needle:
                return count
            
            count += 1

        else:
            return -1
        
main = Solution()
print(main.strStr(haystack='leetcode', needle='leet'))