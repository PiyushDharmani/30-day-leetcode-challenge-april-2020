class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import defaultdict
        present_dic = defaultdict(int)
        count = 0
        for i in arr:
            present_dic[i]+=1

        for key in list(present_dic):
            if present_dic[key+1] > 0:
                count+=present_dic[key]

        print(present_dic)

        return count
