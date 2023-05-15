import requests
from requests_oauthlib import OAuth2Session
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


# Set up OAuth 2.0 credentials
# client_id = '104525'
# client_secret = '01db352d9a12b3b1dad73637d16ef35abfb2799c'
# authorization_base_url = 'https://www.strava.com/oauth/authorize'
# token_url = 'https://www.strava.com/oauth/token'
# redirect_uri = 'https://www.notion.so/Home-Page-b11051db63f744dfb001a8062fe6c36e'

# # Create an OAuth 2.0 session
# oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# # Fetch authorization URL and prompt user to authorize
# authorization_url, state = oauth.authorization_url(authorization_base_url)
# print('Please go to this URL and authorize the application: {}'.format(authorization_url))
# authorization_response = input('Enter the full callback URL: ')

# # Fetch OAuth 2.0 access token
# token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# # Use the access token to make API requests
# response = requests.get('https://www.strava.com/api/v3/athlete', headers={'Authorization': 'Bearer {}'.format(token['access_token'])})
# print(response.json())