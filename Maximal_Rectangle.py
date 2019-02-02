class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        compute_graph = [[int(item) for item in matrix[i]] for i in range(len(matrix))]
        max_area = 0
        for r in range(len(compute_graph)):
            for c in range(len(compute_graph[0])-2, -1, -1):
                if compute_graph[r][c] == 0:
                    continue
                else:
                    compute_graph[r][c] += compute_graph[r][c+1]
        for j in range(len(compute_graph[0])):
            stack = []
            for i in range(len(compute_graph)):
                if not stack:
                    stack.append(i)
                    continue
                while stack and compute_graph[i][j] < compute_graph[stack[-1]][j]:
                    h = compute_graph[stack.pop()][j]
                    prev = stack[-1] if stack else -1
                    w = i - prev - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
            while stack:
                h = compute_graph[stack.pop()][j]
                if h != 0:
                    prev = stack[-1] if stack else -1
                    w = len(compute_graph) - prev - 1
                    max_area = max(max_area, h * w)
        return max_area


if __name__ == '__main__':
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    res = Solution().maximalRectangle(matrix)
    print(res)
