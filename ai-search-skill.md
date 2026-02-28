---
name: ai-search-skill
description: Enables coding agents to perform real-time web searches and deep content retrieval using Brave Search and Linkup Search APIs. Use this when the user asks for current events, technical documentation not in the local codebase, complex research requiring multi-step analysis, or when verified sources are needed.
dependencies: python>=3.8, requests
---

# AI Search Skill for Coding Agents

## Overview
The **AI Search** toolkit provides two powerful command-line utilities that coding agents can invoke to perform web searches with different capabilities:

| Tool | Purpose | Best Use Case | Key Features |
|------|---------|---------------|--------------|
| **search.py** (Brave Search) | Privacy-focused web search using Brave's independent index | Quick factual queries, documentation lookups, privacy-conscious searches | Fast responses (~1-3s), 2,000 free queries/month, structured JSON output |
| **linkup_search.py** (Linkup Search) | Agentic search with superior factuality and deep research capabilities | Complex research, fact-checking, building AI applications, content extraction | Deep multi-step research, multiple output types, content fetching, JavaScript rendering |

Both tools output **machine-readable JSON** (or human-readable text) which downstream agents can parse and act upon.

---

## 1. Brave Search Tool (`search.py`)

### Command
```bash
python brave_search.py "<query>" [-n <N>] [--json]
```
* `<query>` – the search string (use quotes for multi-word queries).
* `-n <N>` – number of results to return (default: 10, range: 1-100).
* `--json` – output as raw JSON for programmatic use (recommended for agents).

### JSON Output Schema
```json
{
  "query": "string",
  "num_results_requested": int,
  "num_results_found": int,
  "results": [
    {
      "title": "string",
      "url": "string",
      "description": "string",
      "engine": "brave_search"
    },
    ...
  ]
}
```
Each object represents a search result with title, URL, description, and engine identifier.

### Example Usage
```bash
# Basic search with human-readable output
python brave_search.py "python web scraping tutorial" -n 5

# Get structured JSON for processing
python brave_search.py "FastAPI dependency injection documentation" --json

# Combine options for maximum control
python brave_search.py "machine learning frameworks 2026" -n 10 --json
```

### JSON Output Example
```json
{
  "query": "python web scraping",
  "num_results_requested": 5,
  "num_results_found": 42,
  "results": [
    {
      "title": "GeeksforGeeks - Python Web Scraping",
      "url": "https://www.geeksforgeeks.org/python-web-scraping/",
      "description": "Learn Python web scraping with BeautifulSoup, Scrapy, and more...",
      "engine": "brave_search"
    },
    {
      "title": "Real Python - Beautiful Soup Tutorial",
      "url": "https://realpython.com/beautiful-soup-web-scraper-python/",
      "description": "Build a web scraper with Python using Beautiful Soup library...",
      "engine": "brave_search"
    }
  ]
}
```

---

## 2. Linkup Search Tool (`linkup_search.py`)

### Commands

#### Search Mode
```bash
python linkup_search.py search "<query>" [-n <N>] [--depth <depth>] [--output-type <type>] [--json]
```
* `<query>` – the search string (required).
* `-n <N>` – number of results to return (default: 10, range: 1-100).
* `--depth <depth>` – search depth: `standard` (fast) or `deep` (comprehensive, default: standard).
* `--output-type <type>` – output type: `searchResults`, `sourcedAnswer`, or `structured` (default: searchResults).
* `--from-date <YYYY-MM-DD>` – filter results from date (optional).
* `--to-date <YYYY-MM-DD>` – filter results to date (optional).
* `--include-domains <domain1> [domain2 ...]` – restrict to specific domains (optional).
* `--exclude-domains <domain1> [domain2 ...]` – exclude specific domains (optional).
* `--json` – output as raw JSON (recommended for agents).

#### Fetch Mode
```bash
python linkup_search.py fetch "<url>" [--output-format <format>] [--render-js] [--json]
```
* `<url>` – the URL to fetch (required).
* `--output-format <format>` – output format: `html` or `markdown` (default: markdown).
* `--render-js` – execute JavaScript before extraction (default: false).
* `--json` – output as raw JSON (recommended for agents).

### JSON Output Schemas

#### Search Results Output Type
```json
{
  "mode": "search",
  "query": "string",
  "parameters": {
    "num_results_requested": int,
    "depth": "standard|deep",
    "output_type": "searchResults"
  },
  "results": [
    {
      "name": "string",
      "url": "string",
      "content": "string",
      "type": "source"
    },
    ...
  ],
  "error": boolean,
  "total_found": int
}
```

#### Sourced Answer Output Type
```json
{
  "mode": "search",
  "query": "string",
  "parameters": {
    "num_results_requested": int,
    "depth": "standard|deep",
    "output_type": "sourcedAnswer"
  },
  "answer": "string",
  "sources": [
    {
      "name": "string",
      "url": "string",
      "content": "string"
    },
    ...
  ],
  "error": boolean
}
```

#### Fetch Output
```json
{
  "mode": "fetch",
  "url": "string",
  "parameters": {
    "output_format": "markdown|html",
    "render_js": boolean
  },
  "content": "string",
  "output_format": "string",
  "timestamp": "ISO8601 timestamp",
  "error": boolean
}
```

### Example Usage

#### Basic Search
```bash
# Standard search with default settings
python linkup_search.py search "open source licenses" -n 5

# Deep research for complex topics
python linkup_search.py search "AI trends 2026" --depth deep -n 10

# Get natural language answer with citations
python linkup_search.py search "what is machine learning" --output-type sourcedAnswer
```

#### Advanced Filtering
```bash
# Date-ranged search
python linkup_search.py search "Python updates" \
  --from-date 2026-01-01 \
  --to-date 2026-02-28 \
  -n 10

# Domain-specific search
python linkup_search.py search "Python documentation" \
  --include-domains python.org docs.python.org \
  -n 5

# Exclude certain domains
python linkup_search.py search "programming tutorials" \
  --exclude-domains medium.com reddit.com \
  -n 10
```

#### Content Fetching
```bash
# Fetch webpage in markdown format
python linkup_search.py fetch "https://docs.python.org"

# Fetch with HTML output
python linkup_search.py fetch "https://example.com/article" --output-format html

# Fetch dynamic content with JavaScript rendering
python linkup_search.py fetch "https://dynamic-site.com" --render-js --json
```

### JSON Output Examples

#### Search Results
```json
{
  "mode": "search",
  "query": "open source licenses",
  "parameters": {
    "num_results_requested": 5,
    "depth": "standard",
    "output_type": "searchResults"
  },
  "results": [
    {
      "name": "Licenses - Open Source Initiative",
      "url": "https://opensource.org/licenses",
      "content": "OSI Approved Licenses Open source licenses are licenses that comply with the Open Source Definition...",
      "type": "source"
    },
    {
      "name": "Open source licenses grant permission...",
      "url": "https://choosealicense.com/licenses/",
      "content": "Open source licenses grant permission for anybody to use, modify, and share licensed software...",
      "type": "source"
    }
  ],
  "error": false,
  "total_found": 5
}
```

#### Sourced Answer
```json
{
  "mode": "search",
  "query": "what is machine learning",
  "parameters": {
    "num_results_requested": 10,
    "depth": "standard",
    "output_type": "sourcedAnswer"
  },
  "answer": "Machine learning is a subset of artificial intelligence that focuses on developing algorithms and models that enable computers to learn from and make predictions based on data...",
  "sources": [
    {
      "name": "Stanford Encyclopedia of Philosophy",
      "url": "https://plato.stanford.edu/",
      "content": "Comprehensive overview of machine learning concepts..."
    },
    {
      "name": "MIT Technology Review",
      "url": "https://www.technologyreview.com/",
      "content": "Latest developments in machine learning research..."
    }
  ],
  "error": false
}
```

#### Fetched Content
```json
{
  "mode": "fetch",
  "url": "https://docs.python.org",
  "parameters": {
    "output_format": "markdown",
    "render_js": false
  },
  "content": "# Welcome to Python's Official Documentation\n\nPython is an interpreted, high-level programming language...\n\n[Full extracted content]",
  "output_format": "markdown",
  "timestamp": "2026-02-28T10:30:00Z",
  "error": false
}
```

---

## 3. Workflow Patterns for Agents

### Pattern 1: Search → Process Pipeline
```bash
# 1) Get URLs from Brave Search
urls=$(python brave_search.py "python web scraping" -n 5 --json | jq -r '.results[].url')

# 2) For each URL, fetch content with Linkup
for u in $urls; do
    python linkup_search.py fetch "$u" --json | jq '.'
done
```

### Pattern 2: Deep Research with Verification
```bash
# 1) Perform deep research
research=$(python linkup_search.py search "quantum computing breakthroughs 2026" \
  --depth deep \
  --output-type sourcedAnswer \
  --json)

# 2) Extract answer and sources
echo "$research" | jq '.answer'
echo "$research" | jq '.sources[] | "\(.name): \(.url)"'
```

### Pattern 3: Content Aggregation
```bash
# Aggregate multiple web pages
urls=("https://docs.python.org" "https://fastapi.tiangolo.com" "https://pydantic.dev")

for url in "${urls[@]}"; do
    echo "Fetching: $url"
    python linkup_search.py fetch "$url" --json | jq '{url, content_length: (.content | length)}'
done
```

### Pattern 4: Fact-Checking Workflow
```bash
# Verify a claim using deep search
claim="Python 3.12 improved performance by 10%"
verification=$(python linkup_search.py search "$claim verified" \
  --depth deep \
  --output-type sourcedAnswer \
  --json)

# Extract verification and confidence
echo "$verification" | jq '.answer'
echo "$verification" | jq '.sources | length'
```

### Pattern 5: Time-Restricted Research
```bash
# Find recent developments in a field
python linkup_search.py search "LLM optimization techniques" \
  --from-date 2026-01-01 \
  --to-date 2026-02-28 \
  --depth deep \
  -n 15 \
  --json
```

---

## 4. Error Handling

### Common Errors and Solutions

#### API Key Not Set
```
Error: BRAVE_API_KEY environment variable not set.
Get your free API key from: https://api-dashboard.search.brave.com/
Set it with: export BRAVE_API_KEY='your-api-key-here'
```

**Solution**: Set the appropriate environment variable before running the script.

#### Request Timed Out
```
Error: Request timed out.
```

**Solution**: 
- Check internet connection
- Reduce number of results with `-n`
- Use `--depth standard` instead of `deep` for Linkup
- Try again later

#### Invalid API Key
```
Error: API returned status code 401
Details: Invalid API key
```

**Solution**: Verify your API key at the respective dashboard and ensure no extra spaces.

#### No Results Found
```
No results found.
```

**Solution**: 
- Try different search terms
- Increase result count with `-n`
- Check spelling and query format
- For Linkup, try `--depth deep` for complex queries

### Robust Error Handling Pattern (Python)

```python
import subprocess
import json
from typing import Tuple, Optional, Dict

def safe_brave_search(
    query: str, 
    num_results: int = 10,
    max_retries: int = 2
) -> Tuple[bool, Optional[Dict], Optional[str]]:
    """
    Perform Brave search with robust error handling.
    
    Returns:
        Tuple of (success, results_dict, error_message)
    """
    for attempt in range(max_retries):
        try:
            cmd = [
                'python', 'search.py',
                query,
                '-n', str(num_results),
                '--json'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip()
                if attempt == max_retries - 1:
                    return False, None, f"Search failed: {error_msg}"
                continue
            
            data = json.loads(result.stdout)
            return True, data, None
            
        except Exception as e:
            if attempt == max_retries - 1:
                return False, None, f"Unexpected error: {str(e)}"
            continue
    
    return False, None, "Max retries exceeded"


def safe_linkup_search(
    query: str,
    num_results: int = 10,
    depth: str = 'standard',
    max_retries: int = 3
) -> Tuple[bool, Optional[Dict], Optional[str]]:
    """
    Perform Linkup search with retry logic and exponential backoff.
    """
    import time
    
    for attempt in range(max_retries):
        try:
            cmd = [
                'python', 'linkup_search.py', 'search',
                query,
                '-n', str(num_results),
                '--depth', depth,
                '--json'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip()
                if attempt < max_retries - 1:
                    sleep_time = 2 ** attempt
                    time.sleep(sleep_time)
                    continue
                return False, None, f"Search failed after {max_retries} attempts"
            
            data = json.loads(result.stdout)
            
            # Check for errors in response
            if data.get('error'):
                error_msg = data.get('error_message', 'Unknown error')
                if attempt < max_retries - 1:
                    sleep_time = 2 ** attempt
                    time.sleep(sleep_time)
                    continue
                return False, None, error_msg
            
            return True, data, None
            
        except subprocess.TimeoutExpired:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return False, None, "Request timed out"
            
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return False, None, f"Unexpected error: {str(e)}"
    
    return False, None, "Max retries exceeded"
```

---

## 5. Prerequisites & Installation

### Requirement: Python 3.7+

Ensure you have Python 3.7 or higher installed:
```bash
python3 --version
```

### Step 1: Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
# Install dependencies for both tools
pip install -r requirements.txt
```

### Step 3: Configure API Keys

#### Brave Search API Key
1. Visit [https://api-dashboard.search.brave.com/](https://api-dashboard.search.brave.com/)
2. Sign up for a free account
3. Generate an API key (free tier includes 2,000 queries/month)
4. Set as environment variable:
   ```bash
   export BRAVE_API_KEY="your-brave-api-key-here"
   ```

#### Linkup Search API Key
1. Visit [https://app.linkup.so/](https://app.linkup.so/)
2. Sign up for a free account
3. Generate an API key
4. Set as environment variable:
   ```bash
   export LINKUP_API_KEY="your-linkup-api-key-here"
   ```

### Step 4: Verify Installation
```bash
# Test Brave Search
python brave_search.py "test query" -n 3 --json

# Test Linkup Search
python linkup_search.py search "test query" -n 3 --json
```

---

## 6. When to Use Each Tool

### Choose Brave Search When:
- ✅ Need quick, simple answers
- ✅ Privacy is the primary concern
- ✅ Searching for basic documentation
- ✅ Working within tight time constraints
- ✅ Budget is limited (free tier: 2,000 queries/month)
- ✅ Simple citation needs

### Choose Linkup Search When:
- ✅ Building AI applications requiring high accuracy
- ✅ Need verified, factually-grounded responses
- ✅ Complex research questions requiring multi-step analysis
- ✅ Want natural language answers with citations
- ✅ Need to extract content from web pages
- ✅ Require structured data extraction
- ✅ Fact-checking claims or verifying information
- ✅ Building chatbots or research assistants

---

## 7. Performance Comparison

| Metric | Brave Search | Linkup Search (Standard) | Linkup Search (Deep) |
|--------|-------------|-------------------------|---------------------|
| **Response Time** | ~1-3 seconds | ~1-3 seconds | ~5-10 seconds |
| **Factuality** | Good | ⭐ Excellent | ⭐⭐ Superior |
| **Best For** | Quick facts | Balanced research | Complex analysis |
| **Output Types** | Basic | 3 types | 3 types |
| **Content Fetching** | ❌ No | ✅ Yes | ✅ Yes |
| **JavaScript Render** | ❌ No | ✅ Yes | ✅ Yes |
| **Free Tier** | 2,000/mo | Available | Available |

---

## 8. Extending the Skill

If new capabilities are required (e.g., custom filtering, caching, or batch processing), add new features to the existing scripts:

### Adding Custom Parameters
Edit `search.py` or `linkup_search.py` to accept additional command-line arguments:

```python
# Example: Add custom parameter to search.py
parser.add_argument(
    '--country',
    dest='country',
    help='Country code for localized results'
)
```

### Adding Caching Layer
Implement result caching to avoid redundant API calls:

```python
# Add to search.py or linkup_search.py
import hashlib
import json
from pathlib import Path

def cache_key(query: str, params: dict) -> str:
    """Generate unique cache key for query + parameters."""
    key_data = f"{query}:{json.dumps(params, sort_keys=True)}"
    return hashlib.sha256(key_data.encode()).hexdigest()

def get_cached_result(cache_key: str, cache_dir: Path = Path("./cache")) -> Optional[dict]:
    """Retrieve cached result if available."""
    cache_file = cache_dir / f"{cache_key}.json"
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return json.load(f)
    return None
```

### Adding Batch Processing
Process multiple queries efficiently:

```bash
# Create a batch processing script
cat > batch_search.sh << 'EOF'
#!/bin/bash
# Process multiple queries from a file

QUERY_FILE="$1"
OUTPUT_FILE="${2:-batch_results.json}"

echo "[" > "$OUTPUT_FILE"
first=true

while IFS= read -r query; do
    if [ -n "$query" ]; then
        if [ "$first" = true ]; then
            first=false
        else
            echo "," >> "$OUTPUT_FILE"
        fi
        
        result=$(python linkup_search.py search "$query" --depth deep --json)
        echo "$result" >> "$OUTPUT_FILE"
    fi
done < "$QUERY_FILE"

echo "]" >> "$OUTPUT_FILE"
echo "Batch processing complete. Results saved to $OUTPUT_FILE"
EOF

chmod +x batch_search.sh
./batch_search.sh queries.txt results.json
```

---

## 9. Testing Your Setup

### Verification Script

Create `test_ai_search_skill.py`:

```python
#!/usr/bin/env python3
"""Test script to verify AI Search skill integration."""

import subprocess
import json
import sys
from typing import List, Dict

def test_brave_search() -> bool:
    """Test Brave Search functionality."""
    print("Testing Brave Search...")
    
    cmd = ['python', 'brave_search.py', 'python tutorial', '-n', '3', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    if result.returncode != 0:
        print(f"❌ Failed: {result.stderr}")
        return False
    
    try:
        data = json.loads(result.stdout)
        if not data.get('results'):
            print("❌ No results found")
            return False
        
        print(f"✅ Success! Found {len(data['results'])} results")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False

def test_linkup_search() -> bool:
    """Test Linkup Search functionality."""
    print("\nTesting Linkup Search...")
    
    cmd = ['python', 'linkup_search.py', 'search', 'machine learning', '-n', '3', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if result.returncode != 0:
        print(f"❌ Failed: {result.stderr}")
        return False
    
    try:
        data = json.loads(result.stdout)
        if not data.get('results'):
            print("❌ No results found")
            return False
        
        print(f"✅ Success! Found {len(data['results'])} results")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False

def test_linkup_fetch() -> bool:
    """Test Linkup Fetch functionality."""
    print("\nTesting Linkup Fetch...")
    
    cmd = ['python', 'linkup_search.py', 'fetch', 'https://docs.python.org', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if result.returncode != 0:
        print(f"❌ Failed: {result.stderr}")
        return False
    
    try:
        data = json.loads(result.stdout)
        if not data.get('content'):
            print("⚠️  Fetch completed but no content")
            return True  # Still counts as success
        
        print(f"✅ Success! Content length: {len(data['content'])} chars")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False

if __name__ == '__main__':
    print("="*60)
    print("AI Search Skill Verification")
    print("="*60)
    
    tests_passed = 0
    tests_total = 0
    
    tests_total += 1
    if test_brave_search():
        tests_passed += 1
    
    tests_total += 1
    if test_linkup_search():
        tests_passed += 1
    
    tests_total += 1
    if test_linkup_fetch():
        tests_passed += 1
    
    print(f"\n{'='*60}")
    print(f"Tests passed: {tests_passed}/{tests_total}")
    print(f"{'='*60}")
    
    sys.exit(0 if tests_passed == tests_total else 1)
```

Run the verification:
```bash
python test_ai_search_skill.py
```

---

## 10. Additional Resources

### Official Documentation
- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [Linkup Python SDK](https://docs.linkup.so/pages/sdk/python/python)

### Project Documentation
- [Main README](./README.md)
- [Brave Search Features](./dev-doc/FEATURES_SUMMARY.md)
- [Linkup Search Features](./dev-doc/FEATURES_LINKUP.md)
- [Project Overview](./dev-doc/PROJECT_SUMMARY.md)
- [Bug Fixes](./dev-doc/FIX_APPLIED.md)

### Integration Examples
- [Example JSON Output Guide](./dev-doc/EXAMPLE_JSON_OUTPUT.md)
- [LangChain Integration](https://docs.langchain.com/)
- [CrewAI Integration](https://docs.crewai.com/)

---

## 11. Troubleshooting Checklist

### Before Using the Tools
- [ ] `BRAVE_API_KEY` environment variable is set
- [ ] `LINKUP_API_KEY` environment variable is set
- [ ] Dependencies are installed (`pip install -r requirements.txt`)
- [ ] Virtual environment is activated
- [ ] Internet connection is working
- [ ] API keys are valid (check dashboards)

### If Search Returns No Results
- [ ] Try different search terms
- [ ] Increase result count with `-n`
- [ ] Check spelling and query format
- [ ] For Linkup, try `--depth deep` for complex queries
- [ ] Verify API credits available

### If Request Times Out
- [ ] Check internet connection
- [ ] Reduce number of results with `-n`
- [ ] Use `--depth standard` instead of `deep` for Linkup
- [ ] Try again later

### If API Key Errors Occur
- [ ] Verify API key at respective dashboard
- [ ] Ensure no extra spaces in key
- [ ] Check account status and credits
- [ ] Regenerate key if expired

---

*End of AI Search Skill description.*

*Generated by AI Search Skill on 2026-02-28*
