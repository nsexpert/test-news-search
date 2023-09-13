from newsapi import NewsApiClient
import os

api_key = os.getenv('API_KEY')
if api_key == None:
    print("===================> PLEASE CONFIG ENV FOR RUNNING SERVER!")

# Api Key
newsSearchEngine = NewsApiClient(api_key = api_key)
