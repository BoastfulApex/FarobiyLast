# Generated by Django 4.1.4 on 2023-02-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_remove_course_top'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.category')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.subcategory'),
        ),
    ]
