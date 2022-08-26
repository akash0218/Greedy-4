# Time Complexity : O(n) + O(n) --> O(n)
# Space Complexity : O(1);
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#
#
from typing import List


class Solution:
    def rotations(self, tops, bottoms, number):
        top = 0
        bottom = 0
        for i in range(len(tops)):
            if tops[i] != number and bottoms[i] != number:
                return -1
            elif tops[i] != number:
                top += 1
            elif bottoms[i] != number:
                bottom += 1
        return min(top, bottom)

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = self.rotations(tops, bottoms, tops[0])
        return max(result, self.rotations(tops, bottoms, bottoms[0]))


print(Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))


# TC: O(n)+O(n) --> O(n); SC: O(n)
# from collections import defaultdict
# from typing import List
#
#
# class Solution:
#     def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
#         n = len(tops)
#         dictu = defaultdict(int)
#         number = 0
#         for i in range(n):
#             dictu[tops[i]] += 1
#             if dictu[tops[i]] >= n:
#                 number = tops[i]
#                 break
#             dictu[bottoms[i]] += 1
#             if dictu[bottoms[i]] >= n:
#                 number = bottoms[i]
#                 break
#         top = 0
#         bottom = 0
#         for i in range(n):
#             if tops[i] != number and bottoms[i] != number:
#                 return -1
#             elif tops[i] != number:
#                 top += 1
#             elif bottoms[i] != number:
#                 bottom += 1
#         return min(top, bottom)
#
#
# print(Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
