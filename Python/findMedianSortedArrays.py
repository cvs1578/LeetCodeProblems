#Problem 4: Median of Two Sorted Arrays:
#Given two sorted arrays, return the median of the merged sorted array
#Time complexity of O(log(m+n))

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    
    #plan: Two pointers going in order from both nums. 
    #Basically create a sorted array from the two and stop when we hit the middle. 
    #Pretty sure the complexity would be O((n+m)/2) though and not log(m+n).
    
    #Holy cow this works. Need to lower complexity in future
    
    #First, find the total length
    totalLen = len(nums1)+len(nums2)
    Even = False 
    length = int(totalLen/2)+1 #Need to add 1 in the LeetCode Compiler. This also accounts for the even numbers because we actually want the even lengths to add a 1
    #Two pointers, each starting at the beginning of each array
    point1 = 0
    point2 = 0
    sortedarray = [] #Where we'll store the sorted array.
    
    #Until we get to the middle
    for i in range(length):
        #We'll compare the values of the two pointers and store the smallest
        if point1<len(nums1) and point2<len(nums2):
            if nums1[point1]<nums2[point2]:
                sortedarray.append(nums1[point1])
                point1+=1
            else:
                sortedarray.append(nums2[point2])
                point2+=1
        #Gotta account for when the pointer exceeds both lists
        elif point1<len(nums1):
            sortedarray.append(nums1[point1])
            point1+=1
        else:
            sortedarray.append(nums2[point2])
            point2+=1
    #If it's even, the median is the last two values added together/2
    if totalLen%2 == 0:
        sortedarray[-1] = float(sortedarray[-2]+sortedarray[-1])/2 #answer requires float or else it'll consider it as an int
    return sortedarray[-1]

print(findMedianSortedArrays([1,2],[3,4]))