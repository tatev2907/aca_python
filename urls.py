
from django.contrib import admin
from django.urls import path
from pages import views #change "pages" to your project name
urlpatterns = [
    path('', views.stud_from_db, name='stud_from_db'),
    path('add_stud/', views.add_stud, name='createstud'),
    path('add_exam/', views.add_exam, name='createexam'),
    path('add_sub/', views.add_sub, name='createsub'),
    path('add_res/', views.add_res, name='createres'),
    path('admin/', admin.site.urls),
]
