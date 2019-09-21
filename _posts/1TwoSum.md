---
layout: post
title:  1TwoSum
categories: leetcode
---

## 1. TwoSum
### Solution1: brutal solution
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```
O(n^2) time limit exceeded
O(1) space

### 2. Solution2: Hashtable
判断条件为：target-nums1 ？= 0，不满足条件将num存入哈希表中，value为下标
```angular2
    
```
