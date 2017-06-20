
import sys
import requests
from bs4 import BeautifulSoup

# Accepts a search term on the command line
# Does not handle multi-word search terms
# Will have to go back and do that
search_term = sys.argv[1]

#Searches DuckDuckGo for given search term
search_engine = 'https://duckduckgo.com/html'
query_string = '/?q=' + search_term + '&ia=web'
request_string = search_engine + query_string

#Send a request with the request_string
r = requests.get(request_string)
data = r.text
soup = BeautifulSoup(data, 'lxml')

#Parses content of search result page
titles = soup.find_all('a', attrs={'class': 'result__a'})

#Returns parsed result in the following JSON format:
output = {}
output["search_term"] = search_term
output["results"] = []

counter = 0

# add to our output["results"], which is an array of dicts
for title in titles:
    result = {}
    result["title"] = title.text
    result["url"] = title["href"]
    output["results"].append(result)
    counter += 1

print('count: %d' % counter)

output["result_count"] = counter

print(output)

# time's up ... need to get the description using the class 'result__snippet'