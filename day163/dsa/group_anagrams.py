"""
DSA Problem: Group Anagrams
Given an array of strings, group anagrams together.
"""

def group_anagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print("Grouped anagrams:", group_anagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
