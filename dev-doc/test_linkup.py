#!/usr/bin/env python3
"""
Test script to demonstrate Linkup Search functionality.
Run this after setting your LINKUP_API_KEY environment variable.
"""

import subprocess
import json
import sys


def run_command(cmd):
    """Run a command and return output."""
    print(f"\n{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    print('='*60)
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd='/Users/ugo/tmp/ws'
    )
    
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.stdout, result.returncode


def parse_json_output(output):
    """Parse JSON output for programmatic use."""
    try:
        data = json.loads(output.strip())
        
        print("\n=== Programmatic Access ===")
        if 'mode' in data:
            print(f"Mode: {data['mode']}")
        
        if data.get('error'):
            print(f"Error: {data.get('error_message', 'Unknown error')}")
            return None
        
        if data['mode'] == 'search':
            print(f"Query: {data.get('query')}")
            print(f"Results found: {data.get('total_found', len(data.get('results', [])))}")
            
            if 'results' in data and data['results']:
                print(f"\nFirst result:")
                first = data['results'][0]
                print(f"  Title: {first.get('name', first.get('title', ''))}")
                print(f"  URL: {first.get('url', '')}")
                content = first.get('content', first.get('description', ''))
                if content:
                    print(f"  Content: {content[:150]}...")
            
            return data
        
        elif data['mode'] == 'fetch':
            print(f"URL: {data.get('url')}")
            print(f"Format: {data.get('output_format')}")
            content = data.get('content', '')
            if content:
                print(f"Content preview: {content[:200]}...")
            
            return data
    
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None


if __name__ == "__main__":
    print("="*60)
    print("Linkup Search Script - Test Suite")
    print("="*60)
    
    # Check for API key
    import os
    api_key = os.environ.get('LINKUP_API_KEY')
    if not api_key:
        print("\n⚠️  WARNING: LINKUP_API_KEY not set!")
        print("Set it with: export LINKUP_API_KEY='your-api-key-here'")
        print("\nFor testing without API key, see the example below.\n")
    
    # Test 1: Basic search
    print("\n🔍 TEST 1: Basic Search (Human-readable)")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'search',
        'python web scraping tutorials', '-n', '3'
    ])
    
    # Test 2: Search with JSON output
    print("\n📊 TEST 2: Search with JSON Output")
    print("="*60)
    output, code = run_command([
        'python', 'linkup_search.py', 'search',
        'machine learning basics', '-n', '3', '--json'
    ])
    
    if code == 0:
        parse_json_output(output)
    
    # Test 3: Deep search
    print("\n🔬 TEST 3: Deep Search (Comprehensive Research)")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'search',
        'quantum computing advances 2026', '--depth', 'deep', '-n', '5'
    ])
    
    # Test 4: Sourced Answer
    print("\n💬 TEST 4: Sourced Answer Mode")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'search',
        'What is Python programming?', '--output-type', 'sourcedAnswer'
    ])
    
    # Test 5: Date filtering
    print("\n📅 TEST 5: Date Filtered Search")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'search',
        'AI news', '--from-date', '2026-02-01', '--to-date', '2026-02-28', '-n', '3'
    ])
    
    # Test 6: Domain filtering
    print("\n🌐 TEST 6: Domain Filtered Search")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'search',
        'python documentation', '--include-domains',
        'python.org', 'realpython.com', '-n', '3'
    ])
    
    # Test 7: Fetch a page
    print("\n📄 TEST 7: Fetch Web Page")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'fetch',
        'https://www.python.org/about/', '-n', '1'
    ])
    
    # Test 8: Fetch with JSON
    print("\n📦 TEST 8: Fetch with JSON Output")
    print("="*60)
    output, code = run_command([
        'python', 'linkup_search.py', 'fetch',
        'https://docs.python.org/3/', '--json'
    ])
    
    if code == 0:
        parse_json_output(output)
    
    # Test 9: Fetch with JavaScript rendering
    print("\n⚡ TEST 9: Fetch with JavaScript Rendering")
    print("="*60)
    run_command([
        'python', 'linkup_search.py', 'fetch',
        'https://example.com', '--render-js'
    ])
    
    print("\n" + "="*60)
    print("Example Usage for Coding Agents:")
    print("="*60)
    print("""
# Python Integration
import subprocess
import json

# Search
result = subprocess.run(
    ['python', 'linkup_search.py', 'search', 'python tutorials', '-n', '5', '--json'],
    capture_output=True, text=True
)
data = json.loads(result.stdout)
for item in data['results']:
    print(f"{item['name']}: {item['url']}")

# Fetch
result = subprocess.run(
    ['python', 'linkup_search.py', 'fetch', 'https://example.com', '--json'],
    capture_output=True, text=True
)
data = json.loads(result.stdout)
print(data['content'])

# Shell Integration
python linkup_search.py search "query" --json | jq '.results[].url'
python linkup_search.py fetch "https://example.com" > page.md
""")
    
    print("\n" + "="*60)
    print("All tests completed!")
    print("="*60)
