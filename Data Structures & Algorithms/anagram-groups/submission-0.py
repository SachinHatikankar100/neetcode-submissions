class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            sortedS = "".join(sorted(i))
            ans[sortedS].append(i)
        return list(ans.values())
        