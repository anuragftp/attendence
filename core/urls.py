from django.urls import path
from django.contrib.auth.decorators import login_required
from core.views import (
      HomeView,
   )
urlpatterns=[
   # path('home/',home,name='home'),
   path('home/',login_required(HomeView.as_view()),name='home_view'),


]