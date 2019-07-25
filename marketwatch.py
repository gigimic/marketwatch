import feedparser
import spacy
import re
import nltk
import urllib
from bs4 import BeautifulSoup

nlp_en = spacy.load('en')

NewsFeed1 = feedparser.parse("http://www.moneycontrol.com/rss/business.xml")
print('Number of RSS posts :', len(NewsFeed1.entries))

story = NewsFeed1.entries

for x in range(len(NewsFeed1.entries)):
    print("\n", story[x].title)
    html_marked = story[x].summary
    soup = BeautifulSoup(html_marked, "lxml")
    storySummary = soup.get_text()
    print(storySummary)

