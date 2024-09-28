import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(count):

  # Fetch the HTML of the current page
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Retrieve all anchor tags
  tags = soup('a')

  # Get the atge at the specified position
  selected_tag = tags[position - 1]

  # Get the href attribute and upate the URL to follow the link
  url = selected_tag.get('href', None)

  # Print the URL being retrieved
  print(f"Retrieving: {url}")

# Regex pattern to extract the name between "known_by_" and ".html"
last_name = re.findall(r'known_by_(\w+)\.html', url)

# Since re.findall returns a list, we take the first match (if it exists)
if last_name:
  last_name = last_name[0]

print(f"Last name in sequence: {last_name}")
