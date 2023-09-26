import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'http://quotes.toscrape.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract the desired data
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    # Iterate through the extracted data and print it
    for i in range(len(quotes)):
        print(f"Quote: {quotes[i].text}")
        print(f"Author: {authors[i].text}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
