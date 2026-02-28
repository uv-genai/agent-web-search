#!/usr/bin/env python3
"""
Quick test script to verify Linkup API connection and authentication.
Run this to diagnose why you're getting no results.
"""

import os
import requests
import json

def test_linkup_api():
    """Test the Linkup API directly."""
    
    # Get API key
    api_key = os.environ.get('LINKUP_API_KEY')
    
    if not api_key:
        print("❌ ERROR: LINKUP_API_KEY environment variable is NOT set!")
        print("\nPlease run:")
        print("  export LINKUP_API_KEY='your-api-key-here'")
        print("\nGet your free API key from: https://app.linkup.so/")
        return False
    
    print("✅ API Key found in environment")
    
    # Test search endpoint
    base_url = "https://api.linkup.so/v1/search"
    
    query = "open source licenses"
    
    params = {
        'q': query,
        'depth': 'standard',
        'outputType': 'searchResults',
        'maxResults': 5
    }
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    print(f"\n🔍 Testing search for: '{query}'")
    print(f"URL: {base_url}")
    print(f"Parameters: {json.dumps(params, indent=2)}\n")
    
    try:
        response = requests.post(base_url, json=params, headers=headers, timeout=30)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}\n")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ SUCCESS! API returned data:")
            print(json.dumps(data, indent=2))
            
            sources = data.get('sources', [])
            print(f"\n📊 Found {len(sources)} sources")
            
            if len(sources) > 0:
                print("\nFirst result:")
                print(f"  Name: {sources[0].get('name', 'N/A')}")
                print(f"  URL: {sources[0].get('url', 'N/A')}")
                print(f"  Content preview: {sources[0].get('content', '')[:200]}...")
            
            return True
        else:
            print(f"❌ ERROR: Status code {response.status_code}")
            print(f"Response text: {response.text[:500]}")
            
            try:
                error_data = response.json()
                print(f"Error details: {json.dumps(error_data, indent=2)}")
            except:
                pass
            
            return False
    
    except requests.exceptions.Timeout:
        print("❌ ERROR: Request timed out")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"❌ ERROR: Connection failed - {e}")
        print("Check your internet connection")
        return False
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {e}")
        return False


if __name__ == "__main__":
    print("="*60)
    print("Linkup API Connection Test")
    print("="*60)
    
    success = test_linkup_api()
    
    print("\n" + "="*60)
    if success:
        print("✅ API connection successful!")
        print("\nNow you can use the main script:")
        print("  python linkup_search.py search \"open source licenses\" -n 5")
    else:
        print("❌ API connection failed!")
        print("\nTroubleshooting steps:")
        print("1. Make sure you have an API key from https://app.linkup.so/")
        print("2. Set it: export LINKUP_API_KEY='your-key-here'")
        print("3. Check that your API key is valid (not expired)")
        print("4. Verify your internet connection")
        print("5. Try with a simpler query like 'python tutorial'")
    print("="*60)
