# Name: Conor Smith
# Date 5/12/21
# Description: Takes a list of numbers mutates that list by squaring each value in the list

def square_list(nums):
  """Uses a for loop to iterate over each object in nums and multiply by itself, mutating the original list"""
  for s in range(len(nums)):
    nums[s] = nums[s]*nums[s]

#nums = [7, -3, 12, 9]
#square_list(nums)
#print(nums)