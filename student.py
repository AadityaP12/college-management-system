

students=[]

def add_student(student):

    students.append(student)
    print(students)


def search_student(sdt_id):

    for st in students:

        print(st)

        if sdt_id==st["student_id"]:
            return st[sdt_id]


    return students[student_id]

def display_student(student_id):

    return students[student_id]


student_data={"student_id":"1", "name": "Aaditya"}
student_data2={"student_id":"2", "name": "Brian"}


add_student(student_data)
add_student(student_data2)

print(search_student(1))