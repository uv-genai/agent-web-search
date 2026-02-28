#!/usr/bin/env python3
"""
Linkup Search Script using Linkup API.
Performs searches and fetches web pages using Linkup's agentic search API.

Usage:
  # Search mode
  python linkup_search.py search "your query" [-n <num_results>] [--json]
  
  # Fetch mode
  python linkup_search.py fetch <url> [--json]

Examples:
  python linkup_search.py search "python web scraping tutorials" -n 10
  python linkup_search.py search "machine learning 2026" --depth deep --json
  python linkup_search.py fetch "https://example.com/article"
  python linkup_search.py fetch "https://example.com" --output-format markdown

Note: You need a Linkup API key from https://app.linkup.so/
Set it as an environment variable: export LINKUP_API_KEY="your-api-key-here"
"""

import sys
import os
import time
import argparse
import requests


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Perform Linkup searches and fetch web pages.',
        epilog='Use "search" or "fetch" as the first argument to choose mode.'
    )
    
    subparsers = parser.add_subparsers(dest='mode', help='Search mode')
    
    # Search subcommand
    search_parser = subparsers.add_parser('search', help='Perform a search')
    search_parser.add_argument(
        'query',
        nargs='+',
        help='Search query (use quotes for multi-word queries)'
    )
    search_parser.add_argument(
        '-n', '--num-results',
        type=int,
        default=10,
        help='Number of results to display (default: 10)'
    )
    search_parser.add_argument(
        '--depth',
        choices=['standard', 'deep'],
        default='standard',
        help='Search depth: standard (fast) or deep (thorough, default: standard)'
    )
    search_parser.add_argument(
        '--output-type',
        choices=['searchResults', 'sourcedAnswer', 'structured'],
        default='searchResults',
        help='Output type (default: searchResults)'
    )
    search_parser.add_argument(
        '--from-date',
        dest='from_date',
        help='Filter results from date (ISO 8601: YYYY-MM-DD)'
    )
    search_parser.add_argument(
        '--to-date',
        dest='to_date',
        help='Filter results to date (ISO 8601: YYYY-MM-DD)'
    )
    search_parser.add_argument(
        '--include-domains',
        dest='include_domains',
        nargs='+',
        help='Restrict search to specific domains'
    )
    search_parser.add_argument(
        '--exclude-domains',
        dest='exclude_domains',
        nargs='+',
        help='Exclude specific domains from search'
    )
    search_parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as raw JSON for coding agents'
    )
    
    # Fetch subcommand
    fetch_parser = subparsers.add_parser('fetch', help='Fetch a web page')
    fetch_parser.add_argument(
        'url',
        help='URL to fetch'
    )
    fetch_parser.add_argument(
        '--output-format',
        dest='output_format',
        choices=['html', 'markdown'],
        default='markdown',
        help='Output format: html or markdown (default: markdown)'
    )
    fetch_parser.add_argument(
        '--render-js',
        dest='render_js',
        action='store_true',
        help='Execute JavaScript to capture dynamic content'
    )
    fetch_parser.add_argument(
        '--json',
        action='store_true',
        help='Output result as raw JSON'
    )
    
    args = parser.parse_args()
    
    if args.mode is None:
        parser.error("Please specify 'search' or 'fetch' mode")
    
    # Validate search parameters
    if args.mode == 'search':
        if args.num_results < 1:
            parser.error('Number of results must be at least 1')
        if args.num_results > 100:
            parser.error('Number of results cannot exceed 100')
        
        # Validate date formats if provided
        if args.from_date:
            try:
                time.strptime(args.from_date, '%Y-%m-%d')
            except ValueError:
                parser.error('Invalid from-date format. Use YYYY-MM-DD')
        
        if args.to_date:
            try:
                time.strptime(args.to_date, '%Y-%m-%d')
            except ValueError:
                parser.error('Invalid to-date format. Use YYYY-MM-DD')
    
    return args


def get_linkup_api_key():
    """Get Linkup API key from environment variable."""
    api_key = os.environ.get('LINKUP_API_KEY')
    if not api_key:
        print("Error: LINKUP_API_KEY environment variable not set.")
        print("Get your free API key from: https://app.linkup.so/")
        print("Set it with: export LINKUP_API_KEY='your-api-key-here'")
        sys.exit(1)
    return api_key


def linkup_search(query, num_results=10, depth='standard', output_type='searchResults',
                  from_date=None, to_date=None, include_domains=None, exclude_domains=None,
                  json_output=False):
    """
    Perform a Linkup search and print the results.
    
    Args:
        query (str): The search query string
        num_results (int): Number of results to display
        depth (str): 'standard' or 'deep'
        output_type (str): 'searchResults', 'sourcedAnswer', or 'structured'
        from_date (str): Filter from date (YYYY-MM-DD)
        to_date (str): Filter to date (YYYY-MM-DD)
        include_domains (list): Domains to include
        exclude_domains (list): Domains to exclude
        json_output (bool): If True, output raw JSON
    """
    import json
    
    api_key = get_linkup_api_key()
    base_url = "https://api.linkup.so/v1/search"
    
    params = {
        'q': query,
        'depth': depth,
        'outputType': output_type,
        'maxResults': min(num_results, 100)
    }
    
    # Add optional parameters
    if from_date:
        params['fromDate'] = from_date
    if to_date:
        params['toDate'] = to_date
    if include_domains:
        params['includeDomains'] = ','.join(include_domains[:100])  # Max 100
    if exclude_domains:
        params['excludeDomains'] = ','.join(exclude_domains)
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    try:
        if json_output:
            # Build structured JSON output for coding agents
            output = {
                'mode': 'search',
                'query': query,
                'parameters': {
                    'num_results_requested': num_results,
                    'depth': depth,
                    'output_type': output_type
                },
                'results': [],
                'error': False
            }
        else:
            print(f"\n{'='*60}")
            print(f"Linkup Search Results for: {query}")
            print(f"Depth: {depth}, Output Type: {output_type}")
            print(f"Showing up to {min(num_results, 100)} results")
            print(f"{'='*60}\n")
        
        response = requests.post(base_url, json=params, headers=headers, timeout=60)
        
        if response.status_code != 200:
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', response.text[:500])
            
            if json_output:
                output['error'] = True
                output['error_message'] = error_msg
                output['status_code'] = response.status_code
                print(json.dumps(output, indent=2))
            else:
                print(f"Error: API returned status code {response.status_code}")
                print(f"Details: {error_msg}")
            sys.exit(1)
        
        data = response.json()
        
        # Handle different output types
        if output_type == 'searchResults':
            # Linkup API uses 'results' key (not 'sources')
            sources = data.get('results', [])
            
            if json_output:
                for source in sources[:num_results]:
                    output['results'].append({
                        'name': source.get('name', ''),
                        'url': source.get('url', ''),
                        'content': source.get('content', ''),
                        'type': 'source'
                    })
                
                output['total_found'] = len(sources)
                print(json.dumps(output, indent=2))
            else:
                if not sources:
                    print("No results found.")
                    return
                
                result_count = 0
                for source in sources[:num_results]:
                    result_count += 1
                    
                    name = source.get('name', 'No title')
                    url = source.get('url', '')
                    content = source.get('content', '')
                    
                    print(f"{result_count}. {name}")
                    print(f"   URL: {url}")
                    if content:
                        # Clean up content (remove extra whitespace, limit length)
                        content = ' '.join(content.split())
                        if len(content) > 200:
                            content = content[:200] + "..."
                        print(f"   Content: {content}")
                    print()
                
                print(f"Total results displayed: {result_count}")
        
        elif output_type == 'sourcedAnswer':
            answer = data.get('answer', '')
            sources = data.get('sources', [])
            
            if json_output:
                output['answer'] = answer
                output['sources'] = [
                    {
                        'name': s.get('name', ''),
                        'url': s.get('url', ''),
                        'content': s.get('content', '')
                    }
                    for s in sources[:num_results]
                ]
                print(json.dumps(output, indent=2))
            else:
                print(f"\nAnswer:\n{answer}\n")
                
                if sources:
                    print("Sources:")
                    for i, source in enumerate(sources[:num_results], 1):
                        print(f"  {i}. {source.get('name', 'Unknown')} ({source.get('url', '')})")
        
        elif output_type == 'structured':
            # Structured output follows the schema provided
            if json_output:
                output['structured_data'] = data
                print(json.dumps(output, indent=2))
            else:
                print(json.dumps(data, indent=2))
    
    except requests.exceptions.Timeout:
        if json_output:
            output = {
                'mode': 'search',
                'query': query,
                'error': True,
                'error_message': 'Request timed out'
            }
            print(json.dumps(output, indent=2))
        else:
            print("Error: Request timed out.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        if json_output:
            output = {
                'mode': 'search',
                'query': query,
                'error': True,
                'error_message': f'Failed to make request - {str(e)}'
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Error: Failed to make request - {e}")
        sys.exit(1)
    except Exception as e:
        if json_output:
            output = {
                'mode': 'search',
                'query': query,
                'error': True,
                'error_message': str(e)
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Error: {e}")
        sys.exit(1)


def linkup_fetch(url, output_format='markdown', render_js=False, json_output=False):
    """
    Fetch a web page using Linkup's /fetch endpoint.
    
    Args:
        url (str): URL to fetch
        output_format (str): 'html' or 'markdown'
        render_js (bool): Execute JavaScript
        json_output (bool): If True, output raw JSON
    """
    import json
    
    api_key = get_linkup_api_key()
    base_url = "https://api.linkup.so/v1/fetch"
    
    params = {
        'url': url,
        'outputFormat': output_format
    }
    
    if render_js:
        params['renderJS'] = True
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    try:
        if json_output:
            output = {
                'mode': 'fetch',
                'url': url,
                'parameters': {
                    'output_format': output_format,
                    'render_js': render_js
                },
                'content': '',
                'error': False
            }
        else:
            print(f"\n{'='*60}")
            print(f"Fetching: {url}")
            print(f"Format: {output_format}, Render JS: {render_js}")
            print(f"{'='*60}\n")
        
        response = requests.post(base_url, json=params, headers=headers, timeout=60)
        
        if response.status_code != 200:
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', response.text[:500])
            
            if json_output:
                output['error'] = True
                output['error_message'] = error_msg
                output['status_code'] = response.status_code
                print(json.dumps(output, indent=2))
            else:
                print(f"Error: API returned status code {response.status_code}")
                print(f"Details: {error_msg}")
            sys.exit(1)
        
        data = response.json()
        content = data.get('content', '')
        
        if json_output:
            output['content'] = content
            output['url'] = data.get('url', url)
            output['output_format'] = data.get('outputFormat', output_format)
            output['timestamp'] = data.get('timestamp', '')
            print(json.dumps(output, indent=2))
        else:
            print(f"URL: {data.get('url', url)}")
            print(f"Format: {data.get('outputFormat', output_format)}")
            print(f"Timestamp: {data.get('timestamp', '')}")
            print(f"\n{'-'*60}\n")
            print(content)
            print(f"\n{'-'*60}")
    
    except requests.exceptions.Timeout:
        if json_output:
            output = {
                'mode': 'fetch',
                'url': url,
                'error': True,
                'error_message': 'Request timed out'
            }
            print(json.dumps(output, indent=2))
        else:
            print("Error: Request timed out.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        if json_output:
            output = {
                'mode': 'fetch',
                'url': url,
                'error': True,
                'error_message': f'Failed to make request - {str(e)}'
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Error: Failed to make request - {e}")
        sys.exit(1)
    except Exception as e:
        if json_output:
            output = {
                'mode': 'fetch',
                'url': url,
                'error': True,
                'error_message': str(e)
            }
            print(json.dumps(output, indent=2))
        else:
            print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    args = parse_arguments()
    
    if args.mode == 'search':
        # Join all query arguments to support queries with spaces
        user_query = " ".join(args.query)
        linkup_search(
            query=user_query,
            num_results=args.num_results,
            depth=args.depth,
            output_type=args.output_type,
            from_date=args.from_date,
            to_date=args.to_date,
            include_domains=args.include_domains,
            exclude_domains=args.exclude_domains,
            json_output=args.json
        )
    
    elif args.mode == 'fetch':
        linkup_fetch(
            url=args.url,
            output_format=args.output_format,
            render_js=args.render_js,
            json_output=args.json
        )
