# Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move_zeroes(nums):
  # initialize a pointer to the first zero element
  zero = 0
  # loop through the array
  for i in range(len(nums)):
    # if the current element is not zero
    if nums[i] != 0:
      # swap it with the element pointed by zero
      nums[i], nums[zero] = nums[zero], nums[i]
      # increment zero
      zero += 1