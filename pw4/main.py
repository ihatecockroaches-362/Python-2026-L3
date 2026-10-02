import input as inp
import output as out

def main():
    num_students = inp.input_number_of_students()
    students = inp.input_students_info(num_students)

    num_courses = inp.input_number_of_courses()
    courses = inp.input_courses_info(num_courses)

    out.list_students(students)
    out.list_courses(courses)
    marks = {}
    inp.input_marks(courses, students,marks)

    chosen_cid = inp.search_for_class()
    out.show_students_marks(students, chosen_cid)

    for s in students:
        s.calculate_gpas(courses)
    out.gpa_ranking(students)

if __name__ == "__main__":
    main()