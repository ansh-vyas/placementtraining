# Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

def find_error_nums(nums):
  # initialize the result array
  result = [0, 0]
  # loop through the array
  for num in nums:
    # get the absolute value of the current element
    num = abs(num)
    # if the element at the index num - 1 is negative, it means it is duplicated
    if nums[num - 1] < 0:
      # store it as the first element of the result
      result[0] = num
    # otherwise, make it negative to mark it as seen
    else:
      nums[num - 1] *= -1
  # loop through the array again
  for i in range(len(nums)):
    # if the element at the index i is positive, it means it is missing
    if nums[i] > 0:
      # store it as the second element of the result
      result[1] = i + 1
      # break the loop
      break
  # return the result array
  return result