class Question1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        # rotate the original array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        # rotate the index 0~k-1 of the rotated array
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        # rotate the index k~len(num)-1 of the rotated array
        l, r = k, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        return nums