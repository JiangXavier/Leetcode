### 剑指 Offer 03. 数组中重复的数字
n*logn(self)
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]
```
n，空间也是n
```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = {}
        for ind , val in enumerate(nums):
            if not d.get(val):
                d[val] = 1
            else:
                return val
```
### 剑指 Offer 04. 二维数组中的查找
```python
n*logn
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]]:
            return False
        for i in range(len(matrix)):
            a = matrix[i]
            if target > a[len(a) - 1]:
                continue
            elif target < a[0]:
                return False
            else:
                i,j = 0,len(a) - 1
                while i <= j:
                    mid = int((i+j) / 2)
                    print(a[mid])
                    if a[mid] == target:
                        return True
                    elif a[mid] < target:
                        i = mid + 1
                    else:
                        j = mid - 1
        return False
```
### 剑指 Offer 05. 替换空格
```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")
```
### 剑指 Offer 06. 从尾到头打印链表
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        a = deque()
        d = head
        while d:
            a.appendleft(d.val)
            d = d.next
        return list(a)
```
### 剑指 Offer 22. 链表中倒数第k个节点
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre = head
        for i in range(k-1):
            pre = pre.next
        n = head
        while pre.next != None:
            n = n.next
            pre = pre.next
        return n
```