# Generated by Django 3.0.4 on 2020-05-09 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
