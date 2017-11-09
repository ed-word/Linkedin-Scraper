from selenium import webdriver
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

query_keyword = ""
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


def getMonths(page):
	months = 0
	soup = page.find_all(class_="pv-entity__bullet-item")
	for s in soup:
		s = s.string
		if "Cause" in s:
			continue
		if "less" not in s:
			exp = [int(x) for x in s.split() if x.isdigit()]
			if(len(exp) == 2):
				months += 12 * exp[0] + exp[1]
			else:
				if "yr" not in s:
					months += exp[0]
				else:
					months += 12 * exp[0]
	months = str(months)
	return months


def getSkills(page):
	skills = ''
	soup = page.find_all("span", class_="pv-skill-entity__skill-name")
	for s in soup:
		skills += s.string + ':'
	return skills


def getRecommendations(page):
	soup = page.find("div", class_="recommendations-inlining")
	soup = soup.find("artdeco-tab")
	soup = soup.string
	s = [int(x) for x in soup if x.isdigit()]
	s = str(s[0])
	return s


def getProjects(page):
	soup = page.find("section", class_="projects")
	soup = soup.find_all("span")
	soup = soup[1].string
	return soup


def getPublications(page):
	soup = page.find("section", class_="publications")
	soup = soup.find_all("span")
	soup = soup[1].string
	return soup


def getFollowers(page):
	soup = page.find("h3", class_="pv-top-card-section__connections")
	soup = soup.find("span")
	soup = soup.string
	return soup


with open("URL/" + query_keyword + "Urls.txt", "r") as f:
	urls = f.read().splitlines()

with open("CSV/" + query_keyword + ".csv", "a") as file:
	file.write(
		"Months of Experience, Skills, Recommendations received, "
		"No. of Projects, No. of Publications, No. of Followers \n"
	)

for i, soup in enumerate(tqdm(urls)):
	driver.get(soup)
	scheight = .1
	while scheight < 20:
		driver.execute_script(
			"window.scrollTo(0, document.body.scrollHeight/%s);"
			% scheight
		)
		scheight += .01

	try:
		arrow = driver.find_element_by_css_selector(
			'button.pv-profile-section'
			'__see-more-inline'
		)
		arrow.click()
	except Exception as e:
		print(e)
	try:
		arrow = driver.find_element_by_css_selector(
			'button.pv-skills-section'
			'__additional-skills'
		)
		arrow.click()
		time.sleep(1)
	except Exception as e:
		print(e)

	page = BeautifulSoup(driver.page_source, 'lxml')

	row = ''
	try:
		# Experience
		months = getMonths(page)
		print("Experience: ", months)
		row += months + ','
	except Exception as e:
		row += '0,'
		print("Experience: ", e)

	try:
		# Skills
		skills = getSkills(page)
		print("Skills: ", skills)
		row += skills + ','
	except Exception as e:
		row += ','
		print("Skills: ", e)

	try:
		# Recommendations received
		rec = getRecommendations(page)
		print("Recommendations: ", rec)
		row += rec + ','
	except Exception as e:
		row += '0,'
		print("Recommendations: ", e)

	try:
		# Projects
		proj = getProjects(page)
		print("Projects: ", proj)
		row += proj + ','
	except Exception as e:
		row += '0,'
		print("Projects: ", e)

	try:
		# Publications
		pub = getPublications(page)
		print("Publications: ", pub)
		row += pub + ','
	except Exception as e:
		row += '0,'
		print("Publications: ", e)

	try:
		# Followers
		followers = getFollowers(page)
		print("Followers: ", followers)
		row += followers
	except Exception as e:
		row += '0'
		print("Followers: ", e)

	print()
	print()
	with open("CSV/" + query_keyword + ".csv", "a") as file:
		file.write(row + '\n')
