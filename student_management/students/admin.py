from django.contrib import admin
from .models import Student, Relative, StudentCharacteristic

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'student_id', 'course', 'faculty', 'admission_year']
    list_filter = ['course', 'faculty', 'admission_year']
    search_fields = ['last_name', 'first_name', 'middle_name', 'student_id']
    readonly_fields = ['full_name']
    fieldsets = (
        (None, {
            'fields': ('last_name', 'first_name', 'middle_name', 'full_name')
        }),
        ('Personal Info', {
            'fields': ('birth_date', 'birth_place', 'phone', 'address', 'photo')
        }),
        ('Academic Info', {
            'fields': ('course', 'faculty', 'student_id', 'admission_year')
        }),
        ('Additional Info', {
            'fields': ('characteristics', 'notes', 'forma2')
        }),
    )

@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'student', 'relationship', 'birth_date', 'birth_place', 'work_place', 'address']
    list_filter = ['relationship']
    search_fields = ['full_name', 'student__last_name', 'student__first_name', 'birth_place', 'work_place']
    raw_id_fields = ['student']

@admin.register(StudentCharacteristic)
class StudentCharacteristicAdmin(admin.ModelAdmin):
    list_display = ['student', 'uploaded_at']
    search_fields = ['student__last_name', 'student__first_name']
    raw_id_fields = ['student']