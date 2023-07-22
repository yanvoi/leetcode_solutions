class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(ruleKey == "type" and ruleValue == type_i or \
                   ruleKey == "color" and ruleValue == color_i or \
                   ruleKey == "name" and ruleValue == name_i \
                   for type_i, color_i, name_i in items)
