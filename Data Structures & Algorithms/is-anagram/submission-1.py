class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        return False



"""
Notes: 

brute force solution: 
    count the number of occurrences of each char and put them as key value pairs in a hashmap. Do this
    for both and if they match, then it is an anagram. 

- must check whether each char in s appears in t the same amount of times.
    1. What is the optimal way to implement this? 
        Thought: If I count how many times each char shows up in s that is O(n) time. 
            - I can then check if it shows up exactly that many times in t. If it does, move on to next char. 
"""
        