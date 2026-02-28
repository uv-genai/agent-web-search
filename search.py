#!/usr/bin/env python3
"""
Brave Search Script using Brave Search API.
Performs a search specified on the command line and prints results to stdout.

Usage: python search.py <search query> [-n <number_of_results>]
Example: python search.py "python programming tutorials" -n 20
         python search.py "best web scraping libraries" --num-results 15

Note: You need a Brave Search API key from https://api-dashboard.search.brave.com/
Set it as an environment variable: export BRAVE_API_KEY="your-api-key-here"
"""

import sys
import os
import argparse
import requests


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
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as raw JSON for coding agents'
    )
    
    args = parser.parse_args()
    
    # Validate num_results
    if args.num_results < 1:
        parser.error('Number of results must be at least 1')
    if args.num_results > 100:
        parser.error('Number of results cannot exceed 100')
    
    return args


def get_brave_api_key():
    """Get Brave Search API key from environment variable."""
    api_key = os.environ.get('BRAVE_API_KEY')
    if not api_key:
        print("Error: BRAVE_API_KEY environment variable not set.")
        print("Get your free API key from: https://api-dashboard.search.brave.com/")
        print("Set it with: export BRAVE_API_KEY='your-api-key-here'")
        sys.exit(1)
    return api_key


def brave_search(query, num_results, json_output=False):
    """
    Perform a Brave Search using the API and print the results.
    
    Args:
        query (str): The search query string
        num_results (int): Number of results to display
        json_output (bool): If True, output raw JSON instead of formatted text
    """
    import json
    
    api_key = get_brave_api_key()
    base_url = "https://api.search.brave.com/res/v1/web/search"
    
    params = {
        'q': query,
        'count': min(num_results, 50),  # API max is 50
        'country': 'us',
        'language': 'en'
    }
    
    headers = {
        'X-Subscription-Token': api_key,
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=30)
        
        if response.status_code != 200:
            error_msg = response.json().get('errors', [{}])[0].get('detail', response.text[:500])
            if json_output:
                output = {
                    'error': True,
                    'query': query,
                    'status_code': response.status_code,
                    'message': error_msg
                }
                print(json.dumps(output, indent=2))
            else:
                print(f"Error: API returned status code {response.status_code}")
                print(f"Details: {error_msg}")
            sys.exit(1)
        
        data = response.json()
        
        # Get web results
        web_results = data.get('web', {}).get('results', [])
        
        if json_output:
            # Build structured JSON output for coding agents
            output = {
                'query': query,
                'num_results_requested': num_results,
                'num_results_found': len(web_results),
                'results': []
            }
            
            for result in web_results[:num_results]:
                output['results'].append({
                    'title': result.get('title', ''),
                    'url': result.get('url', ''),
                    'description': result.get('description', ''),
                    'engine': 'brave_search'
                })
            
            # Print raw JSON
            print(json.dumps(output, indent=2))
        else:
            # Human-readable format
            print(f"\n{'='*60}")
            print(f"Brave Search Results for: {query}")
            print(f"Showing {min(num_results, 50)} results")
            print(f"{'='*60}\n")
            
            if not web_results:
                print("No results found.")
                return
            
            # Display results
            result_count = 0
            for result in web_results[:num_results]:
                result_count += 1
                
                title = result.get('title', 'No title')
                url = result.get('url', '')
                description = result.get('description', '')
                
                print(f"{result_count}. {title}")
                print(f"   URL: {url}")
                if description:
                    # Clean up description (remove extra whitespace)
                    description = ' '.join(description.split())
                    print(f"   Description: {description}")
                print()
            
            print(f"Total results displayed: {result_count}")
        
    except requests.exceptions.Timeout:
        if json_output:
            output = {
                'error': True,
                'query': query,
                'message': 'Request timed out'
            }
            print(json.dumps(output, indent=2))
        else:
            print("Error: Request timed out.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        if json_output:
            output = {
                'error': True,
                'query': query,
                'message': f'Failed to make request - {str(e)}'
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Error: Failed to make request - {e}")
        sys.exit(1)
    except Exception as e:
        if json_output:
            output = {
                'error': True,
                'query': query,
                'message': str(e)
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    args = parse_arguments()
    
    # Join all query arguments to support queries with spaces
    user_query = " ".join(args.query)
    brave_search(user_query, args.num_results, json_output=args.json)
