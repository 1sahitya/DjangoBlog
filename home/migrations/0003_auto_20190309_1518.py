# Generated by Django 2.1.7 on 2019-03-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]
