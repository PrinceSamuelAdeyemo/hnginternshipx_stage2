from django.urls import path
from .views import CreatePerson, ReadUpdateDeletePerson

urlpatterns = [
    path('', CreatePerson.as_view(), name = 'createperson'),
    path('user_id', ReadUpdateDeletePerson.as_view(), name = 'RUDperson'),
]
