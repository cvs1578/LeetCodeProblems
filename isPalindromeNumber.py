#Problem 9: Palindrome Number
#Given an integer x, return true if X is a palindrome.
#Else, return False
#Try and solve without converting the int to a string.

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    if x<0: #Negatives are always not palindromes due to negative sign
        return False 
    digits = []
    #We're gonna store each individual digit in a list so wer can compare them
    while x>0:
        digits.append(x%10) #Gives the remainder, meaning the rightmost digit
        x = int(x/10) #Removes the rightmost digit
    
    #Next we're gonna use 2 pointers to compare the right and left values
    left = 0
    right = len(digits)-1

    while left<right: #Once we hit the middle, we know if it's a palindrome
        if digits[left]!=digits[right]: #If the values are ever different, then it is not a palindrome
            return False
        #Always remember to increment/decrement the pointers!!!
        left+=1
        right-=1
    
    return True #If we made it here, then it's positive

print(isPalindrome(10))