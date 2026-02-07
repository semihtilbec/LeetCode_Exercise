from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist = nums1 + nums2
        newlist.sort()
        lenght = len(newlist)

        if len(newlist) % 2 == 0:
            result1 = newlist[int(lenght // 2)]
            result2 = newlist[int(lenght // 2) - 1]
            finalresult = (result1 + result2) / 2
        
        else:
            finalresult = newlist[int(lenght // 2)]
        return finalresult

nums1 = list(map(int, input("Enter the numbers for nums1: ").split()))
nums2 = list(map(int, input("Enter the numbers for nums2: ").split()))
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)