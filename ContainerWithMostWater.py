class Solution(object):
    def maxArea(self, height):
        max_area = 0
        # Start with the outermost and iterate inwards
        left = 0
        right = len(height)-1
        while left < right:
            # Update max
            tmp = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, tmp)
            # Move inwards on the end with the shortest height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# Test
if __name__ == "__main__":
    obj = Solution()
    print(Solution.maxArea(obj, [1, 8, 6, 2, 5, 4, 8, 3, 7]))

