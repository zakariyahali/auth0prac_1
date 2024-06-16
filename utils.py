import requests

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
    return response.json().get('access_token')

# Replace with your Auth0 domain, client_id, and client_secret
domain = 'your-auth0-domain'
client_id = 'your-client-id'
client_secret = 'your-client-secret'

token = get_management_api_token(domain, client_id, client_secret)
print(f"this is the token: {token}")



def create_organization(domain, token, organization_name):
    url = f"https://{domain}/api/v2/organizations"
    payload = {
        "name": organization_name,
        "display_name": organization_name.capitalize()
    }
    headers = {
        'authorization': f"Bearer {token}",
        'content-type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Replace with the name of the organization you want to create
organization_name = 'new-organization'
organization = create_organization(domain, token, organization_name)
print(f"this is the organization variable: {organization}")


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

# Replace with the email and password for the new user
email = 'newuser@example.com'
password = 'userpassword'
user = create_user(domain, token, email, password)
print(f"this is the user that was created: {user}")

#####################################
#####################################

# get auth token from user email/ password via rest api
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

# Replace with your Auth0 domain, client_id, username, and password
username = 'newuser@example.com'
user_token = get_user_token(domain, client_id, username, password)
print(user_token)

