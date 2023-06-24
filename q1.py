
# 💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# **Example:**
# Input: nums = [2,7,11,15], target = 9
# Output0 [0,1]

# **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][






def two_sum(nums, target):
  # create a dictionary to store the complements of each number
  complements = {}
  # loop through the array
  for i, num in enumerate(nums):
    # check if the current number is a complement of a previous number
    if num in complements:
      # return the indices of the two numbers
      return [complements[num], i]
    # otherwise, store the complement of the current number and its index
    else:
      complements[target - num] = i
  # if no solution is found, return an empty list
  return []