from flask import Flask, request, redirect
import requests
import os
from urllib.parse import parse_qs

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GIT_API_URL = "https://api.github.com"
GIT_URL = "https://github.com"

def exchange_code(code: str) -> dict:
    param = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }
    result = requests.post(GIT_URL + '/login/oauth/access_token', params=param)
    parsed = parse_qs(result.content.decode())
    return parsed

def get_user(token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}"
    }
    result = requests.get(GIT_API_URL + "/user", headers=headers)
    return result.json()

@app.route('/')
def hello():
    link = f'<a href="https://github.com/login/oauth/authorize?client_id={CLIENT_ID}">Login with GitHub</a>'
    return link

@app.route('/callback')
def callback():
    code = request.args.get('code')
    result = exchange_code(code)
    token_list = result.get("access_token")
    if not token_list:
        return redirect("/")
    token = token_list[0]
    user = get_user(token)
    body = f'Got code: {code}. Current user: {user["login"]}'
    return body

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9999")