from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class SliderSerializer(serializers.ModelSerializer):

    # image = serializers.SerializerMethodField()
    
    class Meta:
        model = Slider
        fields = '__all__'
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = "__all__"
        
    # def get_image(self, obj):
    #     if obj.image:
    #         return {
    #             "id": obj.image.id,
    #             "file": obj.image.fileUrl
    #         }
    #     else:
    #         return {}


class CourseDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDescription
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ['id', 'name_uz', 'name_en', 'name_ru', 'description_uz', 'description_en', 'description_ru', 'image']
        
    # def get_image(self, obj):
    #     if obj.image:
    #         return {
    #             "id": obj.image.id,
    #             "file": obj.image.fileUrl
    #         }
    #     else:
    #         return {}


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

