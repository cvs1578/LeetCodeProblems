#Problem 3: Longest Substring without Repeationg Characters
#Given a string find the length of the longest substring without repeating characters
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    longest = 1 #size of longest substring
    letters = {} 
    left = 0 #left pointer
    letters[s[left]] = 1 + letters.get(s[left],0) #Initialize the dictionary
    right = 1 #Right pointer
    count = 1 # current counter

    #Plan: Window travel with dictionaries to keep track of letters

    while right<len(s):
        letters[s[right]] =  1+letters.get(s[right],0) #First, we add the letter to the dictionary
        if letters[s[right]] == 1: #If there is only one letter, then we know that there is no duplicate characters
            count+=1 #increment the count
            if count > longest:
                longest = count #Keep track of the longest pointer
        else: #Else, there is 2 of the same letter
            while letters.get(s[right])>1: #Keep doing this until there is only one of the right pointer letter
                letters[s[left]]-=1  #remove the letter from the dictionary
                left+=1 #Move the letter to the right 
            count = right-left+1 #This because decrementing the letter in the while loop causes issues when left == right.
        right+=1 #Always move the right counter    
                
    return longest
print(lengthOfLongestSubstring( "pwwkew" ))