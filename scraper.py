# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import logging

# --- Configuration ---
# URL of the website to scrape
URL = "http://quotes.toscrape.com"
# Name for the output file
OUTPUT_FILE = "quotes.csv"
# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page(url):
    """
    Fetches the content of a web page.
    
    Args:
        url (str): The URL of the web page to fetch.
        
    Returns:
        str: The content of the web page as text, or None if the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logging.info(f"Successfully fetched the page: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the page {url}: {e}")
        return None

def parse_quotes(html_content):
    """
    Parses the HTML content to extract quote data.
    
    Args:
        html_content (str): The HTML content of the web page.
        
    Returns:
        list: A list of dictionaries, where each dictionary represents a quote.
    """
    if not html_content:
        logging.warning("HTML content is empty. Cannot parse quotes.")
        return []
        
    soup = BeautifulSoup(html_content, 'html.parser')
    quote_elements = soup.find_all('div', class_='quote')
    quotes_data = []
    
    for quote_element in quote_elements:
        text = quote_element.find('span', class_='text').get_text(strip=True)
        author = quote_element.find('small', class_='author').get_text(strip=True)
        tags_elements = quote_element.find_all('a', class_='tag')
        tags = [tag.get_text(strip=True) for tag in tags_elements]
        
        quotes_data.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)
        })
        
    logging.info(f"Successfully parsed {len(quotes_data)} quotes.")
    return quotes_data

def save_to_csv(data, filename):
    """
    Saves the extracted data to a CSV file.
    
    Args:
        data (list): A list of dictionaries to save.
        filename (str): The name of the CSV file.
    """
    if not data:
        logging.warning("No data to save.")
        return

    headers = ["text", "author", "tags"]
    
    try:
        # Open the CSV file in write mode, specifying the UTF-8 encoding.
        # This is the line that fixes the character issue.
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
            
        logging.info(f"Data successfully saved to {filename}")
    except IOError as e:
        logging.error(f"Error writing to file {filename}: {e}")


def main():
    """
    Main function to run the web scraper.
    """
    logging.info("Scraper script started.")
    html = fetch_page(URL)
    
    if html:
        quotes = parse_quotes(html)
        save_to_csv(quotes, OUTPUT_FILE)
        
    logging.info("Scraper script finished.")


if __name__ == "__main__":
    main()