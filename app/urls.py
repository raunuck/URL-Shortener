from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("<str:token>/",views.redirect_view,name="redirect")
]