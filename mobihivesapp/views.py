import logging
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mobihivesapp.firebase import firebase_config

logger = logging.getLogger("info")

class Create_student(APIView):
    serializer_class = opreation_serializer
    def get(self, request):
        data = Student.objects.all()
        serializer = self.serializer_class(data, many = True)
        return Response(serializer.data)
            
    
    def post(self, request):
        data = request.data
        if data.get('name') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Name key was missing"})
        elif data.get('age') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Age key was missing"})
        elif data.get('grade') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Grade key was missing"})
        elif data.get('classroom') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Class Room key was missing"})
        else: 
            serializer = self.serializer_class(data= data)
            if serializer.is_valid():
                serializer.save()
                firebase_config().child('Students').push(serializer.data)
                return Response(
                    {
                        "Status": status.HTTP_201_CREATED,
                        "Result": serializer.data
                    }
                )
            return Response(
                {
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Result" : "Can Not Store Result some fields are None"
                }
            )
    
class Update_student(APIView):
    serializer_class = opreation_serializer
    def get(self,request,id):
        instance = Student.objects.filter(id=id)
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)
    def put(self, request,id):
        instance = Student.objects.get(id=id)
        data = request.data
        serializer = self.serializer_class(instance, data= data)
        if serializer.is_valid():
            serializer.save()
            firebase_config().child('Students').update(serializer.data)
            return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : serializer.data
                }
            )
        return Response(
            {
                "Status": status.HTTP_404_NOT_FOUND,
                "Result" : "Can Not Store Result some fields are None"
            }
        )
            
    def delete(self, request,id):
        instance = Student.objects.get(id=id)
        instance.delete()
        firebase_config().child('Students').remove()
        return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : "Deleted"
                }
            )
  
    
class Create_classroom(APIView):
    serializer_class = ClassRoomserializer
    def get(self, request):
        data = Classroom.objects.all()
        serializer = self.serializer_class(data, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        if data.get('name') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Name key was missing"})
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            firebase_config().child('Class Room').push(serializer.data)
            return Response(
                {
                    "Status": status.HTTP_201_CREATED,
                    "Result": serializer.data
                }
            )
        return Response(
            {
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Result" : "Can Not Store Result some fields are None"
            }
        )
    
class Update_classroom(APIView):
    serializer_class = ClassRoomserializer
    def get(self,request,id):
        instance = Classroom.objects.filter(id=id)
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)
    def put(self, request,id):
        instance = Classroom.objects.get(id=id)
        data = request.data
        serializer = self.serializer_class(instance, data= data)
        if serializer.is_valid():
            serializer.save()
            firebase_config().child('Class Room').update(serializer.data)
            return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : serializer.data
                }
            )
        return Response(
            {
                "Status": status.HTTP_404_NOT_FOUND,
                "Result" : "Can Not Store Result some fields are None"
            }
        )
            
    def delete(self, request,id):
        instance = Classroom.objects.get(id=id)
        instance.delete()
        firebase_config().child('Class Room').remove()
        return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : "Deleted"
                }
            )
    
    
class Create_Subject(APIView):
    serializer_class = SubjectSerializer
    def get(self, request):
        data = Subject.objects.all()
        serializer = self.serializer_class(data, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        if data.get('name') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Name key was missing"})
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            firebase_config().child('Subject').push(serializer.data)
            return Response(
                {
                    "Status": status.HTTP_201_CREATED,
                    "Result": serializer.data
                }
            )
        return Response(
            {
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Result" : "Can Not Store Result some fields are None"
            }
        )
    
class Update_Subject(APIView):
    serializer_class = SubjectSerializer
    def get(self,request,id):
        instance = Subject.objects.filter(id=id)
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)
    def put(self, request,id):
        instance = Subject.objects.get(id=id)
        data = request.data
        serializer = self.serializer_class(instance, data= data)
        if serializer.is_valid():
            serializer.save()
            firebase_config().child('Subject').update(serializer.data)
            return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : serializer.data
                }
            )
        return Response(
            {
                "Status": status.HTTP_404_NOT_FOUND,
                "Result" : "Can Not Store Result some fields are None"
            }
        )
            
    def delete(self, request,id):
        instance = Subject.objects.get(id=id)
        instance.delete()
        firebase_config().child('Subject').remove()
        return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : "Deleted"
                }
            )


class Student_mark_obtained(APIView):
    serializer_class = Student_details_serializers
    
    def get(self, request):
        data = MarksObtained.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        data = request.data
        if data.get('marks') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Mark key was missing"})
        elif data.get('subject') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Subject key was missing"})
        elif data.get('student') is None:
            return Response({"Status": status.HTTP_204_NO_CONTENT, "Result": "Student key was missing"})
        else: 
            serializer = self.serializer_class(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "Status": status.HTTP_201_CREATED,
                        "Result": serializer.data
                    }
                )
            return Response(
                {
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Result" : "Can Not Store Result some fields are None"
                }
            )
        
class update_student_mark_obtained(APIView):
    serializer_class = Student_details_serializers
    def get(self,request,id):
        instance = MarksObtained.objects.filter(id=id)
        serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data)
    def put(self, request,id):
        instance = MarksObtained.objects.get(id=id)
        data = request.data
        serializer = self.serializer_class(instance, data= data)
        if serializer.is_valid():
            serializer.save()
            firebase_config().child('Student Details').update(serializer.data)
            return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : serializer.data
                }
            )
        return Response(
            {
                "Status": status.HTTP_404_NOT_FOUND,
                "Result" : "Can Not Store Result some fields are None"
            }
        )
            
    def delete(self, request,id):
        instance = MarksObtained.objects.get(id=id)
        instance.delete()
        firebase_config().child('Student Details').remove()
        return Response(
                {
                    "Status": status.HTTP_202_ACCEPTED,
                    "Result" : "Deleted"
                }
            )