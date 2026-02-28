#!/usr/bin/env python3
"""
Brave Search Script using Selenium Headless with stealth capabilities.
Performs a search specified on the command line and prints results to stdout.

Usage: python google_search.py <search query> [-n <number_of_results>]
Example: python google_search.py "python programming tutorials" -n 20
         python google_search.py "best web scraping libraries" --num-results 15
"""

import sys
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Perform a Brave Search and print results to stdout.'
    )
    parser.add_argument(
        'query',
        nargs='+',
        help='Search query (use quotes for multi-word queries)'
    )
    parser.add_argument(
        '-n', '--num-results',
        type=int,
        default=10,
        help='Number of results to display (default: 10)'
    )
    
    args = parser.parse_args()
    
    # Validate num_results
    if args.num_results < 1:
        parser.error('Number of results must be at least 1')
    if args.num_results > 100:
        parser.error('Number of results cannot exceed 100')
    
    return args


def google_search(query, num_results):
    """
    Perform a Brave search and print the results.
    
    Args:
        query (str): The search query string
        num_results (int): Number of results to display
    """
    # Configure Chrome Options for Headless Mode
    options = Options()
    options.add_argument("--headless=new")  # Modern headless engine
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # Anti-detection options
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Set user agent to make it look more like a real browser
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    # Initialize WebDriver with webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Apply stealth settings to bypass bot detection
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
        )

        # Navigate to Brave Search
        driver.get("https://search.brave.com/")
        
        # Wait for page to load
        time.sleep(2)

        # Locate search box and submit query
        # Brave uses a textarea with id="searchbox"
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchbox"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='result']"))
        )
        time.sleep(2)

        # Extract and print search results
        results = driver.find_elements(By.CSS_SELECTOR, "[class*='result']")
        
        # Limit results to requested number (or available)
        results_to_display = min(num_results, len(results))
        
        print(f"\n{'='*60}")
        print(f"Brave Search Results for: {query}")
        print(f"Showing {results_to_display} of {len(results)} total results")
        print(f"{'='*60}\n")
        
        result_count = 0
        for index, result in enumerate(results[:results_to_display]):  # Limit to requested number
            try:
                # Extract title and link using the .l1 class
                title_el = result.find_element(By.CSS_SELECTOR, ".l1")
                title = title_el.text
                url = title_el.get_attribute("href")
                
                # Try to get description/snippet
                snippet = ""
                try:
                    # Look for description text in various possible locations
                    desc_el = result.find_element(By.CSS_SELECTOR, ".description, .snippet, p:not(.site-name)")
                    snippet = desc_el.text.strip()
                except:
                    pass
                
                if title and url:
                    result_count += 1
                    print(f"{result_count}. {title}")
                    print(f"   URL: {url}")
                    if snippet:
                        print(f"   Description: {snippet}")
                    print()
                    
            except Exception as e:
                continue

        if result_count == 0:
            print("No results found.")
        else:
            print(f"Total results displayed: {result_count}")

    finally:
        driver.quit()


if __name__ == "__main__":
    args = parse_arguments()
    
    # Join all query arguments to support queries with spaces
    user_query = " ".join(args.query)
    google_search(user_query, args.num_results)
