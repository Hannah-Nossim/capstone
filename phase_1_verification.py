""" add a new student,
 find top student automatically,
sort by score,
add letter grades.
 """

# A list of students and their scores
students = [
    ("Alice", 88),
    ("Bob",   72),
    ("Carol", 95),
    ("Dave",  61),
    ("Eve",   79),
]

# Calculate the average
total = 0
for name, score in students:
    total = total + score

average = total / len(students)

# Print each student's result
print("--- Student Report ---")
for name, score in students:
    if score >= average:
        result = "PASS"
    else:
        result = "below average"
    print(name + ": " + str(score) + " — " + result)

# Print the summary
print("")
print("Class average: " + str(average))
print("Top student:   " + students[0][0])

#add a student
students.append(("Joy",89))

#find top student automatically
students.sort(key=lambda x: x[1], reverse=True
)
print("Top student:   " + students[0][0])

#sort by score
print("--- Student Report (sorted by score) ---")
students.sort(key=lambda x: x[1], reverse=True)
for name, score in students:
    if score >= average:
        result = "PASS"
    else:
        result = "below average"
    print(name + ": " + str(score) + " — " + result)

#add letter grades
print("--- Student Report (with letter grades) ---")
for name, score in students:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(name + ": " + str(score) + " — Grade: " + grade)
