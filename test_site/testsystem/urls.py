from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestHome.as_view(), name='home'),
    path('test/<int:test_id>/', views.showtest, name='test'),
    path('result/', views.result, name='result'),
    path('addtest/', views.addtest, name='addtest'),
    path('edit/<int:test_id>/', views.update, name='edit'),
    path('deletetest/<int:test_id>/', views.deletetest, name='deletetest')
]