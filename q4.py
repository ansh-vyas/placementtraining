# Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

def plus_one(digits):
  # loop through the array from right to left
  for i in range(len(digits) - 1, -1, -1):
    # if the current digit is not 9, increment it by one and return the array
    if digits[i] != 9:
      digits[i] += 1
      return digits
    # otherwise, set the current digit to 0 and continue the loop
    else:
      digits[i] = 0
  # if all the digits are 9, prepend a 1 to the array and return it
  return [1] + digits