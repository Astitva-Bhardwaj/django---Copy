gradeSum = 0

print("Enter CA marks")
for i in range(1,6):
    if i==1:
        print("Enter first subject  marks")
        first_marks = float(input())
    if i==2:
        print("Enter second subject  marks")
        second_marks = float(input())
    if i==3:
        print("Enter third subject  marks")
        third_marks = float(input())
    if i==4:
        print("Enter fourth subject  marks")
        fourth_marks = float(input())
    if i==5:
        print("Enter fifth subject  marks")
        fifth_marks = float(input())
sum_ca = first_marks + second_marks + third_marks + fourth_marks + fifth_marks
    
   


print("Enter your Mid Term marks")
for i in range(1,6):
    if i==1:
        print("Enter first subject  marks")
        first_marks = float(input())
    if i==2:
        print("Enter second subject  marks")
        second_marks = float(input())
    if i==3:
        print("Enter third subject  marks")
        third_marks = float(input())
    if i==4:
        print("Enter fourth subject  marks")
        fourth_marks = float(input())
    if i==5:
        print("Enter fifth subject  marks")
        fifth_marks = float(input())
sum_midterm = first_marks + second_marks + third_marks + fourth_marks + fifth_marks

grade = ''


def gpa_calculator(grades):
    points = 0
    i = 0
    grade_c = {"A":4,"A-":3.67,"B+":3.33,"B":3.0,"B-":2.67, "C+":2.33,"C":2.0,"C-":1.67,"D+":1.33,"D":1.0,"F":0}
    if grades != []:
        for grade in grades:
            points += grade_c[grade]
        gpa = points / len(grades)
        return gpa
    else:
        return None
 
 
grades = [ 'A', 'B', 'A', 'C']
print(gpa_calculator(grades))

grades = ['A', 'B', 'C', 'F', 'A', 'B+']
print(gpa_calculator(grades))