from django.shortcuts import render
from .models import Person

from .serializers import PersonSerializer
from rest_framework import generics
from rest_framework.response import Response

import re

# Create your views here.
class CreatePerson(generics.CreateAPIView):
    serializer_class = PersonSerializer
    def post(self, request):
        serializer = PersonSerializer(data = request.data)
        try:
            Person.objects.get(name = request.data['name'])
            return Response("This user exist in our database")
        except Person.DoesNotExist:
            try:
                serializer.is_valid(raise_exception=True)
                serializer.create(validated_data=request.data)
                return Response(serializer.validated_data)
            except:
                return Response("Check your input, must be string, no other datatype is allowed")
                
        else:
            return Response((serializer.errors ,"Can't save, check your input"))
        
class ReadUpdateDeletePerson(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    def get(self, request, pk):
        try:
            person = Person.objects.get(name = pk)
            #person = Person.objects.get(name = request.query_params['name'])
            serializer_class = PersonSerializer(person)
            return Response(serializer_class.data['name'])
        except:
            return Response("Invalid/Incomplete query parameter")
    
    def put(self, request, pk):
        serializer = PersonSerializer(instance = pk, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=pk, validated_data=request.data)
        return Response(serializer.validated_data)
    
    def delete(self, request, pk):
        try:
            person = Person.objects.get(name = pk)
            serializer_class = PersonSerializer(person)
            serializer_class.delete(validated_data=person)
            return Response("Deleted")
        except:
            return Response("Invalid/Incomplete query parameter")