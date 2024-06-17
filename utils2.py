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
    print(f"Token response: {response.json()}")  # Debugging
    return response.json().get('access_token')

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
    print(f"Create user response: {response.json()}")  # Debugging
    return response.json()

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
    print(f"Get user token response: {response.json()}")  # Debugging
    return response.json()

# # Get the management API token
# token = get_management_api_token(domain, client_id, client_secret)
# print(f"This is the token: {token}")

# # Create a user
# email = 'newuser313@example.com'
# password = 'ThisisProperOkay3134'
# # user = create_user(domain, token, email, password)
# # print(f"This is the user that was created: {user}")

# # Get a user token
# user_token = get_user_token(domain, client_id, email, password)
# print("£")
# print(f"This is the user token: {user_token}")



# Get the management API token
token = get_management_api_token(domain, client_id, client_secret)
# print(f"This is the token: {token}")

# Decode and print the token (for debugging)
import jwt
decoded_token = jwt.decode(token, options={"verify_signature": False})
# print(f"Decoded token: {decoded_token}")

# Create a user
email = 'newuser33333333@example.com'
password = 'Myfrozencartoon314'
# user = create_user(domain, token, email, password)
# print(f"This is the user that was created: {user}")

# Get a user token
user_token = get_user_token(domain, client_id, email, password)
print(f"This is the user token: {user_token}")
