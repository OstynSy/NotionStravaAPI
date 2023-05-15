from pprint import pprint
import requests
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set local id, secret, and redirect_url variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = "https://www.notion.so/Running-31a3dd7f71a445e4b43f57dc188e589f"

# Create session variable
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

# Set auth url and scope variables
auth_base_url = "https://www.strava.com/oauth/authorize"
session.scope = ["profile:read_all"]
auth_link = session.authorization_url(auth_base_url)

# Print auth link and accept input
print(f"Click Here: {auth_link[0]}")
redirect_response = input(f"Paste redirect url here: ")

# Get oauth token
token_url = "https://www.strava.com/api/v3/oauth/token"
session.fetch_token(
    token_url=token_url,
    client_id=client_id,
    client_secret=client_secret,
    authorization_response=redirect_response,
    include_client_id=True
)

# Make request to protected resource
response = session.get("https://www.strava.com/api/v3/athlete")

# Print response
print("\n\n\n")
print(f"Response Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elaspsed: {response.elapsed}")
print(f"Response Text: \n{'-'*15}\n{response.text}")

# GET "https://www.strava.com/api/v3/athlete/activities?before=&after=&page=&per_page= Authorization: Bearer [[token]]"



# The first loop, request_page_number will be set to one, so it requests the first page. Increment this number after
# each request, so the next time we request the second page, then third, and so on...
request_page_num = 1
all_activities = []

# while True:
#     param = {'per_page': 200, 'page': request_page_num}
#     # initial request, where we request the first page of activities
#     my_dataset = requests.get(activites_url, headers=header, params=param).json()

#     # check the response to make sure it is not empty. If it is empty, that means there is no more data left. So if you have
#     # 1000 activities, on the 6th request, where we request page 6, there would be no more data left, so we will break out of the loop
#     if len(my_dataset) == 0:
#         print("breaking out of while loop because the response is zero, which means there must be no more activities")
#         break

#     # if the all_activities list is already populated, that means we want to add additional data to it via extend.
#     if all_activities:
#         print("all_activities is populated")
#         print(all_activities)
#         print(my_dataset)
#         #all_activities.extend(my_dataset)

#     # if the all_activities is empty, this is the first time adding data so we just set it equal to my_dataset
#     else:
#         print("all_activities is NOT populated")
#         all_activities = my_dataset

#     request_page_num += 1

# print(len(all_activities))
# for count, activity in enumerate(all_activities):
#     print(activity["name"])
#     print(count)
