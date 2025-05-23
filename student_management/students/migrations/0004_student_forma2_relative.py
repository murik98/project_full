# Generated by Django 5.2 on 2025-04-13 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_options_student_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='forma2',
            field=models.TextField(blank=True, null=True, verbose_name='Форма 2'),
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО родственника')),
                ('relationship', models.CharField(choices=[('father', 'Отец'), ('mother', 'Мать'), ('grandfather', 'Дед'), ('grandmother', 'Бабушка'), ('sister', 'Сестра'), ('brother', 'Брат')], max_length=20, verbose_name='Родство')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatives', to='students.student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Родственник',
                'verbose_name_plural': 'Родственники',
            },
        ),
    ]
