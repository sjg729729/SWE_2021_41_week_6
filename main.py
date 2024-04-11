from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  # YOUR ANSWER
  for index, num in enumerate(nums):
    complement = target - num
    if complement in nums:
      complementIndex = nums.index(complement)
      
      if complementIndex != index:
        return [index, complementIndex]
    
  return None




## test code

# li = [3,3]
# target = 6

# result = twoSum(li, target)
# if result:
#   print(result)
# else:
#   print("No answer")
