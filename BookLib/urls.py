from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inputForm, name='bookInsert'),
    path('<int:id>/', views.inputForm, name='bookUpdate'),
    path('delete/<int:id>/', views.bookDel, name='bookDelete'),
    path('list/', views.bookList, name='bookShow'),
]