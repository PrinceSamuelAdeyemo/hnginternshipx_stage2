from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=256)
    #country_residence = models.CharField(max_length=50)
    #state_residence = models.CharField(max_length=50)
    
    """
    def create(self, name):
        person = Person(name=name)
        person.save()
        return person
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance
        
    def delete(self, validated_data):
        person = Person(**validated_data)
        person.delete()
    """    
    def __str__(self):
        return self.name
    