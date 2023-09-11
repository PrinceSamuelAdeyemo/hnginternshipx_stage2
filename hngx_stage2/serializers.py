from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    
    class Meta:
        model = Person
        field = '__all__'
        
    def create(self, validated_data):
        person = Person(data = validated_data)
        person.save()
        return person
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance
        
    def delete(self, validated_data):
        person = Person(**validated_data)
        person.delete()