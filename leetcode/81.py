"""

link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii

problem: 将升序数组从某点断开重排，元素可能重复，问某元素target是否存在

solution: 类33题，加了重复条件，先while st++; 令nums[start] != nums[en]后，照33思路，两次二分先找断点再搜即可

"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        st, n = 0, len(nums)
        if n == 0:
            return False
        while nums[st] == nums[-1] and st < n - 1:
            st += 1
        if st == n - 1:
            return nums[0] == target

        l, r = st, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1

        if target > nums[-1]:
            l, r = st, l - 1
        else:
            l, r = l, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return nums[l] == target