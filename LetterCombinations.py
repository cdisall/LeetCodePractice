from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        n = len(digits)
        if n == 0:
            return res

        # Stack for DFS

        stack = [(0, "")]

        # Run DFS
        while stack:
            counter, path = stack.pop()
            # Check if end of tree has been reached
            if counter == n:
                res.append(path)
            else:
                next_node = digits[counter]

                # Add children to stack

                children = letter_map[next_node]
                for child in children:
                    stack.append((counter + 1, path + child))
        return res






