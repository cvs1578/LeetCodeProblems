#include<iostream>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// Problem 1448: Count Good Nodes in Binary Tree
// Given the root, a node in the tree is Good if the path from the root to X are no nodes with a value greater than X.
// Return the number of good nodes
class Solution {
public:
    int goodNodes(TreeNode* root) {
        //Recursion.
        return findGood(root, root->val);
    }
    //Returns int
    //root = current node
    //max = current maximum value in path
    int findGood(TreeNode* root, int max){
        //first, determine if node is valid
        if (!root){
            return 0;
        }
        //Now, determine if the value is greater than or equal to the max
        if (root->val >= max){
            //If so, we add 1 then recursively go through the rest of the nodes
            return 1 + findGood(root->left,root->val) + findGood(root->right, root->val);
        }
        //If not, then we just continue through the rest of the tree
        else{
            return findGood(root->left, max)+findGood(root->right, max);
        }
    }
};