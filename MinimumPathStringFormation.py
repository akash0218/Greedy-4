# Time Complexity : O(m*(log(n)); m --> len(target), n --> len(source)
# Space Complexity : O(1);
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#
#
from collections import defaultdict


class Solution:
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return nums[start] if 0 <= start < len(nums) else -1

    def shortestWay(self, source, target):
        dictu = defaultdict(list)
        count = 1
        s_ptr = 0
        t_ptr = 0
        for i in range(len(source)):
            dictu[source[i]].append(i)
        while t_ptr < len(target):
            if s_ptr < len(source) and source[s_ptr] == target[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            elif s_ptr > len(source)-1 or source[s_ptr] != target[t_ptr]:
                if target[t_ptr] not in dictu:
                    return -1
                index = self.binarySearch(dictu[target[t_ptr]], s_ptr)
                if index == -1:
                    s_ptr = dictu[target[t_ptr]][0]
                    count += 1
                else:
                    s_ptr = index
        return count


print(Solution().shortestWay('xyzzyxyyxxzz', 'xxxyyxzxyyzxyxxzzy'))

# TC: O(m*n); SC: O(1)
# class Solution:
#     def shortestWay(self, source, target):
#         count = 0
#         t_ptr = 0
#         s_ptr = 0
#         dictu = set()
#         for i in source:
#             dictu.add(i)
#         while t_ptr < len(target):
#             s_ptr = s_ptr % len(source)
#             if s_ptr == 0:
#                 count += 1
#             if target[t_ptr] not in dictu:
#                 return -1
#             elif target[t_ptr] == source[s_ptr]:
#                 t_ptr += 1
#                 s_ptr += 1
#             elif target[t_ptr] != source[s_ptr]:
#                 s_ptr += 1
#         return count
#
#
# print(Solution().shortestWay('abc', 'abcbc'))
