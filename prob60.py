"""
Daily Coding Problem: Problem #60 [Medium]

This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned
into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it 
would return true, since we can split it up into {15, 5, 10, 15, 10}
and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, 
since we can't split it up into two subsets that add up to the same sum.
"""

def find_sum(lst, sum): 
    for idx, num in enumerate(lst):
        if sum == num:
            return True
        if num < sum:
            if find_sum(lst[idx+1:], sum - num):
                return True
    return False


def is_part(lst):
    lst.sort(reverse = True)
    total = 0
    for num in lst:
        total += num
    if (total % 2) != 0: # Number must be even to be partitioned into 2 multisets
        return False
    total //= 2
    return find_sum(lst[1:], total - lst[0])
    return False

lst = [15, 5, 20, 10, 35, 15, 10]
print("true" if is_part(lst) else "false")
lst = [15, 5, 20, 10, 26]
print("true" if is_part(lst) else "false")
