from ast import Return
import re
from django.shortcuts import render,HttpResponse

# Create your views here.
def check(request):
    return HttpResponse("Hello world")

def login(request):
    return render(request , 'login_course.html')

def login_semester(request):
    return render(request , 'login_semester.html')

def btech_2(request):
    return render(request, 'btech_2.html')

def contact(request):
    return render(request, 'contact_us.html')

def cse(request):
    return render(request,'cse.html')

def book(request):
    return render(request,'books.html')

def learn(request):
    return render(request,'learn.html')

def unit1(request):
    return render(request,'unit/unit1.html')
def unit2(request):
    return render(request,'unit/unit2.html')
def unit3(request):
    return render(request,'unit/unit3.html')
def unit4(request):
    return render(request,'unit/unit4.html')
def unit5(request):
    return render(request,'unit/unit5.html')

def assigment_main(request):
    return render(request,'assigment_main.html')
def assigment1(request):
    return render(request,'assigment/assigment1.html')
def assigment2(request):
    return render(request,'assigment/assigment2.html')
def assigment3(request):
    return render(request,'assigment/assigment3.html')
def assigment4(request):
    return render(request,'assigment/assigment4.html')
def assigment5(request):
    return render(request,'assigment/assigment5.html')
def ppt(request):
    return render(request,'ppt.html')

def paper(request):
    return render(request,'paper.html')

def quiz(request):
    return render(request,'quiz.html')

def final(request):
    return render(request,'final.html')

def quiz_year(request):
    return render(request,'quiz_year.html')

def midterm_year(request):
    return render(request,'midterm_year.html')

def final_year(request):
    return render(request,'final_year.html')

#MATHS START FROM HERE
def maths(request):
    return render(request,'MATHS/MTH.html')
def mth_book(request):
    return render(request,'MATHS/book.html')
def mth_assigment(request):
    return render(request,'MATHS/assigment_main.html')

def mth_assigment1(request):
    return render(request,'MATHS/assigment/assigment1.html')
def mth_assigment2(request):
    return render(request,'MATHS/assigment/assigment2.html')
def mth_assigment3(request):
    return render(request,'MATHS/assigment/assigment3.html')
def mth_assigment4(request):
    return render(request,'MATHS/assigment/assigment4.html')
def mth_assigment5(request):
    return render(request,'MATHS/assigment/assigment5.html')
def mth_paper(request):
    return render(request,'MATHS/paper.html')
def mth_quiz_year(request):
    return render(request,'MATHS/quiz_year.html')

def mth_midterm_year(request):
    return render(request,'MATHS/midterm_year.html')

def mth_final_year(request):
    return render(request,'MATHS/final_year.html')

def mth_quiz(request):
    return render(request,'MATHS/quiz.html')

def mth_learn(request):
    return render(request,'MATHS/learn.html')

def mth_unit1(request):
    return render(request,'MATHS/unit/unit1.html')
def mth_unit2(request):
    return render(request,'MATHS/unit/unit2.html')
def mth_unit3(request):
    return render(request,'MATHS/unit/unit3.html')
def mth_unit4(request):
    return render(request,'MATHS/unit/unit4.html')
def mth_unit5(request):
    return render(request,'MATHS/unit/unit5.html')

def calculate_gpa(request):
    return render(request,'template/calculate_gpa.html')


# EEE start from here 