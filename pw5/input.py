from domains import Students, Courses
import zipfile

def compress_files():
    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_compress:
            zipf.write(file)

def decompress_files():
    with zipfile.ZipFile("students.dat", "r") as zipf:
        zipf.extractall()

def students_data(students):
    with open("students.txt","w") as f:
        for i,s in enumerate(students, 1):
            line = f"{s.id_s},{s.name_s},{s.dob_s}\n"
            f.write(line)
        print("written")
        
def load_students():
    students = []
    with open("students.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                id_s,name_s,dob_s = line.split(",")
                students.append(Students(id_s, name_s, dob_s))
    return students


def courses_data(courses):
    with open("courses.txt","w") as f:
        for c in courses:
            line = f"{c.c_id},{c.c_name},{c.c_credits}\n"
            f.write(line)
        print("written")

def load_courses():
    courses = []
    with open("courses.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                c_id, c_name, c_credits = line.split(",")
                courses.append(Courses(c_id, c_name, int(c_credits)))
    return courses

def marks_data(students, courses):
    with open("marks.txt","w") as f:
        for c in courses:
            for s in students:
                if c.c_id in s.marks:
                    line = f"{s.id_s},{c.c_id},{s.marks[c.c_id]}\n"
                    f.write(line)
        print("written") 
               
def load_marks(students):
    marks = []
    with open("marks.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                id_s, c_id, score = line.split(",")
                for s in students:
                    if s.id_s == id_s:
                        s.marks[c_id] = float(score)
            
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