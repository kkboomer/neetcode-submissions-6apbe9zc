class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # keep a monotonically increasing stack and at the end muliply len by min number
        stack = []
        max_area = max(heights)
        if len(heights) == 1:
            return max_area
        for i in range(len(heights)):
                # the item we are about to add is greater than the top of the stack
                # was thinking of having a current_max then trying to update max area at the end of the iteration
            while len(stack) != 0 and heights[i] <= heights[stack[-1]]:
                #the logic for calculating the size of the rectangle
                h = stack.pop()
                if not stack:
                    max_area = max(max_area, (i) * heights[h])
                else:
                    max_area = max(max_area, (i-stack[-1]-1) * heights[h])
            stack.append(i)
        e = len(heights) #the right boundary
        while len(stack) != 0:
            h2 = stack.pop()
            if not stack:
                max_area = max(max_area, (e) * heights[h2])
            else:
                max_area = max(max_area, (e-stack[-1]-1)* heights[h2]) ## same logic as above
        return max_area