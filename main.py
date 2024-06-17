from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve variables from the environment
domain = os.getenv('AUTH0_DOMAIN')
client_id = os.getenv('AUTH0_CLIENT_ID')
client_secret = os.getenv('AUTH0_CLIENT_SECRET')

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user_token = get_user_token(domain, client_id, username, password)
    if 'access_token' not in user_token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user_token