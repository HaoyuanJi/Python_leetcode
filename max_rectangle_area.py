import copy

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        index_store = []
        h = copy.deepcopy(height)
        h.append(0)
        maxArea = 0
        i = 0
        while i < len(h):
            if not index_store or h[index_store[-1]] <= h[i]:
                index_store.append(i)
                i = i + 1
            else:
                t = index_store.pop()
                maxArea = max(maxArea, h[t] * (i if not index_store else i - 1 - index_store[-1]))
        return maxArea

if __name__ = '__main__':
    height = [2,1,5,6,2,3]
    solution = Solution().largestRectangleArea(height)
    print(solution)