from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_strings(input):
    accepted_strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input:
        if (i not in accepted_strings):
            raise ValidationError(" is not a string", params={"value": i})
        
    return 'INVALID'
            
class Person(models.Model):
    name = models.CharField(max_length=256, validators=[validate_strings])
    
    def __str__(self):
        return self.name
    