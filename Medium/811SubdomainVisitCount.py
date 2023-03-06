# just some string parsing, no complicated logic behind the code
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        visits_count = defaultdict(int)

        for pair in cpdomains:
            # * is the coolest shit in Python I've seen in a while
            visits, *subdomains = pair.replace(' ', '.').split('.')
            for i in range(len(subdomains)):
                visits_count['.'.join(subdomains[i:])] += int(visits)

        return [str(val) + ' ' + key for key, val in visits_count.items()]
        
