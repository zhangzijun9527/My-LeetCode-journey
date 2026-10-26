# 1.两数之和
# 提示:给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
# 进阶：你可以想出一个时间复杂度小于O(n2)的算法吗

# 1.暴力解法
nums = [1,2,3,4,5]
target = 5
def two_sum(nums,target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j]==target:
                return [[i],[j]]
    return []
print(two_sum(nums,target))

# 2.最优解
def two_sum2(nums,target):
    hashmap = {}
    for idx,num in enumerate(nums):
        other = target - num
        if other in hashmap:
            return [hashmap[other],idx]
        hashmap[num] = idx
    return []
print(two_sum2(nums,target))