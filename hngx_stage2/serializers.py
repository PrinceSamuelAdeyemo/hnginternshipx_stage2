from rest_framework import serializers
from rest_framework.response import Response
from .models import Person

import re


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'
        #validators = [validate_strings]
        
    def create(self, validated_data):
        name = validated_data['name']
        #if type(name) == 'str':
        #print(type(name))
        person = Person(name=name)
        person.save()
        return person
        #else:
        #return Response("Only string is accepted!")
        
    def update(self, instance, validated_data):
        person = Person.objects.filter(name = instance).update(name = validated_data['name'])
        return person
        
    def delete(self, validated_data):
        name = validated_data
        person = Person.objects.get(name = name)
        person.delete()
        
   