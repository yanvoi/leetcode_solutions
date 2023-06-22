// practicing java on easy problems
class Solution {
    public String removeStars(String s) {
        int to_remove = 0;
        StringBuilder answer = new StringBuilder();

        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == '*') {
                to_remove ++;
            }
            else if (to_remove > 0) {
                to_remove --;
            }
            else {
                answer.append(c);
            }
        }

        return answer.reverse().toString();
    }
}
