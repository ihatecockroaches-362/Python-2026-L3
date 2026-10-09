import input as inp
import output as out
import os

def main():
    if os.path.exists("students.dat"):
        inp.decompress_files()
        students = inp.load_students()
        courses = inp.load_courses()
        inp.load_marks(students)
    else:
        num_students = inp.input_number_of_students()
        students = inp.input_students_info(num_students)
        inp.students_data(students)
        
        num_courses = inp.input_number_of_courses()
        courses = inp.input_courses_info(num_courses)
        inp.courses_data(courses)
        
        out.list_students(students)
        out.list_courses(courses)
        
        marks = {}
        inp.input_marks(courses, students,marks)
        inp.marks_data(students, courses)
        inp.compress_files()

    for s in students:
        s.calculate_gpas(courses)
        
    chosen_cid = inp.search_for_class()
    out.show_students_marks(students, chosen_cid)
    out.gpa_ranking(students)
if __name__ == "__main__":
    main()