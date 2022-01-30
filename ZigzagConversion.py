class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        else:
            idx = 0
            direction = 1
            # Create a list representing each row
            rows = [""] * numRows
            # Add to each row
            for i in range(len(s)):
                rows[idx] += s[i]
                idx += direction
                # Change direction when needed
                if idx == 0 or idx == numRows - 1:
                    direction = -direction
            return ''.join([r for r in rows])


#Test
if __name__ == "__main__":
    obj = Solution()
    print(Solution.convert(obj, "PAYPALISHIRING", 3))