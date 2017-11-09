# Linkedin-Scraper

Scraping LinkedIn profiles is not fun(at all). Without signing-in with a LinkedIn account, you can hardly access more than 15 profiles.

 1. You need to sign-in with your account.
 2. LinkedIn profile pages are dynamic and don't load completely unless you scroll the entire page.

This program let's you scrape profiles based on a keyword in the user's title. (You can edit the link to look for profiles of users working at a specific company or studying at some school)
It generates a csv file of these profiles with columns:
 1. Months of Experience
 2. Skills (Seperated by ':')
 3. Recommendations received
 4. No. of Projects
 5. No. of Publications
 6. No. of Followers 
----------
### Requirements

 - Python3
 - Chrome web driver
 - Selenium
 - BeautifulSoup


----------
### Setup
https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
 1. Download and unzip this
 2. chmod +x chromedriver
 3. sudo mv -f chromedriver /usr/local/share/chromedriver
 4. sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
 5. sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
 6. pip3 install selenium (Try sudo -H pip3 install selenium if this fails)
 7. pip3 install beautifulsoup4
 

----------
### Usage
 1. Edit ***urls.py*** by modifying the ***query_keyword*** variable that scrapes profiles with query_keyword as the title(eg. student or professor or founder), ***set no_of_pages*** to the number of search result pages you'd like to scrape(Each page has upto 10 profiles), and enter your ***linkedin credentials***.
 2. python3 urls.py
 3. Edit ***extract.py*** by modifying ***query_keyword*** again.
 4. python3 extract.py
  

----------
P.S. With great power comes great responsibility. Scrape too much too fast, and your account might get blocked. Scrape safe.

