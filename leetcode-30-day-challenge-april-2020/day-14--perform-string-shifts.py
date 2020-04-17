class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        real_amount = 0
        for direction,amount in shift:
            if direction == 0:
                real_amount += amount
            else:
                real_amount -= amount
        print(real_amount)
        real_amount = real_amount % len(s)
        print(real_amount)
        return s[real_amount:] + s[:real_amount]
    
