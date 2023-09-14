from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'
        
    def create(self, validated_data):
        name = validated_data['name']
        person = Person(name=name)
        person.save()
        return person
        
    def update(self, instance, validated_data):
        person = Person.objects.filter(name = instance['name']).update(name = validated_data['name'])
        return person
        
    def delete(self, validated_data):
        name = validated_data
        person = Person.objects.get(name = name)
        person.delete()