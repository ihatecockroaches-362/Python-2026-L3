import numpy as np
import math
class Students():
    def __init__(self, id_s, name_s,dob_s):
        self.id_s = id_s
        self.name_s = name_s
        self.dob_s = name_s
        self.marks ={}
        self.gpa = 0.0
        self.w_gpa = 0.0
        
    def input_marks(self, c_id:str, score:float):
        self.marks[c_id] = score
        
    def calculate_gpas(self, courses: list):
        score = []
        credits = []
        for c in courses:
            cid = getattr(c, 'c_id', getattr(c, 'id', None))
            cred = getattr(c, 'c_credits', getattr(c, 'credits', 0))

            if cid in self.marks:
                score.append(self.marks[cid])
                credits.append(cred)

        if not score or sum(credits) == 0:
            self.gpa = 0.0
            self.w_gpa = 0.0
            return

        score_arr = np.array(score)
        credits_arr = np.array(credits)

        raw_avg = np.average(score_arr)
        raw_w_avg = np.average(score_arr, weights=credits_arr)

        self.gpa = math.floor(raw_avg * 10) / 10
        self.w_gpa = math.floor(raw_w_avg * 10) / 10
    
    def __str_(self):
        return f"ID: {id_s}, Name: {name_s}, DoB: {dob_s}"
