class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of student objects
if __name_+ == "_main_":
    students = [
        Student("Alice", "A123", 3.9),
        Student("Bob", "B456", 3.5),
        Student("Charlie", "C789", 4.0),
        Student("David", "D012", 3.8),
    ]

    sorted_students = sort_students(students)

    print("Sorted Students:")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
