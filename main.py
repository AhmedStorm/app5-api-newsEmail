import requests
from send_email import send_gmail

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-23&sortBy=publishedAt&apiKey" \
      "=3bbcbd0638a74e49a46882f313d7f760 "

request = requests.get(url)
content = request.json()

body = """\
Subject: Daily News

"""
for article in content["articles"]:
    if article["description"] is not None:
        if article["title"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_gmail(message=body)
