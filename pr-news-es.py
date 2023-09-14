#!/usr/bin/env python3

import requests
import json
from secret import API_KEY

def write_to_file(headlines, filename):
    """Write the headlines to the file."""
    with open(filename, 'w') as f:
        json.dump(headlines, f)

def get_bing_news_headlines(api_key, query, count=10):
    endpoint = "https://api.bing.microsoft.com/v7.0/news/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {
        "q": query,
        "count": count,
        "mkt": "es-US",
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    headlines = [
        {
            'name': article['name'], 
            'url': article['url'],
            'description': article.get('description', ''), 
            'provider': article['provider'][0].get('name', '') if isinstance(article.get('provider'), list) and article['provider'] else article.get('provider', {}).get('name', '')
        } 
        for article in search_results['value']
    ]

    return headlines

api_key = API_KEY
query = "Noticias de Puerto Rico"

# Get the headlines
headlines = get_bing_news_headlines(api_key, query)

# Write them to the file
write_to_file(headlines, "headlines.json")
