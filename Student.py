from abc import ABC,abstractmethod

class Student :
    def __init__(self,student_name,student_id, attendance_status):
        self.student_name= student_name
        self.student_id=student_id
        # self.marks= marks
        self.attendance= attendance_status


@abstractmethod
def calculate_total (sub1,sub2,sub3,sub4,sub5):
    sum1=sub1+sub2+sub3+sub4+sub5
    print(f"Total mark is : {sum1}")
    return sum1

def calculate_average(sub1,sub2,sub3,sub4,sub5):
    average =(sub1+sub2+sub3+sub4+sub5)/5
    print(f'Average Mark is : {average}')
    return calculate_average
def calculate_grade(sub1,sub2,sub3,sub4,sub5):
    average =(sub1+sub2+sub3+sub4+sub5)/5
    if average>=90:
        print('A Grade')
    elif average>=80:
        print('B grade')
    elif average>=70:
        print('c grade')
    elif average>=60:
        print('D grade')
    elif average>=50:
        print('E grade')
    elif average<40:
        print('F grade')
    else:
        print('Invalid')

def display_details(self):
    print(f"Student name : {self.student_name} | student id : {self.student_id} ")

stud1=Student('Jerin','ai11',100)
calculate_total(55,56,58,62,68)
calculate_average(55,56,58,62,68)
calculate_grade(55,56,58,62,68)

