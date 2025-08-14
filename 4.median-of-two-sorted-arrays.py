class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l1, l2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        middle = (l1 + l2  - 1) // 2
        while p1 < l1 and p2 < l2 and p1 + p2 < middle:
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        if p1 + p2 < middle:
            if p1 < l1:
                p1 = middle - l2
            else:
                p2 = middle - p1
        if (l1 + l2) % 2 == 0:
            if p2 == l2:
                ret = nums1[p1]
                p1 += 1
            elif p1 == l1:
                ret = nums2[p2]
                p2 += 1
            elif nums1[p1] <= nums2[p2]:
                ret = nums1[p1]
                p1 += 1
            else:
                ret = nums2[p2]
                p2 += 1
            if p2 == l2:
                ret += nums1[p1]
            elif p1 == l1:
                ret += nums2[p2]
            elif nums1[p1] <= nums2[p2]:
                ret += nums1[p1]
            else:
                ret += nums2[p2]
            return ret / 2.0
        else:
            if p2 == l2:
                return nums1[p1]
            elif p1 == l1:
                return nums2[p2]
            elif nums1[p1] <= nums2[p2]:
                return nums1[p1]
            else:
                return nums2[p2]