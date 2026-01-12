class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_c == 0:
                flips += bit_a + bit_b  # Flip all 1s to 0 [web:25]
            else:
                if bit_a == 0 and bit_b == 0:
                    flips += 1  # Flip one to 1 [web:22]
            a, b, c = a >> 1, b >> 1, c >> 1
        return flips
