class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # for each string in list
        for s in strs:
            # each anagram will have same freq of chars in s
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            # in res make each key the tuple of the count
            # append s to list as each anagram will have same tuple(count)
            res[tuple(count)].append(s)

        # return only values and output to list
        return list(res.values())