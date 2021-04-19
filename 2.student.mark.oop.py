#!/usr/bin/env python3

# Database




Mark = []

# Student Info (Id, Name, DoB)
class Student:
    def __init__(self, i, n, d):
        self.Id = i
        self.Name = n
        self.DoB = d

    def __str__(self):
        return f"Student ID: {self.Id}, Student Name: {self.Name}, Student DoB: {self.DoB}"


# Course Info (cID, cName)
class Course:
    def __init__(self, i, n):
        self.cId = i
        self.cName = n

    def __str__(self):
        return f"Course ID: {self.cId}, Course Name: {self.cName}"

# Input
class Input:
    def inpStudent(self):
        studentLs = []

        stNum = int(input('Number of students: '))

        while len(studentLs) < stNum:
            Id = str(input(f'Student ID: '))
            Name = str(input(f'Name: '))
            DoB = str(input(f'DoB: '))
            value = Student(Id, Name, DoB)
            studentLs.append(value)
        return studentLs
    
    def inpCourse(self):
        courseLs = []

        csNum = int(input('Number of courses: '))

        while len(courseLs) < csNum:
            cId = str(input(f'Course ID: '))
            cName = str(input(f'Course Name: '))
            value = Course(cId, cName)
            courseLs.append(value)
        return courseLs

    def inpMark(self):


class List:
    def lsStudent(self):
        

# main:
Input().inpStudent()
Input().inpCourse()