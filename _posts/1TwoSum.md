---
layout: post
title:  1TwoSum
categories: leetcode
---

## 1. TwoSum
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```
### O(n^2) time limit exceeded