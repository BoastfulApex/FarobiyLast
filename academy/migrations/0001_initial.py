# Generated by Django 4.1.4 on 2023-02-22 11:25

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
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('question_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('question_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('answer_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('answer_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('answer_en', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.category')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('top', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.category')),
            ],
        ),
    ]