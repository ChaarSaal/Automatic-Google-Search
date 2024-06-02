#pip install googlesearch-python

from googlesearch import search

# defining a function that will perform the Google Search....

def GoogleSearch(Query):
    SearchResults = search(Query, num_results = 10)
    for i, result in enumerate(SearchResults, start = 1):
        print(f'Result {i}: {result}')

#calling the googlesearch function and get top 10 results of the search on google....

Query = input('Which term would you like to search for? ')
GoogleSearch(Query)