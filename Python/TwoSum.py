#Given an array of integers nums, and an integer target, return indices of the two numbers such that they add up to the target
def twoSum(nums, target):
    #Note: Since I don't want to make it into classes, I removed the Class Solution from the Leetcode Console.
    
    #First: Make a dictionary of all the numbers we've looked at
    numbersLookedAt = {}
    #Next, we will do a for loop and attempt to find if the target-i number is located in the list we created
    for i in range(len(nums)):
        if target-nums[i] in numbersLookedAt:
            return numbersLookedAt[target-nums[i]],i #need to return the indeces
        else: #If the number isn't in hte list, then we will add i to the list
            numbersLookedAt[nums[i]] = i

print (twoSum([2,7,11,15],9)) #This is the example problem
