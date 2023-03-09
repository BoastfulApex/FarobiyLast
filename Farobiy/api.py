from academy.views import*
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'sliders', SliderView, basename='sliders')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'sub_categories', SubCategoryView, basename='sub_categories')
router.register(r'courses', CourseView, basename='courses')
router.register(r'course_descriptions', CourseDescriptionView, basename='course_descriptions')
router.register(r'teachers', TeacherView, basename='teachers')
router.register(r'faqs', FAQView, basename='faqs')
router.register(r'files', FileView, basename='files')