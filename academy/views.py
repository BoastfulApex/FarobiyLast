from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        return super(LoginView, self).post(request, format=None)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

# class SubCategoryView(viewsets.ModelViewSet):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
#     def list(self, request, *args, **kwargs):
#         category_id = request.GET.get('category_id')
#         if category_id:
#             datas = SubCategory.objects.values().filter(category__id=category_id).first()
#             return Response(datas)            
#         else:
#             datas = SubCategory.objects.all().values()
#             return Response(datas)
    
class SubCategoryView(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        return SubCategory.objects.select_related('category')

    def list(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        if category_id:
            subcategories = self.get_queryset().filter(category__id=category_id)
            serializer = self.get_serializer(subcategories, many=True)
            return Response(serializer.data)            
        else:
            subcategories = self.get_queryset().all()
            serializer = self.get_serializer(subcategories, many=True)
            return Response(serializer.data)

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
    def list(self, request, *args, **kwargs):
        category_id = request.GET.get('subcategory_id')
        if category_id:
            datas = Course.objects.filter(sub_category__id=category_id).all()
            data = []
            for course in datas:
                file = []
                if course.image:
                    file = {
                        "id": course.image.id,
                        "file": course.image.fileUrl
                    }
                else:
                    file = []
                d = {
                    "id": course.id,
                    "name_uz": course.name_uz,
                    "name_en": course.name_en,
                    "name_ru": course.name_ru,
                    "description_uz": course.description_uz,
                    "description_en": course.description_en,
                    "description_ru": course.description_ru,
                    "about_uz": course.about_uz,
                    "about_en": course.about_en,
                    "about_ru": course.about_ru,
                    "image": file
                }
                data.append(d)
            
            return Response(datas)            
        else:
            datas = Course.objects.all()
            data = []
            for course in datas:
                file = []
                if course.image:
                    file = {
                        "id": course.image.id,
                        "file": course.image.fileUrl
                    }
                else:
                    file = []
                d = {
                    "id": course.id,
                    "name_uz": course.name_uz,
                    "name_en": course.name_en,
                    "name_ru": course.name_ru,
                    "description_uz": course.description_uz,
                    "description_en": course.description_en,
                    "description_ru": course.description_ru,
                    "about_uz": course.about_uz,
                    "about_en": course.about_en,
                    "about_ru": course.about_ru,
                    "image": file
                }
                data.append(d)
            
            return Response(data)            
    
    
    def retrieve(self, request, *args, **kwargs):
        course_id = kwargs['pk']
        course = Course.objects.values().filter(id=course_id).first()
        if course:
            descriptions = CourseDescription.objects.values().filter(course__id=course_id).all()
            course["descriptions"]=descriptions
            return Response(course)
        else:
            return Response({"detail": "not found"})

# class CourseView(viewsets.ModelViewSet):
#     serializer_class = CourseSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
#     def get_queryset(self):
#         return Course.objects.select_related('sub_category')

#     @action(detail=False, methods=['get'])
#     def list_by_subcategory(self, request):
#         category_id = request.GET.get('subcategory_id')
#         if category_id:
#             courses = self.get_queryset().filter(sub_category__id=category_id)
#             page = self.paginate_queryset(courses)
#             if page is not None:
#                 serializer = self.get_serializer(page, many=True)
#                 return self.get_paginated_response(serializer.data)
#             serializer = self.get_serializer(courses, many=True)
#             return Response(serializer.data)
#         else:
#             return self.list(request)


#     def retrieve(self, request, *args, **kwargs):
#         course_id = kwargs['pk']
#         course = self.get_queryset().filter(id=course_id).first()
#         if course:
#             serializer = self.get_serializer(course)
#             return Response(serializer.data)
#         else:
#             return Response({"detail": "not found"})


class CourseDescriptionView(viewsets.ModelViewSet):
    queryset = CourseDescription.objects.all()
    serializer_class = CourseDescriptionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
      
class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    
    def list(self, request, *args, **kwargs):
        sliders = self.get_queryset()   
        data = []
        for slider in sliders:
            file = []
            if slider.image:
                file = {
                    "id": slider.image.id,
                    "file": slider.image.fileUrl
                }
            else:
                file = []
            d = {
                "id": slider.id,
                "name_uz": slider.name_uz,
                "name_en": slider.name_en,
                "name_ru": slider.name_ru,
                "description_uz": slider.description_uz,
                "description_en": slider.description_en,
                "description_ru": slider.description_ru,
                "image": file
            }
            data.append(d)
                 
        return Response(data)    
    
class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def list(self, request, *args, **kwargs):
        teachers = self.get_queryset()   
        data = []
        for teacher in teachers:
            file = []
            if teacher.image:
                file = {
                    "id": teacher.image.id,
                    "file": teacher.image.fileUrl
                }
            else:
                file = []
            d = {
                "id": teacher.id,
                "name_uz": teacher.name_uz,
                "name_en": teacher.name_en,
                "name_ru": teacher.name_ru,
                "description_uz": teacher.description_uz,
                "description_en": teacher.description_en,
                "description_ru": teacher.description_ru,
                "image": file
            }
            data.append(d)
                 
        return Response(data)    


class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class FileView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def create(self, request, *args, **kwargs):
        image_id = self.request.query_params.get('id')
        if image_id:
            file = File.objects.get(id=image_id)
            file.file = request.data['file']
            data = {
                'id': file.id,
                'file': file.fileUrl
            }
            file.save()
            return Response(data)
        else:        
            file = File.objects.create(
                file = request.data['file']
            )
            file.save()
            data  = {
                "id": file.id,
                "file": file.fileUrl
            }
            return Response(data)