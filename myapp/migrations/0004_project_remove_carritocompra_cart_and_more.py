# Generated by Django 4.1.3 on 2022-12-10 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_project_alter_platocomida_image_task_carritocompra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritocompra',
            name='cart',
        ),
        migrations.AddField(
            model_name='carritocompra',
            name='cart',
            field=models.ManyToManyField(to='myapp.platocomida'),
        ),
    ]
