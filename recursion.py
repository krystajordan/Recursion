"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Krysta Gonzales and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: kg34676
UT EID 2:
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    target -= nums[start]
    if group_sum(start + 1, nums, target):
        return True
    target += nums[start]
    return group_sum(start + 1, nums, target)

def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - nums[start])
    if group_sum_6(start + 1, nums, - nums[start]):
        return True
    return group_sum(start + 1, nums, target)

def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if target - nums[start] >= 0:
        if group_no_adj(start + 2, nums, target - nums[start]):
            return True
    return group_no_adj(start + 1, nums, target)
        
def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    if nums[start] % 5 == 0:
        target -= nums[start]
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target)
        else:
            return group_sum_5(start + 1, nums, target)
    else:
        excluding = group_sum_5(start + 1, nums, target)
        including = target >= nums[start] and group_sum_5(start + 1, nums, target - nums[start])
        return excluding or including

def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    end = start
    while end + 1 < len(nums) and nums[end] == nums[end + 1]:
        end += 1
    sum_clump = sum(nums[start:end + 1])
    if sum_clump <= target and group_sum_clump(end + 1, nums, target - sum_clump):
        return True
    return group_sum_clump(start + 1, nums, target)

def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    if len(nums) < 2:
        return False
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    def helper(start, target):
        if start >= len(nums):
            return target == 0
        if helper(start + 1, target - nums[start]):
            return True
        if helper(start + 1, target):
            return True
        return False
    return helper(0, total_sum // 2)

# TODO: Modify this function. You may delete this comment when you are done.
def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(index, sum1, sum2):
        if index == len(nums):
            return (sum1 % 10 == 0 and sum2 % 2 == 1) or (sum2 % 10 == 0 and sum1 % 2 == 1)
        option1 = helper(index + 1, sum1 + nums[index], sum2)
        option2 = helper(index + 1, sum1, sum2 + nums[index])
        return option1 or option2
    return helper(0, 0, 0)

# TODO: Modify this function. You may delete this comment when you are done.
def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(index, group1_sum, group2_sum):
        if index == len(nums):
            return group1_sum == group2_sum
        if nums[index] % 5 == 0:
            return helper(index + 1, group1_sum + nums[index], group2_sum)
        if nums[index] % 3 == 0:
            return helper(index + 1, group1_sum, group2_sum + nums[index])
        updated_group1 = helper(index + 1, group1_sum + nums[index], group2_sum)
        updated_group2 = helper(index + 1, group1_sum, group2_sum + nums[index])
        return updated_group1 or updated_group2
    return helper(0, 0, 0)
