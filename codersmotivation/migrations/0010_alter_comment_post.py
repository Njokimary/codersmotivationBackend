# Generated by Django 3.2.1 on 2023-03-22 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codersmotivation', '0009_auto_20230319_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='codersmotivation.post'),
        ),
    ]
