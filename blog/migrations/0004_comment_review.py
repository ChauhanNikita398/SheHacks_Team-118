# Generated by Django 3.1 on 2021-03-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.BooleanField(default=True),
        ),
    ]
