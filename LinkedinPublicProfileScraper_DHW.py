
# coding: utf-8

# ## Gather LinkedIn URLs

# In[ ]:

import requests # allows us to fetch URLs
import unicodedata # allows unicode transformations
import re # regex for advanced string transformations

# This function simply creates the url, in string form, and stores it to the list of urls
def make_lnkd_urls(username, url_list):
    url_list.append("https://www.linkedin.com/in/" + username)

# Add any other parameters here in this function
## parameters should/could be columns in your csv file
def get_lnkd_username(name, title, company, url_list, no_list):
    name = name.replace(" ", "+").replace("_", "").encode('utf-8').strip()
    title = title.replace(" ", "+").encode('utf-8').strip()
    company = company.replace(" ", "+").encode('utf-8').strip()

    # EDIT this search string based on the parameters of the function
    url = "https://www.bing.com/search?q=" + name + "+" + title + "+" + company + "linkedin"
    response = requests.get(url)
    
    #print response to check for errors
    print response
    
    string_v = unicodedata.normalize('NFKD', response.text).encode('ascii','ignore')
    m = re.search('https://www.linkedin.com/in/(.+?)"', string_v)
    
    if m:
        try:
            make_lnkd_urls(m.group(1), url_list)  
        except AttributeError:
            no_list.append(name)
            print "Nothing for: ", name
    else:
        # if name does not exist, this widens the search query by dropping a parameter
        ## In this case, I dropped company, but feel free to drop whichever you see fit
        url_2 = "https://www.bing.com/search?q=" + name + "+" + title + "linkedin"
        response = requests.get(url)
        print response
        string_v = unicodedata.normalize('NFKD', response.text).encode('ascii','ignore')
        n = re.search('https://www.linkedin.com/in/(.+?)"', string_v)
        if n:
            try:
                make_lnkd_urls(m.group(1), url_list)  
            except AttributeError:
                no_list.append(name)
                print "Nothing for: ", name
        else:
            no_list.append(name)
            print "Nothing for: ", name


# ## Run search query to gather list of LinkedIn URLs for each of the names in the CSV file

# In[ ]:

import csv
import pandas

raw_row_list = []
# **Replace file path with your own!**
csv_file = csv.reader(open("/something/something/data.csv", "rb"), delimiter=",")
for row in csv_file:
    raw_row_list.append(row)

master_row_list = raw_row_list[1:]


# In[ ]:

import time # for making variable time delays between searches
import random

url_list = []
no_list= []

for row in master_row_list:
    get_lnkd_username(row[0], row[1], url_list, no_list)
    i = random.uniform(0.7, 3.4)
    time.sleep(i)
    


# ## May have to rerun functions a few times since Bing times out (just start from the last name before time out)

# In[ ]:

# DONT RUN THIS BLOCK IF YOU DIDNT TIME OUT
## It's here for your convenience

import time # for making variable time delays between searches
import random

url2_list = []
no2_list= []

for row in master_row_list[542:]:
    get_lnkd_username(row[0], row[1], url2_list, no2_list)
    b = random.uniform(0.7, 3.4)
    time.sleep(b)


# In[ ]:

# DONT RUN THIS BLOCK IF YOU DIDNT TIME OUT
## It's here for your convenience

import time # for making variable time delays between searches
import random

url3_list = []
no3_list= []

for row in master_row_list[1043:]:
    get_lnkd_username(row[0], row[1], url3_list, no3_list)
    b = random.uniform(0.7, 3.4)
    time.sleep(b)


# ## After running through all the names, combine lists
# ### Even if Bing didn't time out, run anyways

# In[ ]:

# combine all runs into one list

master_url_list = url_list + url2_list + url3_list
master_no_list = no_list + no2_list + no3_list
print len(master_url_list)
print len(master_no_list)


# ## Write to master_url_list to CSV File

# In[ ]:

# master_url_list for safekeeping

import csv
# **Replace file path with your own!**
with open("/Users/david.wang/Google_Drive/Hackathon/master_url_list.csv", "wb") as csvfile:
    ticket_writer = csv.writer(csvfile)
    ticket_writer.writerow(['urls'])
    for row in master_url_list:
        ticket_writer.writerow([row,])


# ## Using BeautifulSoup and Selenium for scraping profiles

# In[ ]:

# divis by 2 function to switch web drivers on each iteration through master_url_list

def by_two (num):
    if num % 2 == 0:
        return True
    else:
        return False


# In[ ]:

from bs4 import BeautifulSoup
from selenium import webdriver

past_companies2 = []
bad_urls2 = []

count = 0

for url in master_url_list:
    
    # set the counter for web driver switcher
    count += 1
    
    if count%50 == 0:
        print 'Status Update: PC: ', len(past_companies2)
        print 'Status Update: BU: ', len(bad_urls2)
    
    # set randomized time delay between iterations
    i = random.uniform(1.3, 4.2)
    time.sleep(i)

    # web driver switcher
    if by_two(count):
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    
    # get the profile using url
    try:
        driver.get(url) # use driver to get profile response
    except:
        bad_urls2.append(url)
        continue
        
    html = driver.page_source # load driver to html
    soup = BeautifulSoup(html) # use BS on html
    
    # search for the "Previous positions" section on the header section of the linkedin profile
    ## within the tr tag, where data-section field is pastPositionDetails
    previous = soup.find('tr', { "data-section" : "pastPositionsDetails" })
    
    ### For more positions, inspect any public profile for the correct tags
    
    # try to see if past positions are listed
    try:
        text_v = previous.getText().encode('utf-8').strip().replace("Previous", "").split(",")
    except:
        bad_urls2.append(url)
        driver.close()
        continue
    
    # append text_v to past_companies2
    if text_v[0] == company or text_v[0] == company:
        try:
            past_companies2.append(text_v[1])
        except:
            bad_urls2.append(url)
    else:
        past_companies2.append(text_v[0])
    driver.close()


# In[ ]:

import pandas as pd
df = pd.DataFrame(past_companies2)
df


# ## Write Companies to CSV

# In[ ]:

# past_companies

import csv
# **Replace file path with your own!**
with open("/Volumes/home/w/wang.david/past_companies.csv", "wb") as csvfile:
    ticket_writer = csv.writer(csvfile)
    ticket_writer.writerow(['companies'])
    for row in past_companies2:
        ticket_writer.writerow([row,])


# In[ ]:



