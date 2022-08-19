# Problem 217
# Given array, return 2 if any value appears at least twice
    
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #Sets are unordered data type that does not contain any duplicates, so if we convert the array to a set
    #Then we will be able to compare the size of the set to the array to determine if there were any duiplicates.
    
    if len(set(nums))!= len(nums):
        return True
    else:
        return False