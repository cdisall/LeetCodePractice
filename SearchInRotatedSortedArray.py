class Solution:
    def search(self, nums, target):
        # Find rotation
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i+j)//2
            if nums[(j)] < nums[(mid)]:
                i = mid + 1
            else:
                j = mid
        k = i
        i = 0
        j = len(nums) - 1
        # Find target
        while i <= j:
            # Find literal mid of array
            # mid = (i+j)/2
            # Shift to account for rotation
            # mid = mid + k
            # Use mod len to wrap to start of array
            # mid = mid % n
            tmp = ((i+j)//2)
            mid = (tmp + k) % len(nums)
           #  mid = (((i+j)/2) + k) % len(nums)
            # Search
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = tmp + 1;
            else:
                j = tmp - 1
        return -1




