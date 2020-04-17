class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # def preProcess(S):
        #     stack = []
        #     for c in S:
        #         if c != '#':
        #             stack.append(c)
        #         elif stack:
        #             stack.pop()
        #     return "".join(stack)
        # return preProcess(S) == preProcess(T)

        def f(S):
            skip = 0
            for c in reversed(S):
                if c == '#':
                    skip+=1
                elif skip:
                    skip-=1
                else:
                    yield c
        return all(x==y for x, y in itertools.zip_longest(f(S),f(T)))


        
