from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

# Navigate to the desired webpage
driver.get("https://doj.gov.in/document-category/latest-orders-of-appointment-transfer-etc/page/{i}/")  # Replace with your actual URL

# Locate the element using a CSS selector
element = driver.find_element(By.CSS_SELECTOR, "td[data-th='Title'] span.bt-content a")

# Extract information from the element (e.g., text and link)
title = element.text
link = element.get_attribute("href")

# Assuming you can extract the date from the title (modify as needed)
date = "21.08.2024"  # You can extract the date from the title if needed

# Print the extracted data
print(f"Title: {title}")
print(f"Date: {date}")
print(f"Link: {link}")

# Close the WebDriver
driver.quit()
