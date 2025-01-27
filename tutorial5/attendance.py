# Please execute the below code to ensure that you are added to our records! 
# This is mandatory to continuing in this team and this will be how we keep track
# of your progress. Please execute this file by replacing your name in this file. 
import requests
import json

name = "Rashed Rifat"
if not name:
    raise ValueError("You did not enter your name! Please do so.")

post_response = requests.post("https://9dontxvnf1.execute-api.us-east-2.amazonaws.com/alpha/record",
                data=json.dumps({"full_name" : name, "TID" : "05", "hash" : "bHapmSXua3"})
            )

print(post_response.json())