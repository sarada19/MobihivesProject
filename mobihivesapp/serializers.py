from .models import *
from rest_framework import serializers

class ClassRoomserializer(serializers.Serializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        
    def validate(self, data):
        if len(data['name']) == 0:
            raise serializers.ValidationError(
                {"Error": "Name can not be null"}
            )
        return data
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
    def validate(self, data):
        if len(data['name']) == 0:
            raise serializers.ValidationError(
                {"Error": "Name can not be null"}
            )
        return data

class opreation_serializer(serializers.ModelSerializer):
    Classroom = ClassRoomserializer(read_only = True, many = True)
    
    class Meta:
        model = Student
        fields = '__all__'
        
    def validate(self, data):
        if len(data['name']) == 0:
            raise serializers.ValidationError(
                {"Error": "Name can not be null"}
            )
        elif data['age'] == 0:
            raise serializers.ValidationError(
                {
                    "Error" : "Age can not be null"
                }
            )
        elif len(data['grade']) == 0:
            raise serializers.ValidationError(
                {
                    "Error":"Student Grade Require"
                }
            )
        elif data['classroom'] == 0:
            raise serializers.ValidationError(
                {
                    "Error" : "Please Select a Classroom"
                }
            )
        
        return data
    
    
class Student_details_serializers(serializers.ModelSerializer):    
    class Meta:
        model = MarksObtained
        fields = '__all__'
        
    def validate(self, data):
        if data['marks'] == 0:
            raise serializers.ValidationError(
                {"Error": "Marks can not be null"}
            )
        
        return data