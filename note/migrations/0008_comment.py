# Generated by Django 3.0.4 on 2020-05-08 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0007_auto_20200503_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField(blank=True, max_length=50)),
                ('rate', models.IntegerField(blank=True)),
                ('status', models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.Note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
