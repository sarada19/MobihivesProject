from django.contrib import admin
from django.urls import path
from mobihivesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Student Details Sections
    path("Create/", Student_mark_obtained.as_view()),
    path("Update/<str:id>", update_student_mark_obtained.as_view()),
    # Create Student Sections
    path("Create-Student/",Create_student.as_view()),
    path("Update-student/<str:id>", Update_student.as_view()),
    # Create Subject Sections
    path("Create-Subject/",Create_Subject.as_view()),
    path("Update-Subject/<str:id>", Update_Subject.as_view()),
    # Create ClassRoom Sections
    path("Create-Class-Room/", Create_classroom.as_view()),
    path("Update-Class-Room/<str:id>", Update_classroom.as_view()),
]
