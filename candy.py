from functools import reduce

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        assignment = [1] * len(ratings)
        for i in range(0, len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                assignment[i + 1] = assignment[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and assignment[i - 1] <= assignment[i]:
                assignment[i - 1] = assignment[i] + 1
        return reduce(lambda x,y:x + y, assignment)

if __name__ == '__main__':
    ratings = [3,2,5]
    solution = Solution()
    print(solution.candy(ratings))