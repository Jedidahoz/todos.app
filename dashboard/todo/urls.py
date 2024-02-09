from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('<int:id>/delete', views.deletetodos, name='deletetodos'),
    path('<int:id>/update', views.updatetodos, name='updatetodos')
    
]