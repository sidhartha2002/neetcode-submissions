class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for st in strs:
            # sort the character of each string...
            sorted_key = "".join(sorted(st))
            dic[sorted_key].append(st)

        return list(dic.values())
        