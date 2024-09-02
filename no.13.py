print("batch of student")

student = int(input("number of students enrolled: "))

batch = student // 30
left = student % 30

print(f"by {student} students enrolled, there will be {batch} sections and {left} students will be left over.")