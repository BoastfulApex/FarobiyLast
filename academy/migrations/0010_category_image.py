# Generated by Django 4.1.4 on 2023-03-10 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0009_remove_category_image_remove_subcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.file'),
        ),
    ]