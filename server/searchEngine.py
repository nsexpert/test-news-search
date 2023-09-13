from newsapi import NewsApiClient
import os

api_key = os.getenv('API_KEY')
print(api_key)

# Api Key
newsSearchEngine = NewsApiClient(api_key = api_key)
# newsSearchEngine = NewsApiClient(api_key = '96312fb7d52a4ffc871e7174abe5f7c5')
