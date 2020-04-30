class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        table = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    table[i][j] = 1 + table[i-1][j-1]
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])

        return table[m][n]


#         from functools import lru_cache
#         @lru_cache()
#         def helper(text1,text2,m,n):

#             if m == 0 or n == 0:
#                 return 0

#             if text1[m-1] == text2[n-1]:
#                 return 1 + helper(text1,text2,m-1,n-1)
#             else:
#                 return max(helper(text1,text2,m-1,n),helper(text1,text2,m,n-1))

#         return helper(text1,text2,len(text1),len(text2))
