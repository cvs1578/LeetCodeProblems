#Problem 242: Valid Anagram
#Given two strings, find if t is an anagram of s
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    #Idea: Use dictionary to store each individual letter
    sDict = {} #Start with S Dictionaru
    for i in s:
        sDict[i]=1+sDict.get(i,0) #Increment counter by 1 if exists, if not then it is created
    tDict = {} #same with t
    for i in t:
        tDict[i] = 1+tDict.get(i,0)
    if sDict == tDict: #An anagram should have the exact same dictionary
        return True
    return False
#This has a Runtime of 36ms and Mem Usage of 14MB :D

#Another solution with longer runtime:
#Basically, just sort the arrays
def isAnagramLonger(s,t):
    return sorted(s)==sorted(s)