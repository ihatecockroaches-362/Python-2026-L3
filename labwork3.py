import numpy as np
import math
students = []
courses = []
score =[]
marks = {}
def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_students_info(num_student):
    for i in range(num_student):
        id_s = input(f"ID for student {i+1}: ").strip()
        name_s = input(f"Student {i+1}'s name: ").strip()
        dob_s = input(f"Student {i+1}'s DoB: ").strip()
        students.append((id_s, name_s, dob_s))

def input_number_of_courses():
    return int(input("Enter the number of class: "))

def input_courses_info(num_courses):
    for i in range(num_courses):
        c_id = input(f"Class ID {i+1}: ").strip()
        c_name = input(f"Class {i+1} name: ").strip()
        c_credits = int(input(f"Class {i+1} credits: "))
        courses.append((c_id, c_name, c_credits))

def input_marks(num_courses):
    for i in range (num_courses):
        if not courses:
            return
        chosen_cid = input(f"Enter the class ID for input marks in class {i+1}: ")

        if not any(c_id == chosen_cid for c_id, c_name,_ in courses):
            print("error : no course id")
            return
        if chosen_cid not in marks:
            marks[chosen_cid] = {}
        print(f"\nEnter the student's marks for class: {chosen_cid}")

        for id_s, name_s, _ in students:
            score = float(input(f"Mark for {id_s}-{name_s}: "))
            marks[chosen_cid][id_s] = score

def list_students():
    i = 1
    for id_s, name_s, dob_s in students:
        print(f"Student {i}: ID: {id_s}, name:{name_s}, DoB:{dob_s}")
        i += 1

def list_courses():
    for c_id, c_name,_ in courses:
        print(f"Class ID: {c_id}, Class Name: {c_name}")

def show_students_marks():
    chosen_cid = input("Enter the class ID you want to search: ").strip()

    if chosen_cid not in marks or not marks[chosen_cid]:
        print("Class does not exist")
        return
    for id_s, name_s, _ in students:
        score = marks[chosen_cid][id_s]
        print(f"ID: {id_s}, Name: {name_s}, Marks: {score}")
        
def avg_gpa():
    avg ={}
    w_avg = {}
    credits = [c_credits for _, _, c_credits in courses]
    for id_s,name_s, _ in students:
        w_score = []
        score =[]
        for c_id,c_name,c_credits in courses:
            score.append(marks[c_id][id_s])
            w_score.append(marks[c_id][id_s]*c_credits)
        avg[id_s] = math.floor(np.average(score)*10)/10
        w_avg[id_s] = math.floor(np.average(score, weights = credits)*10)/10
    sorted_students = sorted(students, key=lambda s: avg[s[0]], reverse=True)
    for id_s,name_s, _ in sorted_students:
        print(f"Student: {name_s}, ID: {id_s},GPA: {avg[id_s]},Weighted GPA: {w_avg[id_s]}")

def main():
    num_student = input_number_of_students()
    input_students_info(num_student)
    num_courses = input_number_of_courses()
    input_courses_info(num_courses)
    list_students()
    list_courses()
    input_marks(num_courses)
    show_students_marks()
    avg_gpa()
if __name__ == "__main__":
    main()