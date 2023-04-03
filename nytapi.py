import requests
import json
from datetime import datetime, timedelta

def get_articles(api_key, start_date, end_date):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    articles = []

    for i in range(7):
        params = {
            "api-key": api_key,
            "begin_date": start_date.strftime("%Y%m%d"),
            "end_date": end_date.strftime("%Y%m%d"),
            "page": i
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200 or "response" not in data:
            print("Error:", response.status_code, response.text)
            return

        docs = data["response"]["docs"]
        for doc in docs:
            article = {
                "title": doc["headline"]["main"],
                "url": doc["web_url"]
            }
            articles.append(article)

    return articles

def save_to_json(articles, filename):
    with open(filename, 'w') as f:
        json.dump(articles, f)

def main():
    api_key = "KtP9x1P4RqaUGxGAacPCWIdSS3kAKabs"
    today = datetime.today()
    week_ago = today - timedelta(days=7)
    
    articles = get_articles(api_key, week_ago, today)
    save_to_json(articles, "arti.json")

if __name__ == "__main__":
    main()
