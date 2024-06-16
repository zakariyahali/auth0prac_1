from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import requests

app = FastAPI()

# OAuth2PasswordBearer is used to extract the token from the request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Replace these variables with your Auth0 domain and client ID
domain = 'your-auth0-domain'
client_id = 'your-client-id'

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

def verify_token(token: str):
    url = f"https://{domain}/userinfo"
    headers = {'authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid token")
    return response.json()

@app.get("/protected-endpoint")
def protected_endpoint(token: str = Depends(oauth2_scheme)):
    user_info = verify_token(token)
    return {"message": "This is a protected endpoint", "user_info": user_info}

# This is the endpoint to obtain the token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_token = get_user_token(domain, client_id, form_data.username, form_data.password)
    if 'access_token' not in user_token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user_token
