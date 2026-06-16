# Q11. Web Scraping Task:
# Use requests and BeautifulSoup
# Website: http://quotes.toscrape.com
# Scrape all quotes and authors
# Print only quotes by Albert Einstein
# Save all data to quotes.json
# Print total quotes scraped
# Handle exceptions properly

import json
import sys


try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"Error: Required library missing - {e.name}")
    print("Please install the required libraries: pip install requests beautifulsoup4")
    sys.exit(1)

def scrape_quotes_system() -> None:
    
    base_url = "http://quotes.toscrape.com"
    current_page = 1
    all_quotes = []
    
    print("Starting Web Scraping Task...")
    print(f"Target Website: {base_url}\n")
    
    try:
        while True:
            page_url = f"{base_url}/page/{current_page}/"
            print(f"Scraping page {current_page}: {page_url}...")
            
            response = requests.get(page_url, timeout=15)
            
            
            if response.status_code != 200:
                print(f"Reached end of pages or page failed to load (Status: {response.status_code}).")
                break
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            
            quote_elements = soup.find_all('div', class_='quote')
            
            
            if not quote_elements:
                print("No more quotes found on this page. Stopping.")
                break
                
            for element in quote_elements:
                text_elem = element.find('span', class_='text')
                author_elem = element.find('small', class_='author')
                
                if text_elem and author_elem:

                    quote_text = text_elem.get_text().strip()
                    author_name = author_elem.get_text().strip()
                    
                    all_quotes.append({
                        "quote": quote_text,
                        "author": author_name
                    })
            

            next_button = soup.find('li', class_='next')
            if not next_button:
                print("No 'Next' button found. Scraped last page.")
                break
                
            current_page += 1

        print(f"\nScraping complete. Total pages scraped: {current_page}")
        total_scraped = len(all_quotes)
        print(f"Total quotes scraped across all pages: {total_scraped}\n")
        
        
        einstein_quotes = [q for q in all_quotes if q["author"] == "Albert Einstein"]
        
        print("=" * 80)
        print(f" QUOTES BY ALBERT EINSTEIN ({len(einstein_quotes)} found)")
        print("=" * 80)
        for i, q in enumerate(einstein_quotes, 1):
            print(f"{i}. {q['quote']}")
            print(f"   - {q['author']}\n")
        print("=" * 80 + "\n")
        
        
        output_file = "quotes.json"
        print(f"Saving all scraped quotes to '{output_file}'...")
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(all_quotes, file, indent=4)
        print(f"Successfully saved all quotes to {output_file}.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. The website took too long to respond.")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed. Please check your internet connection.")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred during scraping: {e}")

if __name__ == "__main__":
    print("--- Quotes Scraper Application ---")
    scrape_quotes_system()
