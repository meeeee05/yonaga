# Generated by Django 4.1.2 on 2022-10-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
