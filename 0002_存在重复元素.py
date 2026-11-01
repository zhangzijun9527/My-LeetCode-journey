# 存在重复元素
#
# 给你一个整数数组nums 。如果任一值在数组中出现至少两次 ，返回true ；如果数组中每个元素互不相同，返回false


def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

nums = [1,2,3,4,5,6,6,8,9]
def containsDuplicate2(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            return True
        hashmap[num] = 1
    return False
print(containsDuplicate2(nums))