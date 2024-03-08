class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        multiple = n
        while multiple % 2 != 0:
            multiple += n
        return multiple
