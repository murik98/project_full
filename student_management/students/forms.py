from django import forms
from .models import Student, Relative, StudentCharacteristic

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'last_name', 'first_name', 'middle_name', 'birth_date', 'birth_place',
            'course', 'faculty', 'student_id', 'admission_year', 'phone',
            'address', 'photo', 'characteristics', 'notes'
        ]
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'admission_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'characteristics': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'last_name': 'Familiýasy',
            'first_name': 'Ady',
            'middle_name': 'Atasynyň ady',
            'birth_date': 'Doglan senesi',
            'birth_place': 'Doglan ýeri',
            'course': 'Kurs',
            'faculty': 'Fakultet',
            'student_id': 'Talyp ID',
            'admission_year': 'Kabul edilen ýyly',
            'phone': 'Telefon',
            'address': 'Ýaşaýyş salgysy',
            'photo': 'Surat',
            'characteristics': 'Häsiýetnama',
            'notes': 'Bellikler',
        }

class RelativeForm(forms.ModelForm):
    class Meta:
        model = Relative
        fields = ['full_name', 'relationship', 'birth_date', 'birth_place', 'work_place', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'work_place': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'full_name': 'FIO',
            'relationship': 'Garindashlyk derejesi',
            'birth_date': 'Doglan wagty',
            'birth_place': 'Doglan ýeri',
            'work_place': 'Işleýän ýeri',
            'address': 'Ýaşaýan ýeri',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['birth_place'].required = False
        self.fields['work_place'].required = False

class CharacteristicUploadForm(forms.ModelForm):
    class Meta:
        model = StudentCharacteristic
        fields = ['file', 'text']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }
        labels = {
            'file': 'Fayl häsiýetnamasy',
            'text': 'Tekst häsiýetnamasy',
        }