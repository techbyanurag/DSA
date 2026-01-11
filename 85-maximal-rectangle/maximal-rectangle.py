class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = heights[j] + 1 if val == "1" else 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        return max(heights[i] * (right[i] - left[i] - 1) for i in range(n))
