class Solution:
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                else:
                    digits[i] = 0
                if i == 0: 
                    return [1] + digits
