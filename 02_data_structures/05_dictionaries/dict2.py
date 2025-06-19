student = {
    "name": "Jane",
    "age": 20,
    "grade": "A"
}

print(f"  Number of items: {len(student)}")

# Looping Through a Dictionary
for key in student:
    print(f"  {key}: {student[key]}")

# OR
for key, value in student.items():
    print(f"  {key} => {value}")

# Dictionary Keys, Values, Items
print(f"\n  Keys: {list(student.keys())}")
print(f"\n  Values: {list(student.values())}")
print(f"\n  Items: {list(student.items())} \n")

school = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

# Nested Dictionary
print(f"  student2's age: {school['student1']['age']}")



