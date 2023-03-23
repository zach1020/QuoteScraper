# A script that scrapes a random quote from goodreads.com/quotes

import requests
from bs4 import BeautifulSoup

from collections import defaultdict

import random


# Generate a random number to determine the page to retrieve the quote from
page_number = random.randint(1, 100) # Inclusive range

URL = 'https://www.goodreads.com/quotes?page=' + str(page_number)

# Get the page source
page = requests.get(URL)

# Create a beautiful soup
soup = BeautifulSoup(page.content, 'html.parser')

# On goodreads, the quotes are in <div>s with the class 'quoteText'
quotes = soup.find_all('div', class_='quoteText')

# We need a defaultdict because we have may have multiple instances of the same key (author)
quotes_dict = defaultdict(list)


for quote in quotes:
	# quote.contents[0] should provide the quote given the page source
	q = quote.contents[0]
	# The following should provide the author's name
	a = quote.find('span').contents[0]
	quotes_dict[a] = q

author, quote = random.choice(list(quotes_dict.items()))

# Clean up author and quote strings
quote = quote.strip()
author = author.strip()
author = author.rstrip(',')

print(quote)
print(author)
print(URL)