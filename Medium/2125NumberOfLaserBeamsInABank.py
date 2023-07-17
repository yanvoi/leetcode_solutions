class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = []
        for row in bank:
            devices_count = row.count("1")
            if devices_count: beams.append(devices_count)

        return sum(r1 * r2 for r1, r2 in zip(beams, beams[1:]))
