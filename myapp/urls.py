
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.home),
    path('post_data',views.post_data),
    path('update_data/<id>',views.update_data),
    path('delete_data/<id>',views.delete_data),
    path('students', views.student_data, name='student-data'),
    path('students/<int:id>', views.student_detailview, name='student_detailview'),
    path('student/', views.StudentDataView.as_view(), name='student-list'),
    path('student/<id>/', views.StudentDataView.as_view(), name='student-detail'),
     path('std/', views.StudentDataView.as_view(), name='student-list'),
    path('std/<int:pk>/', views.StudentDetailsView.as_view(), name='student-details'),

]