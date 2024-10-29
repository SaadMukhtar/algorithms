from collections import defaultdict
from typing import List

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # Pair values with their labels and sort them by value in descending order
        items = sorted(zip(values, labels), key=lambda x: x[0], reverse=True)
        label_count = defaultdict(int)
        res = 0
        selected_count = 0
        
        # Iterate through sorted items
        for value, label in items:
            # Stop if we've selected the maximum number of items
            if selected_count == numWanted:
                break
            # Skip this item if the label limit is reached
            if label_count[label] < useLimit:
                res += value
                label_count[label] += 1
                selected_count += 1
                
        return res
