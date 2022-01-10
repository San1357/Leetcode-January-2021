
#Time complexity : O(N+M)

#Space complexity : O(max(N,M))

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        
        while y:
            
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            print("x:",x)
        return bin(x)[2:]
