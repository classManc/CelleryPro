import requests
from celery import Celery
import bs4

#creates a celery app
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task
def get_latest():

    # send a request to the punch website
    website = requests.get('https://punchng.com/')

    # use the data returned to create BeautifulSoup object and use lxml to parse the data into html pattern
    soup = bs4.BeautifulSoup(website.text, 'lxml')

    # get the first element from the list of elements with a class .entry_title and also a link
    latest_news = soup.select('.entry-title a')[0]

    # get the value of the link and send a request to it
    latest_news_link = requests.get(latest_news['href'])

     # use the data returned to create BeautifulSoup object and use lxml to parse the data into html pattern
    soup = bs4.BeautifulSoup(latest_news_link.text, 'lxml')
    
    # get the first element from the list of elements with a class .post_title  which is the main content of the post
    latest_news_content =  soup.select('.post-content')[0]
    
    return latest_news_content.text