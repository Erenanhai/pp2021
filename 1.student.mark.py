# Database
Student = []

Course = []

Mark = []

# Input Student Info (Id, Name, DoB)
def inpStudent(s):
    Id = str(input(f'Student ID no {s+1} : '))
    Name = str(input(f'Name: '))
    DoB = str(input(f'DoB: '))
    St = {"studentId": Id, "studentName": Name, "studentDoB": DoB}
    return St

# Input Course Info (cID, cName)
def inpCourse(c):
    cId = str(input(f'Course ID {c+1}: '))
    cName = str(input(f'Course Name: '))
    Cs = {'courseId': cId, 'courseName': cName}
    return Cs 


# Mark
def MarkStudent(cid, sid):
    mk = input('Mark for student ' + Student[cid]['studentId'] + ' : ')
    return mk


'''
# Listing
def List():
    # Courses
    # Students
    # Mark
'''

stNum = int(input('Number of students: '))
for stIndex in range(stNum):
    st = inpStudent(stIndex)
    Student += [st]

csNum = int(input('Number of courses: '))
for csIndex in range(csNum):
    cs = inpCourse(csIndex)
    Course += [cs]

print(Student)

print(Course)
