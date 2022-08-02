students = {"John":["Python","Django","DRF"], "Bob":["Java","Spring"], "Jim":["js","node", "react"]}
keys = students.keys()
for key in keys:
    print(f"Courses taken by {key} are: ")
    for course in students[key]:
        print(course)