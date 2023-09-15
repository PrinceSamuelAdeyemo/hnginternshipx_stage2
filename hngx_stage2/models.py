from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.

def validate_strings(input):
    """
    accepted_strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input:
        if (i not in accepted_strings):
            raise ValidationError(" is not a string", params={"value": i})
        
    return 'INVALID'
           """
           
    accepted_strings = r'^[a-zA-Z]+( [a-zA-Z]+)?$'
    if not re.findall(accepted_strings, input):
        raise serializers.ValidationError("not a string") 
    
class Person(models.Model):
    name = models.CharField(max_length=256, validators=[validate_strings])
    
    def __str__(self):
        return self.name
    