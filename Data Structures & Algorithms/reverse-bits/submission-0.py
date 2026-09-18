class Solution:
    def reverseBits(self, n: int) -> int:
        binaire = format(n, '032b')
        binaire_inverse = binaire[::-1]
        return int(binaire_inverse, 2)