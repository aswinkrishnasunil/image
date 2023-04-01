from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path('stulog/',views.stulog,name='stulog'),
    path('welcome/',views.welcome,name='welcome'),
    path('stuupdate/<int:pk>',views.stuupdate,name="stuupdate"),
    path('imacreate/',views.imacreate,name='imacreate'),
    path('view/',views.view,name='view'),
]

