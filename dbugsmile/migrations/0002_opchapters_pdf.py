# Generated by Django 5.0.3 on 2024-03-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbugsmile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opchapters',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf'),
        ),
    ]
