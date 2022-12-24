class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
        good = set(positive_feedback)
        bad = set(negative_feedback)
        
        points = dict()
        for i, st_id in enumerate(student_id):
            cur = 0
            words_to_check = report[i].split()
            for word in words_to_check:
                if word in good:
                    cur += 3
                elif word in bad:
                    cur -= 1
                    
            points[st_id] = cur
            
        return sorted(student_id, key=lambda x: (points[x], -x), reverse=True)[:k]
        
