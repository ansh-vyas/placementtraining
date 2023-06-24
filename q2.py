# 💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# - Return k.

# **Example :**
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_*,_*]

# **Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[


def remove_element(nums, val):
  # initialize a pointer to the first element
  i = 0
  # loop through the array
  for num in nums:
    # if the current element is not equal to val
    if num != val:
      # copy it to the position pointed by i
      nums[i] = num
      # increment i
      i += 1
  # return i as the number of elements not equal to val
  return i