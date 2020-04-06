#!/usr/bin/env python


class Solution:
        
    @classmethod
    def binary_search(cls, arr, val):

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low+high)/2
            if arr[mid] < val:
                low = mid + 1
            elif arr[mid] > val:
                high = mid - 1
            else:
                return arr[mid]

        return -1


if __name__ == '__main__':
    print Solution.binary_search([1, 2, 3, 34, 56, 57, 78, 87], 57)
