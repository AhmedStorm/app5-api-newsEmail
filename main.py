import requests
from send_email import send_gmail

topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-06-23&sortBy=publishedAt&language=en&apiKey" \
      "=3bbcbd0638a74e49a46882f313d7f760 "

request = requests.get(url)
content = request.json()

body = """\
Subject: Today's News

"""
for article in content["articles"][:20]:
    if article["description"] is not None and article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_gmail(message=body)
