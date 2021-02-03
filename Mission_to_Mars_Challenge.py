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
browser = Browser('chrome', **executable_path, headless=False)


# ## Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page

browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


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

# In[9]:


df = pd.read_html('https://space-facts.com/mars/')[0]
df.columns=['Description', 'Value']
df.set_index('Description', inplace=True)
df


# In[10]:


df.to_html()


# In[11]:


#browser.quit()


# ### Mars Weather

# In[12]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[13]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[14]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[15]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 
browser.visit(url)


# In[16]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css("a.product-item h3")

for i  in range(len(links)):
    hemispheres = {}
    browser.find_by_css("a.product-item h3")[i].click()
    sample_element = browser.find_link_by_text('Sample').first
    hemispheres["img_url"]=sample_element["href"]
    hemispheres["title"]=browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[17]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[18]:


# 5. Quit the browser
browser.quit()


# In[ ]:




