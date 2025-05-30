# Generated by Django 5.2 on 2025-04-15 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_remove_student_group_student_course_student_faculty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relative',
            options={'ordering': ['relationship'], 'verbose_name': 'Rodstvennik', 'verbose_name_plural': 'Rodstvenniki'},
        ),
        migrations.RemoveField(
            model_name='relative',
            name='phone',
        ),
        migrations.AddField(
            model_name='relative',
            name='birth_date',
            field=models.DateField(default='1970-01-01', verbose_name='Doglan wagty'),
        ),
        migrations.AddField(
            model_name='relative',
            name='birth_place',
            field=models.CharField(blank=True, max_length=150, verbose_name='Doglan ýeri'),
        ),
        migrations.AddField(
            model_name='relative',
            name='work_place',
            field=models.CharField(blank=True, max_length=200, verbose_name='Işleýän ýeri'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Ýaşaýan ýeri'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='full_name',
            field=models.CharField(max_length=150, verbose_name='FIO'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='relationship',
            field=models.CharField(choices=[('father', 'Atasy'), ('mother', 'Enesi'), ('grandfather', 'Babasy'), ('grandmother', 'Mamasy'), ('sister', 'Kakasy'), ('brother', 'Ejesi'), ('female_sibling', 'Ayal dogany'), ('male_sibling', 'Erkek dogany')], max_length=20, verbose_name='Garindashlyk derejesi'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatives', to='students.student', verbose_name='Talyp'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.IntegerField(choices=[(1, '1-nji kurs'), (2, '2-nji kurs'), (3, '3-nji kurs'), (4, '4-nji kurs'), (5, '5-nji kurs')], default=3, verbose_name='Kurs'),
        ),
    ]
