# Generated by Django 4.2.7 on 2023-11-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_image_item_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='img',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='static/app/img/product-1.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
