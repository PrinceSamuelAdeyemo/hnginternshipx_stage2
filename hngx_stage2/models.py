from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_strings(input):
    alpha = "1Hello"
    number_dict = []
    for i in input:
        try:
            print("Int:",int(i))
            number_dict.append(int(i))
        except ValueError:
            continue
            
    if (number_dict != []):
        print("numbers present")
class Person(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    