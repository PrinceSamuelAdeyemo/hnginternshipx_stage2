import requests
import re

# POST request to the API
def create_user(user_id):
    if user_id != None:
        #r = requests.Request('POST', f'http://127.0.0.1:8000/api', data={"name": user_id})
        r = requests.post(f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    else:
        user_id = "Micheal Essien"
        r = requests.post(f'http://127.0.0.1:8000/api', data={"name": user_id})
        #r = requests.Request('PUT', f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    
# GET request to the API
def get_user(user_id):
    if user_id != None:
        #r = requests.Request('GET', f'http://127.0.0.1:8000/api/{user_id}')
        r = requests.get(f'http://127.0.0.1:8000/api/{user_id}')
        return r.text
    else:
        user_id = "Micheal Essien"
        r = requests.get(f'http://127.0.0.1:8000/api/{user_id}')
        #r = requests.Request('PUT', f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    
# PUT request to the API    
def update_user(user_id, new_id):
    if user_id != None:
        r = requests.put(f'http://127.0.0.1:8000/api/{user_id}', data={"name": new_id})
        #r = requests.Request('PUT', f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    else:
        user_id = "Micheal Essien"
        r = requests.put(f'http://127.0.0.1:8000/api/{user_id}', data={"name": new_id})
        #r = requests.Request('PUT', f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    
# DELETE request to the API    
def delete_user(user_id):
    if user_id != None:
        #r = requests.Request('DELETE', f'http://127.0.0.1:8000/api/{user_id}')
        r = requests.delete(f'http://127.0.0.1:8000/api/{user_id}')
        return r.text
    else:
        user_id = "Micheal Essien"
        r = requests.delete(f'http://127.0.0.1:8000/api/{user_id}')
        #r = requests.Request('PUT', f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
        
print(create_user("Jon Snow"))

'''
def validate_strings(input):
    accepted_strings = r'^[a-zA-Z]+( [a-zA-Z]+)?$'
    if re.findall(accepted_strings, input):
        raise serializers.ValidationError("not a string") 
#validate_strings('Micheal Essien')
'''
"""

accepted_strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input:
        if (i not in accepted_strings):
            raise Error(" is not a string", params={"value": i})

def check(input):
    #accepted_strings = r"[a-zA-Z]+[]?[a-zA-Z]+"
    accepted_strings = r'^[a-zA-Z]+( [a-zA-Z]+)?$'
    if re.findall(accepted_strings, input):
        return  "Match"
    else:
        return "Doesn't match"
    
print(check("Samues sw"))
"""

