from tavily import TavilyClient
import os
from deep_translator import GoogleTranslator


tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


class SearchAgent:
    def __init__(self):
        pass
    def translate_to_english(self, text):
        translator = GoogleTranslator(source='auto', target='en')
        return translator.translate(text)
        
     def search_tavily(self, query: str):
        translated_query = self.translate_to_english(query)
        print("query = ",query)
        print("translated_query = ", translated_query)

        results = tavily_client.search(query=translated_query, topic="news", max_results=10, include_images=True)
        sources = results["results"]
        try:
            image = results["images"][0]
        except:
            image = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bmV3c3BhcGVyJTIwbmV3c3BhcGVyJTIwYXJ0aWNsZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"
        return sources, image

    def run(self, article: dict):
        res = self.search_tavily(article["query"])
        article["sources"] = res[0]
        article["image"] = res[1]
        return article
