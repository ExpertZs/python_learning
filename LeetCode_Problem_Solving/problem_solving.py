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

#LeetCode Problem 392. Is Subsequence
#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#Example 1:
#Input: s = "abc", t = "ahbgdc"
#Output: true

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1, pointer2 = 0 ,0
        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer1 += 1
            pointer2 += 1
        return True if pointer1 == len(s) else False

#LeetCode Problem 1. Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for index, number in enumerate(nums):
            remainings = target - number
            if remainings in hashMap:
                return [hashMap[remainings], index]
            hashMap[number] = index


#LeetCode Problem 88. Merge Sorted Array
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#Example 1:
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]
#Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n -1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n -1] = nums2[n-1]
                n-=1
        while n>0:
           nums1[m+n -1] = nums2[n-1]
           n-=1

#LeetCode Problem 21. Merge Two Sorted Lists
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

#leetCode Problem 206. Reverse Linked List
#Given the head of a singly linked list, reverse the list, and return the reversed list.
#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

#LeetCode Problem 350. Intersection of Two Arrays II
#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for index in nums1:
            if index in nums2:
                result.append(index)
                nums2.remove(index)
        return result


#LeetCode Problem 121. Best Time to Buy and Sell Stock
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#Example 1:
#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_pointer, selling_pointer = 0, 1
        max_profit = 0

        while selling_pointer < len(prices):
            if prices[buying_pointer] < prices[selling_pointer]:
                profit = prices[selling_pointer] - prices[buying_pointer]
                max_profit = max(max_profit, profit)
            else:
                buying_pointer = selling_pointer
            selling_pointer += 1
        return max_profit


