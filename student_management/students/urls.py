from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.login_view, name='root'), 
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('students/', login_required(views.student_list), name='student_list'), 
    path('student/add/', views.student_create, name='student_create'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/edit/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('student/<int:student_pk>/relatives/', views.relative_list, name='relative_list'),
    path('student/<int:student_pk>/relative/add/', views.relative_create, name='relative_create'),
    path('student/<int:student_pk>/relative/<int:pk>/edit/', views.relative_update, name='relative_update'),
    path('student/<int:student_pk>/relative/<int:pk>/delete/', views.relative_delete, name='relative_delete'),
    path('student/<int:student_pk>/generate-relatives/', views.generate_relatives_doc, name='generate_relatives_doc'),
    path('student/<int:pk>/generate-characteristics/', views.generate_characteristics, name='generate_characteristics'),
    path('characteristic/select/', views.upload_characteristic_select, name='upload_characteristic_select'),
    path('student/<int:pk>/characteristic/upload/', views.upload_characteristic, name='upload_characteristic'),
    path('student/<int:pk>/characteristic/view/', views.view_characteristic, name='view_characteristic'),
    path('student/<int:pk>/save_doc/', views.save_relatives_doc, name='save_relatives_doc'),
    path('export/csv/', views.export_students_csv, name='export_students_csv'),
]