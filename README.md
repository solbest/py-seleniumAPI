# Selenium to Web-Scraper
<p align="center"><img src="https://user-images.githubusercontent.com/136579135/260284717-b51713b5-b881-4f5d-9c38-06f12870a424.jpg" alt="solbest" /></p>
Selenium is a Python library and tool used for automating web browsers to do a number of tasks. One of such is web-scraping to extract useful data and information that may be otherwise unavailable. I made this API for 6 years. 
Web scraping based on Web structure. This can use for LinkedIn personal or company data scraping.

## Install and Imports
```bash
pip install -r requirements.txt

```
Once installed, you’re ready for the imports.
```python
import os
from api import Person, actions
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)

```
## LinkenIn Scraping with selenium API

Once that’s done, we’ll start the actual web scraping process. Let’s declare a function so we can use our web scraping code to fetch posts from multiple accounts in recursion. We’ll call it Scrape_func.
```python
def Scrape_func(a,b,c):
    name = a[28:-1]
    page = a
    time.sleep(10)

    driver.get(page + 'detail/recent-activity/shares/')  
    start=time.time()
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        end=time.time()
        if round(end-start)>20:
            break

    company_page = driver.page_source   

    linkedin_soup = bs(company_page.encode("utf-8"), "html")
    linkedin_soup.prettify()
    containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})
    print("Fetching data from account: "+ name)
    iterations = 0
    nos = int(input("Enter number of posts: "))
    for container in containers:

        try:
            text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper ember-view"})
            text = text_box.find("span",{"dir":"ltr"})
            b.append(text.text.strip())
            c.append(name)
            iterations += 1
            print(iterations)
            
            if(iterations==nos):
                break

        except:
            pass 

n = int(input("Enter the number of entries: "))
for i in range(n):
    post_links.append(input("Enter the link: "))
for j in range(n):
    Scrape_func(post_links[j],post_texts,post_names)

        
driver.quit()
```

<p align="center"><img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*0ffesBp0lJH6zXAI7r7fnA.jpeg" alt="solbest" /></p>