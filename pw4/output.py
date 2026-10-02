from domains import Students, Courses
def list_students(students : list):
    for i,s in enumerate(students, 1):
        print(f"Student {i}: ID: {s.id_s}, name:{s.name_s}, DoB:{s.dob_s}")
        i += 1

def list_courses(courses: list):
    for c in courses:
        print(f"Class ID: {c.c_id}, Class Name: {c.c_name}, Class credits: {c.c_credits}")

def show_students_marks(students: list, chosen_cid:str):
    found = False
    for s in students:
        if chosen_cid in s.marks:
            found = True
            print(f"ID: {s.id_s} Name: {s.name_s} Marks: {s.marks[chosen_cid]}")
        
def gpa_ranking(students: list):
    sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
    for i, s in enumerate(sorted_students, 1):
        print(f"{i}. Student: {s.name_s}, ID: {s.id_s}, GPA: {s.gpa}, Weighted GPA: {s.w_gpa}")