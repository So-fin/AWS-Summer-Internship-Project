from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('', home,name='home'),
	path('contact', contact,name='contact'),
]