from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='finch-index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='finch-detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch-create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch-update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch-delete'),
    path('finches/<int:finch_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    path('finches/<int:finch_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),
    path('finches/<int:finch_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove-toy'),
]