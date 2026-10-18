class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack
        result = [0]* len(temperatures)
        stack = [] # pair: [temperature, index]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                result[stackIndex] = i-stackIndex
            stack.append([temp,i])
        
        return result