# This module contains operations related to sets.

def unique_majors(student_list):
    majors = {student[2] for student in student_list}
    return majors
