import imp
from django.contrib import admin
from django.urls import path,include
from first import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login ,name= 'login'),
    path('b.tech', views.login_semester,name='login_semester'),
    path('b.tech/2', views.btech_2,name='B.tech_2'),
    path('contact', views.contact,name='Contact'),
    path('b.tech/2/cse', views.cse,name='cse'),
    path('b.tech/2/cse/books', views.book,name='book'),
    path('b.tech/2/cse/learn', views.learn,name='Learn'),
    path('b.tech/2/cse/learn/unit1',views.unit1,name='Unit-1'),
    path('b.tech/2/cse/learn/unit2',views.unit2,name='Unit-2'),
    path('b.tech/2/cse/learn/unit3',views.unit3,name='Unit-3'),
    path('b.tech/2/cse/learn/unit4',views.unit4,name='Unit-4'),
    path('b.tech/2/cse/learn/unit5',views.unit5,name='Unit-5'),
    path('b.tech/2/cse/assigment',views.assigment_main,name='Assigment'),
    path('b.tech/2/cse/assigment1',views.assigment1,name='Assigment'),
    path('b.tech/2/cse/assigment2',views.assigment2,name='Assigment'),
    path('b.tech/2/cse/assigment3',views.assigment3,name='Assigment'),
    path('b.tech/2/cse/assigment4',views.assigment4,name='Assigment'),
    path('b.tech/2/cse/assigment5',views.assigment5,name='Assigment'),
    path('b.tech/2/cse/ppt',views.ppt,name='Ppt'),
    path('b.tech/2/cse/paper',views.paper,name='Paper'),
    path('b.tech/2/cse/quiz',views.quiz,name='Paper'),    
    path('b.tech/2/cse/final',views.final,name='final'),    
    path('b.tech/2/cse/quiz_year',views.quiz_year,name='final'),
    path('b.tech/2/cse/midterm_year',views.midterm_year,name='final'),
    path('b.tech/2/cse/final_year',views.final_year,name='final'),

    # maths links start from here
    path('b.tech/2/maths',views.maths,name='maths'),
    path('b.tech/2/maths/books',views.mth_book,name='maths books'),
    path('b.tech/2/maths/assigment',views.mth_assigment,name='maths books'),
    path('b.tech/2/maths/assigment1',views.mth_assigment1,name='Assigment'),
    path('b.tech/2/maths/assigment2',views.mth_assigment2,name='Assigment'),
    path('b.tech/2/maths/assigment3',views.mth_assigment3,name='Assigment'),
    path('b.tech/2/maths/assigment4',views.mth_assigment4,name='Assigment'),
    path('b.tech/2/maths/assigment5',views.mth_assigment5,name='Assigment'),
    path('b.tech/2/maths/paper',views.mth_paper,name='Paper'),
    path('b.tech/2/maths/quiz_year',views.mth_quiz_year,name='final'),
    path('b.tech/2/maths/midterm_year',views.mth_midterm_year,name='final'),
    path('b.tech/2/maths/final_year',views.mth_final_year,name='final'),
    path('b.tech/2/maths/quiz',views.mth_quiz,name='Paper'), 
    path('b.tech/2/maths/learn', views.mth_learn,name='Learn'),
    path('b.tech/2/maths/learn/unit1',views.mth_unit1,name='Unit-1'),
    path('b.tech/2/maths/learn/unit2',views.mth_unit2,name='Unit-2'),
    path('b.tech/2/maths/learn/unit3',views.mth_unit3,name='Unit-3'),
    path('b.tech/2/maths/learn/unit4',views.mth_unit4,name='Unit-4'),
    path('b.tech/2/maths/learn/unit5',views.mth_unit5,name='Unit-5'),
    

    
    path('b.tech/2/template/calculate_gpa', views.calculate_gpa,name='calculate_gpa')
    




    
]