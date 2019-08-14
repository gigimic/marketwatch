import feedparser
from bs4 import BeautifulSoup

NewsFeed1 = feedparser.parse("http://www.moneycontrol.com/rss/business.xml")
print('Number of RSS posts :', len(NewsFeed1.entries))

for entry in NewsFeed1.entries:
    print("\n", entry.title)
    html_marked = entry.summary
    soup = BeautifulSoup(html_marked, "lxml")
    storySummary = soup.get_text()
    print(storySummary)
