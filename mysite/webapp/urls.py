from django.urls import path
from webapp import views

urlpatterns = [
    path("", views.home, name=""),
    
    path('register/', views.register, name="register"),
    
    path('login/', views.the_login, name="the-login"),

    path('logout/', views.the_logout, name='the-logout'),

    #crud
    path('dashboard/', views.dashboard, name='dashboard'),

    path('create/', views.create_record, name='create-record'),

    path('update/<int:pk>/', views.update_record, name='update-record'),

    path('view/<int:pk>/', views.view_record, name='view-record'),

    path('delete/<int:pk>/', views.delete_record, name='delete-record'),
]