# LinkedIn Public Profile Scraper

Overview: Given a list of names and various parameters such as job title and company (in a csv file), this scraper will find the best-matched LinkedIn URLs for each of the names, along with any additional information requested such as previous company worked at, current company, school, etc. I tried to make the code as boilerplate as possible and give helpful comments throughout. Let me know if there's any confusion!

Notes:
- The scraper only digs the top result so if your POI is not the top result then a different LinkedIn username and URL will be pulled. Thus, the benefits of this scraper are to search for a group of people within a known organization. For example, if I wanted to get the LinkedIn URLs for everyone who worked at Uber, then I would get a csv file with columns: first name, last name, and position. Then I read the csv file and use the scraper to append the first name, last name, position, "uber, and "LinkedIn" - these last two being added based on my discretion
- Average data accuracy through testing: 81% (Thus this scraper is probably best used to identify trends rather than get 100% accurate data. For the latter, please see LinkedIn for talent solutions/recruiting products.)
- Scraper takes about 1.5 hours to run for a list of 1000 names (depending on internet connection)
- Must have Firefox AND Chrome installed (or pick whatever webdrivers you want to use and make sure to change them in the code)
- Since webdrivers are being used, the repeated opening and closing of browser windows is totally normal
