import requests

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        print (urllink.url)

googleSearch('python')





g = requests.get('https://www.google.com') 
print(g.headers.keys())
