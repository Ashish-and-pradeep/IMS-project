from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('register',views.register,name='register'),
    path('signin/',views.signin,name='signin'),
    path('student/',views.student,name='student'),
    path('signout/',views.singout,name='logout'),
    path('gallery/',views.gellery,name='gallery'),
    path('teacher/',views.teacher,name='teacher'),
    path('notes/',views.notes,name='notes'),

]