from django.contrib import admin
from lecturesAPI.views import lecture_list, lecture_create, lecture
from django.urls import path

urlpatterns = [
    path('', lecture_create),
    path('list/', lecture_list),
    path('<int:pk>', lecture)
]


