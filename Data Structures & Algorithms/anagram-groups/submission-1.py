class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char) - ord('a')] += 1
            
            dic[tuple(count)].append(st)
            
        return list(dic.values())

        