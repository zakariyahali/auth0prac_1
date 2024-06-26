import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve variables from the environment
domain = os.getenv('AUTH0_DOMAIN')
client_id = os.getenv('AUTH0_CLIENT_ID')
client_secret = os.getenv('AUTH0_CLIENT_SECRET')

def get_management_api_token(domain, client_id, client_secret):
    url = f"https://{domain}/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": f"https://{domain}/api/v2/",
        "grant_type": "client_credentials"
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    
    # Print detailed response for debugging
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    
    return response.json().get('access_token')

token = get_management_api_token(domain, client_id, client_secret)
print(f"This is the token: {token}")


###############################################################################################
#################################
"""use once to create user"""
#################################
def create_user(domain, token, email, password):
    url = f"https://{domain}/api/v2/users"
    payload = {
        "email": email,
        "password": password,
        "connection": "Username-Password-Authentication"
    }
    headers = {
        'authorization': f"Bearer {token}",
        'content-type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

email = 'newuse1r@example.com'
password = 'Pinkelephant2992'
user = create_user(domain, token, email, password)
print(f"This is the user that was created: {user}")
###############################################################################################



# extracting the token from the user's email
def get_user_token(domain, client_id, username, password):
    url = f"https://{domain}/oauth/token"
    payload = {
        "grant_type": "password",
        "client_id": client_id,
        "username": username,
        "password": password,
        "scope": "openid"
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

print(f"trying last method,.,.")
username = 'newuser@example.com'
user_token = get_user_token(domain, client_id, username, password)
print(user_token)
