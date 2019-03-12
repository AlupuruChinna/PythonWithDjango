from django.urls import path

from accounts import views

urlpatterns=[

    path('login/', views.login, name='login'),
    path('logout/', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
]