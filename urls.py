from selenium import webdriver
import time
from bs4 import BeautifulSoup
from tqdm import tqdm


query_keyword = ""
no_of_pages = 1
email = ""
password = ""

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/')

email_box = driver.find_element_by_id('login-email')
email_box.send_keys(email)
pass_box = driver.find_element_by_id('login-password')
pass_box.send_keys(password)
submit_button = driver.find_element_by_id('login-submit')
submit_button.click()

time.sleep(1)

urls = []
for i in tqdm(range(no_of_pages)):
	try:
		driver.get(
			'https://www.linkedin.com/search/results/people/?'
			'origin=FACETED_SEARCH&page=' + str(i) +
			'&title=' + query_keyword
		)
		soup = BeautifulSoup(driver.page_source, "lxml")
		soup = soup.find_all(class_="search-result__result-link")
		for s in soup:
			url = 'https://www.linkedin.com' + s['href']
			urls.append(url)
		print(i)
	except KeyboardInterrupt:
		break

urls = list(set(urls))
with open("URL/" + query_keyword + "Urls.txt", "a") as f:
	for url in urls:
		f.write(url + "\n")
