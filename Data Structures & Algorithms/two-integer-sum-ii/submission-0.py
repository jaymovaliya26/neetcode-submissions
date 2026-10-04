class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n =len(numbers)
        low=0
        high=n-1
        while low<high:
            current = numbers[low]+numbers[high]
            if current==target:
                return [low+1,high+1]
            elif current < target:
                low+=1
            else:
                high-=1
        