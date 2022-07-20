class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False
        
        changes = 0
        diffs = []
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                changes += 1
                diffs.append(i)
                
        if changes > 2:
            return False
        elif changes == 2 and s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]:
            return True
        elif changes == 0 and len(set(s)) < len(s):
            return True
        return False
