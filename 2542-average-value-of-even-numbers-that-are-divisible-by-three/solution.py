from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for num in nums:
            if num % 6 == 0:  # divisible by both 2 and 3
                total += num
                count += 1

        if count == 0:
            return 0
        else:
            return total // count  # integer average
