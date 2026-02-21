from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/create/', views.student_profile_create, name='profile_create'),
    path('profile/', views.profile_detail, name='profile_detail'),
    path('universities/', views.university_list, name='university_list'),
    path('universities/<int:pk>/', views.university_detail, name='university_detail'),
    path('majors/', views.major_list, name='major_list'),
    path('majors/<int:pk>/', views.major_detail, name='major_detail'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('preference/add/', views.preference_create, name='preference_create'),
    path('preference/<int:pk>/delete/', views.preference_delete, name='preference_delete'),
]
