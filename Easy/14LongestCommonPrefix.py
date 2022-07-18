class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = strs[0]
        
        for check_prefix in strs[1:]:
            prefix = check_prefix[:len(common)]
            common = common[:len(prefix)]
            
            if prefix == common:
                continue
                
            while prefix != common:
                prefix = prefix[:len(prefix) - 1]
                common = common[:len(common) - 1]
        
        return common
        
