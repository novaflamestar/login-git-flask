# Git button example
* example of a button login based on [github docs](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-login-with-github-button-with-a-github-app).

# Setup
1. Create a GitHub App
2. set callback url to `http://127.0.0.1:9999/callback`
3. set the following env variables based on the created app:
```
CLIENT_ID=***
CLIENT_SECRET=***
```
4. ensure the URLs are correct