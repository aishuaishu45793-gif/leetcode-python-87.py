student1 = {
    "name": "Aishu",
    "age": 21
}

student2 = {
    "course": "Python",
    "marks": 90
}

merged_student = {**student1, **student2}

print("Merged dictionary:", merged_student)