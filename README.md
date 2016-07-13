# LinkedIn URL Scraper

Overview: Given a list of names and various parameters, one can use this scraper to find the relevant user LinkedIn URLs for each of the names.

Use Cases:
- "I have a list of names of people who are part of xyz company/organization and I want to be able to get the LinkedIn URLs for each of these names"
- ...more to come

Steps:

1. Edit the search parameters within the "url" variable. 

>> url is a string that is basically a google search query with parameters attached to the end of it that help refine the search. It is important you add the right parameters because this scraper relies heavily on Google's ability to use these parameters to find the person you actually mean. 

>> The scraper only digs the top result so if your POI is not the top result then a different LinkedIn username and URL will be pulled. Thus, the benefits of this scraper are to search for a group of people within a known organization. For example, if I wanted to get the LinkedIn URLs for everyone who worked at Uber, then I would get a csv file with columns: first name, last name, and position. Then I read the csv file and use the scraper to append the first name, last name, position, "uber, and "LinkedIn" - these last two being added based on my discretion

2. As mentioned above, importing data and setting it up in the way that is readable to the scraper is very important. However, the code here is pretty boilerplate and I encourage customization to fit your needs.

3. To scrape the individual LinkedIn urls for information such as companies works at, positions held, skills endorsed, etc, please refer to this script: https://github.com/yatish27/linkedin-scraper
