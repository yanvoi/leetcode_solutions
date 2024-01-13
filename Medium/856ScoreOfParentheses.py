"""
Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:

	"()" has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.

 
Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2

 
Constraints:

	2 <= s.length <= 50
	s consists of only '(' and ')'.
	s is a balanced parentheses string.

"""

# O(n) time, O(1) space
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        answer, depth = 0, 0
        prev = '*'
        for char in s:
            if char == '(': depth += 1
            else:
                depth -= 1
                if prev == '(': answer += pow(2, depth)
            prev = char

        return answer
