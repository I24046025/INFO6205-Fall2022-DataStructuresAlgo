import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # m: number of strings in strs
        # n: avergae length of strings in strs

        # time complexity: O(m * n)
        # space complexity: O(m)

        # mapping charCount to list of Anagrams
        res = collections.defaultdict(list)

        for s in strs:
            # a, b, c, ..., y, z
            count = [0] * 26

            for c in s:
                # ASCII position
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()