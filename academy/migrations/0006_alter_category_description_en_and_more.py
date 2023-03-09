# Generated by Django 4.1.4 on 2023-03-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_coursedescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_uz',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_en',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_uz',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='description_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='description_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='description_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='name_en',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='coursedescription',
            name='name_uz',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='description_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='description_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='description_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name_en',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='name_uz',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name_uz',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description_en',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description_ru',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description_uz',
            field=models.TextField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name_en',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name_uz',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]