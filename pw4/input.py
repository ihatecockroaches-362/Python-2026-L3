from domains import Students, Courses


def input_number_of_students():
    return int(input("Enter the number of students: ").strip())


def input_students_info(num_student):
    students = []
    for i in range(num_student):
        id_s = input(f"ID for student {i+1}: ").strip()
        name_s = input(f"Student {i+1}'s name: ").strip()
        dob_s = input(f"Student {i+1}'s DoB: ").strip()
        students.append(Students(id_s, name_s, dob_s))
    return students


def input_number_of_courses():
    return int(input("Enter the number of class: ").strip())


def input_courses_info(num_courses):
    courses = []
    for i in range(num_courses):
        c_id = input(f"Class ID {i+1}: ").strip()
        c_name = input(f"Class {i+1} name: ").strip()
        c_credits = int(input(f"Class {i+1} credits: ").strip())
        courses.append(Courses(c_id, c_name, c_credits))
    return courses


def input_marks(courses, students, marks):
    if not courses:
        print("No courses available.")
        return

    for i in range(len(courses)):
        chosen_cid = input(f"Enter the class ID for input marks in class {i+1}: ").strip()

        # Check against course objects using their course ID attribute
        matched_course = next((c for c in courses if getattr(c, 'c_id', getattr(c, 'id', None)) == chosen_cid), None)
        if not matched_course:
            print("error : no course id")
            return

        if chosen_cid not in marks:
            marks[chosen_cid] = {}

        print(f"\nEnter the student's marks for class: {chosen_cid}")
        for s in students:
            s_id = getattr(s, 'id_s', getattr(s, 'id', ''))
            s_name = getattr(s, 'name_s', getattr(s, 'name', ''))
            
            score = float(input(f"Mark for {s_id}-{s_name}: "))
            marks[chosen_cid][s_id] = score
            s.input_marks(chosen_cid, score)

def search_for_class():
    return input("Enter the class ID you want to search: ").strip()