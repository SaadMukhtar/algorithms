class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start = goal[0]
        indices = []
        for i, c in enumerate(s):
            if c == start:
                indices.append(i)
        for index in indices:
            if s[index:] + s[:index] == goal:
                return True
        return False
        