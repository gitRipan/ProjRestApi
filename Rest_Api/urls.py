from django.urls import path
from Rest_Api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
