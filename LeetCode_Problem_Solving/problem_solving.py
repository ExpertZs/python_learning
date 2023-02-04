#1480. Running Sum of 1d Array
#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums.
#Example 1:

#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        output = []
        for number in nums:
            temp += number
            output.append(temp)
        return output

#724. Find Pivot Index
#Given an array of integers nums, calculate the pivot index of this array.
#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
#Return the leftmost pivot index. If no such index exists, return -1
#Example 1:
#Input: nums = [1,7,3,6,5,6]
#Output: 3
#Explanation:
#The pivot index is 3.
#Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
#Right sum = nums[4] + nums[5] = 5 + 6 = 11


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left_sum = 0
        for index in range(len(nums)):
            right_sum = total - nums[index] - left_sum
            if left_sum == right_sum:
                return index
            left_sum += nums[index]
        return -1



