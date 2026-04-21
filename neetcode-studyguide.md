# Core Data Structures

## Dynamic Array

```python
# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.
class DynamicArray:
    
    def __init__(self, capacity: int):


    # Get value at i-th index
    def get(self, i: int) -> int:

    # Set n at i-th index
    def set(self, i: int, n: int) -> None:

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:


    # Remove the last element in the array
    def popback(self) -> int:


    def resize(self) -> None:


    def getSize(self) -> int:

    
    def getCapacity(self) -> int:

```

## Singly Linked List
```python
# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):


# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):

    
    def get(self, index: int) -> int:

      
    def insertHead(self, val: int) -> None:


    def insertTail(self, val: int) -> None:


    def remove(self, index: int) -> bool:


    def getValues(self) -> List[int]:

```

## Doubly Linked List
```python
# Doubly Linked List Node
class Node:
    def __init__(self, value, next_node=None, prev_node=None):


    def set_next_node(self, next_node):

    def get_next_node(self):

    def set_prev_node(self, prev_node):

    def get_prev_node(self):

    def get_value(self):

    
class DoublyLinkedList:
    def __init__(self):


    def add_to_head(self, new_value):
 


    def add_to_tail(self, new_value):



    def remove_head(self):
    


    def remove_tail(self):



    def remove_by_value(self, value_to_remove):

```

## Binary Search Tree
```python
# Binary Search Tree Node
class TreeNode:
    def __init__(self, key):

    

# A utility function to insert
# a new node with the given key
def insert(root, key):

```

# NeetCode Solutions

## Arrays and Hashing

### Contains Duplicate
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
```
Time and Space Complexity:
- Time: O(n)
- Space: O(n)

### Valid Anagram
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

```
Time and Space Complexity:
- Time: O(n + m)
- Space: O(1) since we have at most 26 different characters.

where n and m are the lengths of the strings s and t respectively.

### Two Sum
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

```
Time and Space Complexity:
- Time: O(n)
- Space: O(n)

### Group Anagrams
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

```
Time and Space Complexity:
- Time: O(m * n)
- Space: 
  - O(m * n) extra space
  - O(m * n) space for the output list

### Top K Frequent Elements

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

```
Time and Space Complexity:
- Time: O(n)
- Space: O(n)

### Encode and Decode Strings
```python
class Solution:

    def encode(self, strs: List[str]) -> str:


    def decode(self, s: str) -> List[str]:

```
Time and Space Complexity:
- Time: O(m) for each encode() and decode() function call.
- Space: O(m + n) for each encode() and decode() function call.

Where m is the total length of all strings and n is the number of strings.

### Products of Array Except Self

```python
class Solution:
    def productExceptSelf(self,

```

### Products of Array Except Self

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
```
Time and Space Complexity:
- Time: O(n) 
- Space:
  - O(1) extra space
  - O(n) space for the output array


## Two Pointers

### Valid Palindrome
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        

    def alphaNum(self, c) -> bool:
        
```
Time and Space Complexity:
- Time: O(n) 
- Space: O(1)

### Two Integer Sum II
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

```



## Sliding Window

### Best Time to Buy and Sell Stock
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
```
Time and Space Complexity:
- Time: O(n) 
- Space: O(1)

### Longest Substring Without Repeating Characters
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # char -> index (last)
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                # max(lastIndex[char] + 1, left)
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
```
Time and Space Complexity:
- Time: O(n) 
- Space: O(m)


## Stack

### Valid Parentheses
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
```
Time and Space Complexity:
- Time: O(n) 
- Space: O(n)

### Min Stack
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1] 
```
Time and Space Complexity:
- Time: O(1) for all operations.
- Space: O(n)

### Evaluate Reverse Polish Notation
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # pop order matters
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # float division to avoid integer overflow
                # truncate towards zero using int()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
```
Time and Space Complexity:
- Time: O(n) 
- Space: O(n)

