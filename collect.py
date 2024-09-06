from bs4 import BeautifulSoup
import os

d= {'title':[1,2], 'Date' :[1,2] , 'Link' : [1,2]}

for file in os.listdir("data"):
    with open(f"data/{file}") as f:
        html_doc = f.read()
    soup =BeautifulSoup(html_doc, 'html.parser')
    title = soup.a.get_text(strip=True)
    date = "06.02.2023"  # Extracted from the title
    link = soup.a['href']

print(f"Title: {title}")
print(f"Date: {date}")
print(f"Link: {link}")
 

