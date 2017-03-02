class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows + 1):
            temp = [1] * i
            if i >= 3:
                for j in range(1, i - 1):
                    temp[j] = result[i - 2][j - 1] + result[i - 2][j]
            result.append(temp)
        return result

   
test = Solution()
print test.generate(5)
