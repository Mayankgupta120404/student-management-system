# Dictionary to store student information
students = {
    101: {'name': 'Alice', 'age': 15, 'grade': '10th', 'contact': 'alice@example.com'},
    102: {'name': 'Bob', 'age': 16, 'grade': '11th', 'contact': 'bob@example.com'},
    103: {'name': 'Charlie', 'age': 14, 'grade': '9th', 'contact': 'charlie@example.com'}
}

# Accessing student information by ID
student_id = 102
print(f"Student ID: {student_id}")
print(f"Name: {students[student_id]['name']}")
print(f"Age: {students[student_id]['age']}")
print(f"Grade: {students[student_id]['grade']}")
print(f"Contact: {students[student_id]['contact']}")
