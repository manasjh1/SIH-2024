from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "Order"
File = 0

for i in range(1, 13):
    driver.get(f"https://doj.gov.in/document-category/latest-orders-of-appointment-transfer-etc/page/{i}/")

    # Assuming you have a WebDriver instance called 'driver'
    elems = driver.find_elements(By.CLASS_NAME, "bt-content")
    print(f"{len(elems)} items found")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{File}.html", "w", encoding="utf-8") as f:
            f.write(d)
            File += 1

    # Add a delay to avoid overloading the server
    time.sleep(2)

driver.close()
