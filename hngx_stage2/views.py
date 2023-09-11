from django.shortcuts import render

from .models import Person

from .serializers import PersonSerializer
from rest_framework import generics

# Create your views here.
class CreatePerson(generics.CreateAPIView):
    def get(self, request):
        serializer = PersonSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        self.name = serializer.validated_data['name']
        self.country_residence = serializer.validated_data['country_residence']
        self.state_residence = serializer.validated_data['state_residence']
        
        person = Person(name = self.name, country_residence= self.country_residence, state_residence= self.state_residence)
        person.save()
        return person
        
class ReadUpdateDeletePerson(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request):
        serializer_class = PersonSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        
        self.name = serializer.validated_data['name']
        self.country_residence = serializer.validated_data['country_residence']
        self.state_residence = serializer.validated_data['state_residence']
        
        
        
        return person
    
    def put(self, request):
        serializer_class = PersonSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        
        self.name = serializer.validated_data['name']
        self.country_residence = serializer.validated_data['country_residence']
        self.state_residence = serializer.validated_data['state_residence']
        
        person = Person(name = self.name, country_residence= self.country_residence, state_residence= self.state_residence)
        person.save()
        
        return person
    
    def delete(self, request):
        serializer_class = PersonSerializer(data = request.data)
        serializer_class.is_valid(raise_exception=True)
        
        self.name = serializer.validated_data['name']
        self.country_residence = serializer.validated_data['country_residence']
        self.state_residence = serializer.validated_data['state_residence']
        
        person = Person(name = self.name, country_residence= self.country_residence, state_residence= self.state_residence)
        person.save()
        
        return person