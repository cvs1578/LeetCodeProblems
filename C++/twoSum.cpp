#include<iostream>
#include<vector>
#include <map>
using namespace std;

//Problem 1: Two Sum
//Given array of integers, return indices of the two numbers such that they add up to target
vector<int> twoSum(vector<int>& nums, int target) {
    map <int,int> numbersLookedAt;
    for(int i = 0; i<nums.size();i++){
        cout<<i;
        if (numbersLookedAt.find(target-nums[i])!=numbersLookedAt.end())
        {
            return {numbersLookedAt[target-nums[i]],i};
        }
        else{
            numbersLookedAt.insert({nums[i],i});
        }
    }
    //Need this for compiler to work on Leetcode
    return {-1,-1};
};

