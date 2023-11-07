# Question 2 - Find Pairs
# LeetCode 1 - Two Sum 
# Time complexity: O(n^2)
# Space complexity: O(1)

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(nums[i], nums[j])

myList = [1, 2, 3, 4, 5, 6]
findPairs(myList, 6)