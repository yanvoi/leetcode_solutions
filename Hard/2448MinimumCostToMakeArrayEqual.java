// I wanted to practive java a little bit for a change
class Solution {
    private long getCost(long pivot, int[] nums, int[] cost) {
        long cur_cost = 0L;
        for (int i = 0; i < nums.length; i++) {
            cur_cost += Math.abs(nums[i] - pivot) * cost[i];
        }
        return cur_cost;
    }

    public long minCost(int[] nums, int[] cost) {
        
        long left = 1L;
        long right = 1000000L;
        for (int num : nums) {
            left = Math.min(left, num);
            right = Math.max(right, num);
        }
        long answer = getCost(0, nums, cost);

        while (left < right) {
            long mid = (left + right) / 2;
            long first_cost = getCost(mid, nums, cost);
            long second_cost = getCost(mid + 1, nums, cost);
            answer = Math.min(first_cost, second_cost);
            if (first_cost < second_cost) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }

        return answer;
    }
}
