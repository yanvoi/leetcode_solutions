class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []
        for i, j, k, in itertools.combinations(range(1, len(s)), 3):
        # same as:
        # for i in range(1, len(s)):
        #   for j in range(i + 1, len(s)):
        #     for k in range(j + 1, len(s)):
            ip = (s[:i], s[i:j], s[j:k], s[k:])
            if self.ip_is_valid(ip):
                answer.append('.'.join(ip))

        return answer


    def ip_is_valid(self, ip):
        return all(self.part_is_valid(part) for part in ip)

    
    def part_is_valid(self, part):
        return int(part) <= 255 and (part[0] != '0' or part == '0')
