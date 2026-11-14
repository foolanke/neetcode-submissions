class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)

        for word in strs:
            fingerprint = [0] * 26
            for c in word:
                fingerprint[ord(c) - ord('a')] += 1
            key = tuple(fingerprint)
            groups[key].append(word)

        return list(groups.values())



        
            
