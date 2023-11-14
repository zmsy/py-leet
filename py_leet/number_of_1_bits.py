class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Write a function that takes the binary representation of an unsigned
        integer and returns the number of '1' bits it has (also known as the
        Hamming weight).
        """
        one_bits = 0
        i = n
        while i > 0:
            one_bits += i % 2
            i >>= 1

        return one_bits
