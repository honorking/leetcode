#!/usr/bin/env python

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
"""

class Solution:

    @classmethod
    def remove_duplicates(cls, arr):
        if len(arr) <= 1:
            return len(arr)

        slow = 0
        fast = 1
        length = 1
        while fast < len(arr):
            if arr[slow] != arr[fast]:
                length += 1
                slow = fast

            fast += 1

        return length


if __name__ == '__main__':
    print Solution.remove_duplicates([2, 2, 3, 3, 4, 4, 4, 4, 5])
