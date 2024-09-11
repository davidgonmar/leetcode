class Solution:
    def mySqrt(self, x: int) -> int:
        _max = 1
        for i in range(0, ceil(x/2) + 1):
            if i*i > x:
                return _max
            if i*i == x:
                return i
            if i*i < x:
                _max = i
        return _max