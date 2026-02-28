#!/usr/bin/env python3
"""
Test script to demonstrate JSON output from search.py
Run this after setting your BRAVE_API_KEY environment variable.
"""

import subprocess
import json
import sys


def run_search(query, num_results=5, use_json=False):
    """Run the search script and return results."""
    cmd = ['python', 'search.py', query]
    if num_results:
        cmd.extend(['-n', str(num_results)])
    if use_json:
        cmd.append('--json')
    
    print(f"Running: {' '.join(cmd)}")
    print("-" * 60)
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd='/Users/ugo/tmp/ws'
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.stdout, result.returncode


def parse_json_output(output):
    """Parse JSON output for programmatic use."""
    try:
        data = json.loads(output.strip())
        
        # Example: Access specific fields
        print("\n=== Programmatic Access ===")
        print(f"Query: {data.get('query')}")
        print(f"Results found: {data.get('num_results_found')}")
        
        if 'results' in data:
            print(f"\nFirst result:")
            first = data['results'][0]
            print(f"  Title: {first.get('title')}")
            print(f"  URL: {first.get('url')}")
            print(f"  Description: {first.get('description')}")
        
        return data
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("Brave Search Script - Test Suite")
    print("=" * 60)
    
    # Check for API key
    import os
    api_key = os.environ.get('BRAVE_API_KEY')
    if not api_key:
        print("\n⚠️  WARNING: BRAVE_API_KEY not set!")
        print("Set it with: export BRAVE_API_KEY='your-api-key-here'")
        print("\nFor testing without API key, see the example below.\n")
    
    # Test 1: Human-readable output (default)
    print("\n📋 TEST 1: Human-readable output (default)")
    print("=" * 60)
    run_search("python web scraping", num_results=3, use_json=False)
    
    # Test 2: JSON output
    print("\n📊 TEST 2: JSON output (--json flag)")
    print("=" * 60)
    output, code = run_search("python web scraping", num_results=3, use_json=True)
    
    # Parse and show programmatic access
    if code == 0:
        parse_json_output(output)
    
    # Test 3: Different number of results
    print("\n🔢 TEST 3: Custom number of results")
    print("=" * 60)
    run_search("machine learning tutorials", num_results=7, use_json=False)
    
    # Test 4: JSON with custom count
    print("\n📦 TEST 4: JSON with custom count")
    print("=" * 60)
    output, code = run_search("machine learning", num_results=7, use_json=True)
    
    if code == 0:
        parse_json_output(output)
    
    print("\n" + "=" * 60)
    print("Example usage for coding agents:")
    print("=" * 60)
    print("""
# Python example:
import subprocess
import json

result = subprocess.run(
    ['python', 'search.py', 'python tutorials', '-n', '5', '--json'],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)
for item in data['results']:
    print(f"{item['title']}: {item['url']}")

# Shell example:
python search.py "query" --json | jq '.results[].url'

# Node.js example:
const { execSync } = require('child_process');
const data = JSON.parse(execSync('python search.py "query" --json'));
console.log(data.results[0].title);
""")
