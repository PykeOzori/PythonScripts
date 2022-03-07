# HTML info:
# class ="text-3xl font-bold pt-8 lg:pt-0" > Jane Doe < / h1 >
# <span class ="ml-2" > Job: HumanResources </span>
# <span class="ml-3">Location: Amsterdam, Netherlands</span>
# <span class="ml-3">Contact: jane.doe@acme.com</span>

# Importing the libraries needed
# The requests library is needed to send an HTTP GET request to the URL
# BeautifulSoup is used to parse the data
# JSON library is used to convert Python Objects into JSON strings
import requests
from bs4 import BeautifulSoup
import json
# URL refers to the website
# Page sends a GET request to the given URL
URL = "http://localhost/"
page = requests.get(URL)
# Takes the page content we scraped earlier as input
soup = BeautifulSoup(page.content, "html.parser")
# Prints the GET requests and filters out the necessary text
Full_Name = soup.find("h1").text
# JLC stands for Job Location Contact. JLC[0] gets the first value, JLC[1] the second value and JLC[2] the third value
JLC = soup.find_all("span")
Job = JLC[0].get_text()
Location = JLC[1].get_text()
Contact = JLC[2].get_text()
# Prints the values
print(Full_Name)
print(Job)
print(Location)
print(Contact)

# Python object that needs to be converted into a JSON String
profile = {
  "Name": Full_Name,
  "Job": Job,
  "Location": Location,
  "Contact": Contact
}

# converts the Python object into JSON string
data = json.dumps(profile)

# the result is a JSON string
print(json.dumps(data))

# Writes the JSON string to a file
with open('profile.json', 'w') as outfile:
    outfile.write(data)
