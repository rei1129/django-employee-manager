from django.urls import path,include
from .import views

app_name ='employee'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
]
