from django.db import models
import os

def student_photo_path(instance, filename):
    return f'students_photos/id_{instance.id}/{filename}'

class Student(models.Model):
    COURSE_CHOICES = [
        (1, '1-nji kurs'),
        (2, '2-nji kurs'),
        (3, '3-nji kurs'),
        (4, '4-nji kurs'),
        (5, '5-nji kurs'),
    ]

    FACULTY_CHOICES = [
        ('physics', 'Fizika'),
        ('mathematics', 'Matematika'),
        ('chemistry', 'Himiýa'),
        ('biology', 'Biologiýa'),
    ]

    first_name = models.CharField(max_length=50, verbose_name="Ady")
    last_name = models.CharField(max_length=50, verbose_name="Familiýasy")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="Atasynyň ady")
    birth_date = models.DateField(verbose_name="Doglan senesi")
    birth_place = models.CharField(max_length=150, verbose_name="Doglan ýeri", blank=True, null=True)
    course = models.IntegerField(choices=COURSE_CHOICES, default=3, verbose_name="Kurs")
    faculty = models.CharField(max_length=50, choices=FACULTY_CHOICES, default='physics', verbose_name="Fakultet")
    student_id = models.CharField(max_length=20, unique=True, verbose_name="Talyp ID")
    admission_year = models.PositiveIntegerField(verbose_name="Kabul edilen ýyly", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Telefon", blank=True, null=True)
    address = models.TextField(verbose_name="Ýaşaýyş salgysy", blank=True, null=True)
    photo = models.ImageField(upload_to=student_photo_path, blank=True, null=True, verbose_name="Surat")
    characteristics = models.TextField(verbose_name="Häsiýetnama")
    notes = models.TextField(verbose_name="Bellikler", blank=True, null=True)
    forma2 = models.TextField(verbose_name="Forma 2", blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('student_detail', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

    class Meta:
        verbose_name = "Talyp"
        verbose_name_plural = "Talyplar"
        ordering = ['last_name', 'first_name']
        indexes = [
            models.Index(fields=['course']),
            models.Index(fields=['faculty']),
            models.Index(fields=['student_id']),
        ]

class Relative(models.Model):
    RELATIONSHIP_CHOICES = [
        ('father', 'Atasy'),
        ('mother', 'Enesi'),
        ('grandfather', 'Babasy'),
        ('grandmother', 'Mamasy'),
        ('sister', 'Kakasy'),
        ('brother', 'Ejesi'),
        ('female_sibling', 'Aýal dogany'),
        ('male_sibling', 'Erkek dogany'),
    ]

    RELATIONSHIP_ORDER = {
        'father': 1,
        'mother': 2,
        'grandfather': 3,
        'grandmother': 4,
        'sister': 5,
        'brother': 6,
        'female_sibling': 7,
        'male_sibling': 8,
    }

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='relatives',
        verbose_name="Talyp"
    )
    full_name = models.CharField(max_length=150, verbose_name="FAA")
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, verbose_name="Garyndaşlyk derejesi")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Doglan wagty")
    birth_place = models.CharField(max_length=150, blank=True, verbose_name="Doglan ýeri")
    work_place = models.CharField(max_length=200, blank=True, verbose_name="Işleýän ýeri")
    address = models.TextField(blank=True, null=True, verbose_name="Ýaşaýan ýeri")

    def __str__(self):
        return f"{self.full_name} ({self.get_relationship_display()})"

    class Meta:
        verbose_name = "Garyndaş"
        verbose_name_plural = "Garyndaşlar"
        ordering = ['relationship']

class StudentCharacteristic(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='characteristic',
        verbose_name="Talyp"
    )
    file = models.FileField(
        upload_to='characteristics/',
        verbose_name="Häsiýetnama faýly"
    )
    text = models.TextField(verbose_name="Häsiýetnama teksti")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Ýüklenen wagty")

    class Meta:
        verbose_name = "Häsiýetnama"
        verbose_name_plural = "Häsiýetnamalar"

    def __str__(self):
        return f"Häsiýetnama {self.student}"