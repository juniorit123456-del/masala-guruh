students = {
"Eshmat" : 69,
"Toshmat" : 92,
"Ali" : 85,
"Vali" : 96,
"Sardor" : 88,
"Akmal": 54
}
jami_ball = 0

for key in students:
    jami_ball += students[key]

ortacha = jami_ball / len(students)
print(students)
for key in students:
    if students[key] > 70:
        print(f"O'quvchi: {key} - {students[key]} ball")

yuqori_ball = max(students)

print(f"Eng yuqori ball olgan o'quvchi: {yuqori_ball}")
print(f"Guruhri ortacha balli: {ortacha}")