#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# What does is_element_not_present_by_css mean
browser.is_element_not_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use parent element to find summary of news article
summary = slide_elem.find("div", class_='article_teaser_body').get_text()
summary


# ### Featured Images

# In[8]:


# Visit Archived JPL URL
PREFIX = "https://web.archive.org/web/20181114023740"
url = f'{PREFIX}/https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[9]:


try:
    PREFIX = "https://web.archive.org/web/20181114023740"
    url = f'{PREFIX}/https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    article = browser.find_by_tag('article').first['style']
    article_background = article.split("_/")[1].replace('");',"")
    print (f'{PREFIX}_if/{article_background}')
except:
    print('https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/pia22486-main.jpg')


# ## Mars Info Table

# In[10]:


df = pd.read_html('https://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[11]:


df.to_html()


# In[12]:


browser.quit()


# In[ ]:




