import requests
from bs4 import BeautifulSoup

# Replace this with the link to the video you want to download
link = "https://youtu.be/gFNlefDsMT4"

# Use the requests library to download the video
response = requests.get(link)

# Check the status code to make sure the request was successful
if response.status_code == 200:
    # Save the video to a file
    with open("video.mp4", "wb") as f:
        f.write(response.content)
    print("Video downloaded successfully")
else:
    print("Failed to download video")