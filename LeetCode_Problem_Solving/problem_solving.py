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

#LeetCode Problem 876. Middle of the Linked List
#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.
#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
#Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#LeetCode problem 142. Linked List Cycle II
#Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#Do not modify the linked list.
#Example 3
#Input: head = [1], pos = -1
#Output: no cycle
#Explanation: There is no cycle in the linked list.

#Follow Up
#Can you solve it without using extra space?
#Methodology
#This is the extension quesion of 141. Linked List Cycle Now we want to return the start node of cycle
    #    We need to check if there is cycle
    #    If there is not cycle return None and if there is cycle we set slow pointer to head
#    If slow pointer and fast pointer are not equal we move 1 step for each pointer until the two pointer conincide, then we get the node of cycle begining.
#There are lots of explainations online, the best way to try is draw graph yourself. There is simple math behind. Here
    #    L1: the distance from head to start node of cycle
    #   L2: the distance from start node of cycle to crossing node of two pointers
    #    L3: the distance from crossing node of two pointers to start node of cycle
#Slow pointer to crossing node is L1+L2.
#Fast pointer to crossing node is 2(L1+L2) since fast pointer always move 2 times of slow pointer step.
#Fast pointer is also equal to L1+L2+L3+L2 because to meet with slow pointer, the fast pointer has to run over cycle at least 1 time.
#Therefor 2(L1+L2)=L1+L2+L3+L2 -> 2L1=L1+L3 -> L1 = L3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

#leetCode Problem 566. Reshape the Matrix
#In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
#You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
#The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
#If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

#Example 1:
#Input: mat = [[1,2],[3,4]], r = 1, c = 4
#Output: [[1,2,3,4]]

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        new_mat = [[] for _ in range(r)]
        k = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(new_mat[k]) == c:
                    k += 1
                new_mat[k].append(mat[i][j])
        return new_mat


#LeetCode Problem 118. Pascal's Triangle
#Given an integer numRows, return the first numRows of Pascal's triangle.
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#Example 1:
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangles = []
        for i in range(numRows):
            triangles.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangles[i].append(1)
                else:
                    triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
        return triangles

#LeetCode Problem 409. Longest Palindrome
#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#Example 1:
#Input: s = "abccccdd"
#Output: 7
#Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.



class Solution:
    def longestPalindrome(self, s: str) -> int:
        store_dic = dict()
        for single_str in s:
            if single_str in store_dic:
                del store_dic[single_str]
            else:
                store_dic[single_str] = 1

        if len(store_dic) == 0:
            return len(s) - len(store_dic)
        else:
            return len(s) - len(store_dic) + 1


#LeetCode Problem 36. Valid Sudoku
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:
#    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#    Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_row():
            for row in board:
                if not is_valid(row):
                    return False
            return True

        def is_valid_col():
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True

        def is_valid_square():
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = [board[x][y] for x in range(i, i + 3)
                              for y in range(j, j + 3)]
                    if not is_valid(square):
                        return False
            return True

        def is_valid(value):
            res = [i for i in value if i != "."]
            return len(res) == len(set(res))

        return is_valid_row() and is_valid_col() and is_valid_square()

#LeetCode Problem 74. Search a 2D Matrix
#You are given an m x n integer matrix matrix with the following two properties:
#    Each row is sorted in non-decreasing order.
#    The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.
#You must write a solution in O(log(m * n)) time complexity.
#Example 1:
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
          return False
        m,n = len(matrix), len(matrix[0])
        low = 0
        high = (m * n) -1
        while low <= high:
          mid = (low+high)//2
          midElement = matrix[mid//n][mid%n]
          if midElement == target:
            return True
          elif midElement > target:
            high = mid -1
          else:
            low = mid + 1
        return False


