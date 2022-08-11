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
    #Pretty sure the complexity would be O((n+m)/2) though and not log(m+n), so this probably will not work.
    length = int(len(nums1)+len(nums2)/2)
    point1 = 0
    point2 = 0
    sortedarray = []
    for i in range(length):
        if point1<len(nums1) and point2<len(nums2):
            if nums1[point1]<nums2[point2]:
                sortedarray.append(nums1[point1])
                nums1+=1
            else:
                sortedarray.append(nums2(point2))
                nums2+=1