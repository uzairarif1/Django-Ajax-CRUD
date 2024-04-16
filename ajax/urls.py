from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('show',views.show,name='show'),
    path('add',views.add,name='add'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
