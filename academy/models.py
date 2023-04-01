from django.db import models


class Slider(models.Model):
    name_uz = models.CharField(max_length=20000, null=True, blank=True)
    name_ru = models.CharField(max_length=20000, null=True, blank=True)
    name_en = models.CharField(max_length=20000, null=True, blank=True)
    description_uz = models.TextField(max_length=200000, null=True, blank=True)
    description_ru = models.TextField(max_length=200000, null=True, blank=True)
    description_en = models.TextField(max_length=200000, null=True, blank=True)
    image = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True, blank=True)


class Category(models.Model):
    name_uz = models.CharField(max_length=20000, null=True, blank=True)
    name_ru = models.CharField(max_length=20000, null=True, blank=True)
    name_en = models.CharField(max_length=20000, null=True, blank=True)
    description_uz = models.TextField(max_length=200000, null=True, blank=True)
    description_ru = models.TextField(max_length=200000, null=True, blank=True)
    description_en = models.TextField(max_length=200000, null=True, blank=True)
    image = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_uz


class SubCategory(models.Model):
    name_uz = models.CharField(max_length=20000, null=True, blank=True)
    name_ru = models.CharField(max_length=20000, null=True, blank=True)
    name_en = models.CharField(max_length=20000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description_uz = models.TextField(max_length=200000, null=True, blank=True)
    description_ru = models.TextField(max_length=200000, null=True, blank=True)
    description_en = models.TextField(max_length=200000, null=True, blank=True)
    image = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_uz


class Course(models.Model):
    name_uz = models.CharField(max_length=20000, null=True, blank=True)
    name_ru = models.CharField(max_length=20000, null=True, blank=True)
    name_en = models.CharField(max_length=20000, null=True, blank=True)
    description_uz = models.TextField(max_length=200000, null=True, blank=True)
    description_ru = models.TextField(max_length=200000, null=True, blank=True)
    description_en = models.TextField(max_length=200000, null=True, blank=True)
    about_uz = models.TextField(max_length=200000, null=True, blank=True)
    about_ru = models.TextField(max_length=200000, null=True, blank=True)
    about_en = models.TextField(max_length=200000, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name_uz
    
        
class Teacher(models.Model):
    name_uz = models.CharField(max_length=20000, null=True, blank=True)
    name_ru = models.CharField(max_length=20000, null=True, blank=True)
    name_en = models.CharField(max_length=20000, null=True, blank=True)
    description_uz = models.TextField(max_length=200000, null=True, blank=True)
    description_ru = models.TextField(max_length=200000, null=True, blank=True)
    description_en = models.TextField(max_length=200000, null=True, blank=True)
    image = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True, blank=True, related_name='teacher_image')
    icon = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True, blank=True, related_name='teacher_icon')
    
    def __str__(self):
        return self.name_uz

        
class CourseDescription(models.Model):
    name_uz = models.CharField(max_length=20000, null=True, blank=True)
    name_ru = models.CharField(max_length=20000, null=True, blank=True)
    name_en = models.CharField(max_length=20000, null=True, blank=True)
    description_uz = models.TextField(max_length=200000, null=True, blank=True)
    description_ru = models.TextField(max_length=200000, null=True, blank=True)
    description_en = models.TextField(max_length=200000, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.name_uz


class FAQ(models.Model):
    question_uz = models.TextField(max_length=200000, null=True, blank=True)
    question_ru = models.TextField(max_length=200000, null=True, blank=True)
    question_en = models.TextField(max_length=200000, null=True, blank=True)
    answer_uz = models.TextField(max_length=200000, null=True, blank=True)
    answer_ru = models.TextField(max_length=200000, null=True, blank=True)
    answer_en = models.TextField(max_length=200000, null=True, blank=True)
    
    def __str__(self):
        return self.question_uz


class About(models.Model):
    about_uz = models.TextField(max_length=200000, null=True, blank=True)
    about_ru = models.TextField(max_length=200000, null=True, blank=True)
    about_en = models.TextField(max_length=200000, null=True, blank=True)
    image = models.ForeignKey('academy.File', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_uz


class File(models.Model):
    file = models.FileField(null=True, blank=True)
    
    
    @property
    def fileUrl(self):
        try:
            return self.file.url
        except:
            return ''
        
    def __str__(self):
        return str(self.id)

