# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem 1448: Count Good Nodes in Binary Tree
# Given the root, a node in the tree is Good if the path from the root to X are no nodes with a value greater than X.
# Return the number of good nodes
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Idea: This is just an recursion question
        
        count = self.findGood(root,root.val)
        return count
    
    #function: return the number of good nodes.
    #Root = node in binary tree
    #maximum = maximum value in current path
    #Returns int
    def findGood(self, root, maximum):
        #Default, return 0 if there is no node
        if not root:
            return 0
        #If the value is greater than or equal to the maximum, then it's a good node
        if root.val >=maximum:
            #We'll add a 1 then recursively go through the rest of the tree
            return 1+self.findGood(root.left,root.val)+ self.findGood(root.right,root.val)
        #If not good, then just continue through the tree
        else:
            return self.findGood(root.left,maximum)+self.findGood(root.right,maximum)