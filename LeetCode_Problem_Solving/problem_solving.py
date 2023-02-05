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

#LeetCode Problem 217. Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:
#Input: nums = [1,2,3,1]
#Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for index in range(len(nums)):
            if nums[index] in hashmap.keys():
                return True
            else:
                hashmap[nums[index]] = index
        return False

#Leetcode Problem 53. Maximum Subarray
#Given an integer array nums, find the subarray with the largest sum, and return its sum.
#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for index in range(1, len(nums)):
            if nums[index-1]>0:
                nums[index] += nums[index-1]
        return max(nums)

#LeetCode problem 205. Isomorphic Strings
#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
#Example 1:
#Input: s = "egg", t = "add"
#Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t, map_t_to_s = {}, {}
        for char1, char2 in zip(s, t):
            if((char1 in map_s_to_t and map_s_to_t[char1] !=  char2 ) or
            (char2 in map_t_to_s and map_t_to_s[char2] !=  char1 )):
                return False
            map_s_to_t[char1] = char2
            map_t_to_s[char2] = char1
        return True



