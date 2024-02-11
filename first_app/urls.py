 
from django.urls import path
from .import views
urlpatterns = [
    path('login/', views.user_login,name='login'),
    path('signUp/', views.sign,name='sign'),
    path('logout/', views.user_logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('passchange/', views.pass_change,name='pass_change'),
    path('passchange_2/', views.pass_change_2,name='pass2_change'),
]
