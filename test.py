from bs4 import BeautifulSoup
import re

# Assuming the HTML is stored in a variable called 'html_content'
soup = BeautifulSoup(html_content, 'html.parser')

# Find the <a> tag with target="_blank"
link_tag = soup.find('a', target='_blank')

if link_tag:
    # Extract title (removing the date at the end)
    full_title = link_tag.text.strip()
    title = re.sub(r'\s*\([^)]*\)\s*$', '', full_title)

    # Extract date
    date_match = re.search(r'\((\d{2}\.\d{2}\.\d{4})\)$', full_title)
    date = date_match.group(1) if date_match else None

    # Extract link
    link = link_tag.get('href')

    print(f"Title: {title}")
    print(f"Date: {date}")
    print(f"Link: {link}")
else:
    print("No matching element found")