from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configure Selenium to run headless
options = Options()
options.headless = True

# Initialize WebDriver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome(options=options)

# URL of the webpage
url = "https://ipm.ucanr.edu/PMG/GARDEN/FRUIT/DISEASE/shothole.html"
context = []
ignore_keywords = ['copyright', 'contact', 'nondiscrimination', 'accessibility', 'staff-only', 'subscribe']

try:
    driver.get(url)
    
    # Wait for dynamic content to load; adjust the sleep or use WebDriverWait for specific elements
    time.sleep(5)  # simple wait, or better: WebDriverWait
    
    # Example: find paragraph tags
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    
    # Filter content you want (for example, paragraphs with specific keywords)
    for p in paragraphs:
        text = p.text.strip()
        # if len(text) < 20:
        #     continue
        if any(keyword in text.lower() for keyword in ignore_keywords):
            continue
        print(text)
        # context.append(text)
        # if "Dry rot" in text:  # your condition to find relevant context
        #     print(text)
    # print(context)
finally:
    driver.quit()
