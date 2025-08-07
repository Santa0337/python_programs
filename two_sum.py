class Solution:
    def twoSum(self, numbers, target: int):
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i]+numbers[j] == target and i!=j:
                    return [i,j]
numbers = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(numbers, target)
print(result)