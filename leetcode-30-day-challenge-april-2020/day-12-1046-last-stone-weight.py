class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1 :
            stones.sort(reverse=True)
            if stones[0]!=stones[1]:
                stones[0]-=stones[1]
                del stones[1]
            else:
                del stones[0:2]
        if len(stones):
            return stones[0]
        else:
            return 0
