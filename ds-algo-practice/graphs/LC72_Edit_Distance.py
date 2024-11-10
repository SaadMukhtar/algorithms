from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dfs(x, y):
            # Base cases
            if x == len(word1):
                print(f"Insert {word2[y:]}")
                return len(word2[y:])
            if y == len(word2):
                print(f"Remove {word1[x:]}")
                return len(word1[x:])

            # If characters match, move to next character
            if word1[x] == word2[y]:
                return dfs(x + 1, y + 1)

            # Calculate the minimum operations for Insert, Remove, and Replace
            insert_op = 1 + dfs(x, y + 1)      # Insert character from word2
            remove_op = 1 + dfs(x + 1, y)      # Remove character from word1
            replace_op = 1 + dfs(x + 1, y + 1) # Replace character from word1 to match word2

            # Find the minimum cost
            return min(insert_op, remove_op, replace_op)

        return dfs(0, 0)
