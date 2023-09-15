import requests

# POST request to the API
def create_user(user_id):
    if user_id != None:
        #r = requests.Request('POST', f'http://127.0.0.1:8000/api', data={"name": user_id})
        r = requests.post(f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    
# GET request to the API
def get_user(user_id):
    if user_id != None:
        #r = requests.Request('GET', f'http://127.0.0.1:8000/api/{user_id}')
        r = requests.get(f'http://127.0.0.1:8000/api/{user_id}')
        return r.text
    
# PUT request to the API    
def update_user(user_id):
    if user_id != None:
        r = requests.put(f'http://127.0.0.1:8000/api/{user_id}', data={"name": "Replaced"})
        #r = requests.Request('PUT', f'http://127.0.0.1:8000/api', data={"name": user_id})
        return r.text
    
# DELETE request to the API    
def delete_user(user_id):
    if user_id != None:
        #r = requests.Request('DELETE', f'http://127.0.0.1:8000/api/{user_id}')
        r = requests.delete(f'http://127.0.0.1:8000/api/{user_id}')
        return r.text
        
print(update_user("Essien"))