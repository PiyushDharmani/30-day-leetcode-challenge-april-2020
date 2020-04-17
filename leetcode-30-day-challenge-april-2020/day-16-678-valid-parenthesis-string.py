class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum_open_brackets = 0
        maximum_open_brackets = 0
        for c in s:
            if c=='(':
                minimum_open_brackets+=1
                maximum_open_brackets+=1
            elif c==')':
                minimum_open_brackets-=1
                maximum_open_brackets-=1
            else:
                minimum_open_brackets-=1
                maximum_open_brackets+=1
            if maximum_open_brackets<0:
                return False
            minimum_open_brackets = max(minimum_open_brackets,0)

        return minimum_open_brackets == 0
