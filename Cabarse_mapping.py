class Student:
   
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name

    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"


class Course:
    
    def __init__(self, course_code: str, course_name: str):
        self.course_code = course_code
        self.course_name = course_name
        self.students = [] 

    def add_student(self, student: Student):
        
        if isinstance(student, Student):
            self.students.append(student)
            print(f"Added {student.name} to {self.course_name}.")
        else:
            raise TypeError("Only instances of Student can be added.")

    def display_enrolled_students(self):
        print(f"\n--- Students enrolled in {self.course_code}: {self.course_name} ---")
        if not self.students:
            print("No students enrolled yet.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"{idx}. [{student.student_id}] {student.name}")



if __name__ == "__main__":
  
    python_course = Course("CS101", "Introduction to Computer Science")

    
    student1 = Student("S001", "Alice Smith")
    student2 = Student("S002", "Bob Jones")

    
    python_course.add_student(student1)
    python_course.add_student(student2)

    python_course.display_enrolled_students()
