from django.db import models
from mobihivesapp.firebase import firebase_config

class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        db_table = 'Class Room Table'
        managed = True
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        data = {
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'classroom': self.classroom.name,
        }
        firebase_config().child("Class Room").push(data)
    
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        data = {
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'classroom': self.classroom.name,
        }
        firebase_config().child("Subject").push(data)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='Classroom')
    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        db_table = 'Student Table'
        managed = True
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        data = {
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'classroom': self.classroom.name,
        }
        firebase_config().child("Students").push(data)
        
        
class MarksObtained(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='Subject')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Student')
    marks = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.student.name)
    
    class Meta:
        db_table = 'Marks Table'
        managed = True
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        data = {
            'Subject': self.subject.name,
            'Student Name': self.student.name,
            'Student Age': self.student.age,
            'Student grade': self.student.grade,
            'Class Room': self.student.classroom.name,
            'Mark': self.marks 
        }
        firebase_config().child('Student Details').push(data)