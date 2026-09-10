from math import prod
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            total = 1
            for x in nums:
                if x != 0:
                    total *= x
            return [total if x == 0 else 0 for x in nums]

        # aucun zéro : produit total calculé UNE seule fois
        total = prod(nums)
        return [total // x for x in nums]