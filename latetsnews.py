import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def fetch_njdg_news():
    url = "https://www.drishtiias.com/daily-updates/daily-news-analysis/national-judicial-data-grid"
    
    try:
        # Send a GET request to the URL with a User-Agent header
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the news content (you may need to adjust these selectors based on the website structure)
        news_section = soup.find('div', class_='mw-parser-output')
        
        if news_section:
            # Extract paragraphs
            paragraphs = news_section.find_all('p')
            
            # Extract headings
            headings = news_section.find_all(['h2', 'h3', 'h4'])
            
            # Combine headings and paragraphs
            news_items = []
            for item in headings + paragraphs:
                if item.name in ['h2', 'h3', 'h4']:
                    news_items.append({'type': 'heading', 'content': item.text.strip()})
                else:
                    news_items.append({'type': 'paragraph', 'content': item.text.strip()})
            
            # Create a DataFrame
            df = pd.DataFrame(news_items)
            
            # Add timestamp
            df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            return df
        else:
            print("Could not find the news section on the page.")
            return pd.DataFrame()
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching the news: {e}")
        return pd.DataFrame()

# Usage
if __name__ == "__main__":
    news_df = fetch_njdg_news()
    if not news_df.empty:
        print(news_df)
        # You can save the DataFrame to a CSV file if needed
        # news_df.to_csv('njdg_news.csv', index=False)
    else:
        print("No news data retrieved.")