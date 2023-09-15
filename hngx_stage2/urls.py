from django.urls import path
from .views import CreatePerson, ReadUpdateDeletePerson

urlpatterns = [
    path('', CreatePerson.as_view(), name = 'createperson'),
    path('/<str:pk>', ReadUpdateDeletePerson.as_view(), name = 'RUDperson'),
]
