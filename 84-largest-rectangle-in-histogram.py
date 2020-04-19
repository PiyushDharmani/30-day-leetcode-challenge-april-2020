class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        print(heights)
        area = 0
        for i in range(len(heights)):
            if (not stack) or (heights[i] >= stack[-1][0]):
                stack.append((heights[i],i))
            else:
                while stack and stack[-1][0] >= heights[i]:
                    top = stack.pop()
                    area = max(area, (i-top[1])*top[0])
                stack.append((heights[i],top[1]))
        return area
