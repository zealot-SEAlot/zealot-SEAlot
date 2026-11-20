class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            max_left_1 = float("-inf") if i == 0 else nums1[i - 1]
            min_right_1 = float("inf") if i == m else nums1[i]

            max_left_2 = float("-inf") if j == 0 else nums2[j - 1]
            min_right_2 = float("inf") if j == n else nums2[j]

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (m + n) % 2 == 1:
                    return float(max(max_left_1, max_left_2))
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2.0
            elif max_left_1 > min_right_2:
                high = i - 1
            else:
                low = i + 1

        return 0.0