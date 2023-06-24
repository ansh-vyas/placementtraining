# Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

def contains_duplicate(nums):
  # create a set to store the seen elements
  seen = set()
  # loop through the array
  for num in nums:
    # if the current element is already in the set, return true
    if num in seen:
      return True
    # otherwise, add it to the set
    else:
      seen.add(num)
  # if no duplicate is found, return false
  return False