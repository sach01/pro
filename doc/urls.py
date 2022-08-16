from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('cert', views.cert, name='cert'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]