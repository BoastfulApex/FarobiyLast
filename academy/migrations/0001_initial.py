# Generated by Django 4.1.4 on 2023-04-15 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=20000, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=200000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=20000, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('about_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('about_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('about_en', models.TextField(blank=True, max_length=200000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('question_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('question_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('answer_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('answer_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('answer_en', models.TextField(blank=True, max_length=200000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=20000, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_icon', to='academy.file')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_image', to='academy.file')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=20000, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.category')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.file')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=20000, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.file')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=20000, null=True)),
                ('name_en', models.CharField(blank=True, max_length=20000, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.file'),
        ),
        migrations.AddField(
            model_name='course',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.subcategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.file'),
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_uz', models.TextField(blank=True, max_length=200000, null=True)),
                ('about_ru', models.TextField(blank=True, max_length=200000, null=True)),
                ('about_en', models.TextField(blank=True, max_length=200000, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.file')),
            ],
        ),
    ]