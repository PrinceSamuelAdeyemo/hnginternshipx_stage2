from django.shortcuts import render
from .models import Person

from .serializers import PersonSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class CreatePerson(generics.CreateAPIView):
    serializer_class = PersonSerializer
    def post(self, request):
        serializer = PersonSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            Person.objects.get(name = request.data['name'])
        except Person.DoesNotExist:
            serializer.create(validated_data=request.data)
            return Response(serializer.validated_data)
        else:
            return Response("This user exist in our database")
        
class ReadUpdateDeletePerson(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    def get(self, request):
        try:
            person = Person.objects.get(name = request.query_params['name'])
            serializer_class = PersonSerializer(person)
            return Response(serializer_class.data['name'])
        except:
            return Response("Invalid/Incomplete query parameter")
    
    def put(self, request):
        serializer = PersonSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance=request.query_params, validated_data=request.data)
        return Response(serializer.validated_data)
    
    def delete(self, request):
        person = Person.objects.get(name = request.query_params['name'])
        serializer_class = PersonSerializer(person)
        serializer_class.delete(validated_data=person)
        return Response("Deleted")