int binaryGap(int n){
    int answer = 0;
    int cur_distance = 0;
    int seen_one = 0;

    while (n > 0) {
        int bit = n & 1;
        n >>= 1;

        if (bit == 1) {
            if (seen_one == 1 && cur_distance > answer) {
                answer = cur_distance;
            }
            seen_one = 1;
            cur_distance = 1;
        }
        else {
            cur_distance += 1;
        }
    }

    return answer;
}
