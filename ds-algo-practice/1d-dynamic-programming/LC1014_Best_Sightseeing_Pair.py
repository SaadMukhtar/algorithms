class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # LC1014_Best_Sightseeing_Pair.py
        maxPair = 0
        resScore = 0
        for i, n in enumerate(values):
            resScore = max(resScore, maxPair-i+n)
            if maxPair < i + n:
                maxPair = i + n
        return resScore
