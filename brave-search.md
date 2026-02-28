---
name: brave-search
description: Performs web searches using the Brave Search API to find up-to-date information, documentation, and technical answers. Use when the user asks for current events, external documentation, or "search the web".
dependencies: python>=3.8, requests
---

# Brave Search Skill

This skill allows you to access the web via the Brave Search API. Use it when you need information beyond your training data or specifically when the user requests a web search.

All the instructions in this document **ARE MANDATORY** and must be followed at all times.

## Overview

The Brave Search script (`search.py`) provides privacy-focused web searching using Brave's independent search index. It supports both human-readable output and structured JSON for programmatic use by coding agents.

### Key Capabilities

- ✅ Real-time web search results
- ✅ Privacy-focused (no tracking or profiling)
- ✅ Structured JSON output for automation
- ✅ Customizable result counts (1-100)
- ✅ Fast responses (~1-3 seconds)
- ✅ Free tier: 2,000 queries/month

## Prerequisites

Before using this skill, ensure:

1. **API Key Configuration**: The `BRAVE_API_KEY` environment variable must be set
   ```bash
   export BRAVE_API_KEY="your-api-key-here"
   ```
   Get your free key from: https://api-dashboard.search.brave.com/

2. **Dependencies Installed**: Ensure the project dependencies are installed
   ```bash
   pip install -r requirements.txt
   # OR using uv
   uv run pip install -r requirements.txt
   ```

3. **Virtual Environment**: Activate the virtual environment if available
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage Instructions

### Basic Usage Pattern

When you need to search the web, use the following pattern:

```python
import subprocess
import json

def search_web(query: str, num_results: int = 10) -> list[dict]:
    """Search the web using Brave Search API."""
    cmd = [
        'python', 'search.py',
        query,
        '-n', str(num_results),
        '--json'  # Always use JSON for programmatic access
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    if result.returncode != 0:
        raise RuntimeError(f"Search failed: {result.stderr}")
    
    return json.loads(result.stdout)
```

### Command-Line Interface

The script supports the following command-line options:

| Option | Description | Default | Required |
|--------|-------------|---------|----------|
| `query` | Search query string | - | Yes |
| `-n`, `--num-results` | Number of results (1-100) | 10 | No |
| `--json` | Output as raw JSON | False | Optional |
| `-h`, `--help` | Show help message | - | No |

### Common Search Patterns

#### 1. Simple Web Search
```bash
python search.py "python web scraping tutorial" -n 5
```

#### 2. Technical Documentation Search
```bash
python search.py "FastAPI dependency injection documentation" --json
```

#### 3. Current Events Search
```bash
python search.py "latest Python release features 2026" -n 10
```

#### 4. Code Example Search
```bash
python search.py "how to parse JSON in Python example" -n 5 --json
```

## Response Format

### Human-Readable Output (Default)

```
============================================================
Brave Search Results for: python web scraping
Showing 5 results
============================================================

1. GeeksforGeeks
   URL: https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/
   Description: Learn Python web scraping with BeautifulSoup, Scrapy, and more...

2. Real Python
   URL: https://realpython.com/beautiful-soup-web-scraper-python/
   Description: Build a web scraper with Python using Beautiful Soup library...

Total results displayed: 2
```

### JSON Output (Recommended for Agents)

```json
{
  "query": "python web scraping",
  "num_results_requested": 5,
  "num_results_found": 42,
  "results": [
    {
      "title": "GeeksforGeeks",
      "url": "https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/",
      "description": "Learn Python web scraping with BeautifulSoup...",
      "engine": "brave_search"
    },
    {
      "title": "Real Python",
      "url": "https://realpython.com/beautiful-soup-web-scraper-python/",
      "description": "Build a web scraper with Python using Beautiful Soup...",
      "engine": "brave_search"
    }
  ]
}
```

## Integration Examples

### Python Integration

#### Basic Search Function
```python
import subprocess
import json
from typing import Optional, List, Dict

class BraveSearchAgent:
    """Coding agent tool for Brave Search integration."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with optional API key override."""
        self.api_key = api_key or os.getenv('BRAVE_API_KEY')
        if not self.api_key:
            raise ValueError("BRAVE_API_KEY environment variable not set")
    
    def search(
        self, 
        query: str, 
        num_results: int = 10,
        as_json: bool = True
    ) -> Dict:
        """
        Perform a web search.
        
        Args:
            query: The search query string
            num_results: Number of results to return (1-100)
            as_json: If True, return structured JSON
            
        Returns:
            Dictionary containing search results
            
        Raises:
            RuntimeError: If search fails or API key is missing
        """
        if num_results < 1 or num_results > 100:
            raise ValueError("num_results must be between 1 and 100")
        
        cmd = [
            'python', 'search.py',
            *query.split(),
            '-n', str(num_results),
            '--json' if as_json else ''
        ]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        
        if result.returncode != 0:
            error_msg = result.stderr.strip() or "Unknown error"
            raise RuntimeError(f"Search failed: {error_msg}")
        
        return json.loads(result.stdout)
    
    def get_urls(self, query: str, limit: int = 5) -> List[str]:
        """Extract URLs from search results."""
        results = self.search(query, num_results=limit)
        return [r['url'] for r in results.get('results', [])]
    
    def find_documentation(self, topic: str) -> List[Dict]:
        """Find official documentation for a technology."""
        query = f"{topic} official documentation"
        results = self.search(query, num_results=10)
        
        # Filter for likely documentation sources
        doc_sites = ['docs.', 'documentation.', '.io/docs', '/docs/']
        return [
            r for r in results.get('results', [])
            if any(site in r.get('url', '').lower() for site in doc_sites)
        ][:5]
```

### LangChain Tool Integration

```python
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class BraveSearchInput(BaseModel):
    """Input for Brave Search tool."""
    query: str = Field(..., description="Search query string")
    num_results: int = Field(default=5, description="Number of results (1-100)")

class BraveSearchTool(BaseTool):
    """Tool for performing web searches with Brave Search API."""
    
    name: str = "brave_search"
    description: str = "Search the web for current information and documentation"
    args_schema: Type[BaseModel] = BraveSearchInput
    
    def _run(self, query: str, num_results: int = 5) -> str:
        """Execute the search and return formatted results."""
        try:
            results = self._search(query, num_results)
            
            if not results.get('results'):
                return "No results found for your query."
            
            output = []
            for i, result in enumerate(results['results'], 1):
                output.append(f"{i}. {result['title']}\n   {result['url']}\n   {result['description']}\n")
            
            return "\n".join(output)
            
        except Exception as e:
            return f"Search error: {str(e)}"
    
    def _search(self, query: str, num_results: int) -> dict:
        """Internal search implementation."""
        # Implementation using subprocess or direct API call
        pass
```

### CrewAI Task Integration

```python
from crewai import Agent, Task, Tools
from your_module import BraveSearchTool

# Create search agent
research_agent = Agent(
    role='Web Research Specialist',
    goal='Find accurate, up-to-date information from the web',
    backstory='Expert at searching and verifying web information',
    verbose=True,
    tools=[BraveSearchTool()]
)

# Create research task
research_task = Task(
    description="""
    Search for the latest information about {topic}.
    Find official documentation, recent news, and community resources.
    Return a summary with links to the most relevant sources.
    """,
    agent=research_agent,
    expected_output="Summary of findings with source links"
)
```

### Shell Script Integration

```bash
#!/bin/bash
# Quick web search wrapper

QUERY="$1"
NUM_RESULTS="${2:-5}"

if [ -z "$QUERY" ]; then
    echo "Usage: $0 <query> [num_results]"
    exit 1
fi

# Search and extract URLs
python search.py "$QUERY" -n "$NUM_RESULTS" --json | \
    jq -r '.results[] | "\(.title): \(.url)"'
```

## Error Handling

### Common Errors and Solutions

#### 1. API Key Not Set
```
Error: BRAVE_API_KEY environment variable not set.
Get your free API key from: https://api-dashboard.search.brave.com/
Set it with: export BRAVE_API_KEY='your-api-key-here'
```

**Solution**: Set the environment variable before running the script.

#### 2. Request Timed Out
```
Error: Request timed out.
```

**Solution**: 
- Check internet connection
- Reduce number of results with `-n`
- Try again later

#### 3. Invalid API Key
```
Error: API returned status code 401
Details: Invalid API key
```

**Solution**: Verify your API key at the Brave dashboard and ensure no extra spaces.

#### 4. No Results Found
```
No results found.
```

**Solution**: 
- Try different search terms
- Increase result count with `-n`
- Check spelling and query format

### Robust Error Handling Pattern

```python
import subprocess
import json
from typing import Optional, Tuple

def safe_search(
    query: str, 
    num_results: int = 10,
    max_retries: int = 2
) -> Tuple[bool, Optional[dict], Optional[str]]:
    """
    Perform search with robust error handling.
    
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
                    return False, None, f"Search failed after {max_retries} attempts: {error_msg}"
                continue
            
            data = json.loads(result.stdout)
            
            # Check for API errors in response
            if data.get('error'):
                error_msg = data.get('error_message', 'Unknown error')
                if attempt == max_retries - 1:
                    return False, None, error_msg
                continue
            
            return True, data, None
            
        except subprocess.TimeoutExpired:
            if attempt == max_retries - 1:
                return False, None, "Search timed out"
            continue
        except json.JSONDecodeError:
            if attempt == max_retries - 1:
                return False, None, "Invalid JSON response"
            continue
        except Exception as e:
            if attempt == max_retries - 1:
                return False, None, f"Unexpected error: {str(e)}"
            continue
    
    return False, None, "Max retries exceeded"
```

## Best Practices

### For Coding Agents

1. **Always Use JSON Output**: When integrating programmatically, always use `--json` flag for reliable parsing.

2. **Validate Input**: Ensure queries don't contain special characters that could cause shell injection.

3. **Handle Rate Limits**: Respect API limits (2,000 queries/month free tier).

4. **Cache Results**: Store frequently searched queries to avoid redundant API calls.

5. **Timeout Protection**: Always set reasonable timeouts (30 seconds recommended).

6. **Error Recovery**: Implement retry logic for transient failures.

7. **Result Filtering**: Post-process results to filter irrelevant content.

### Query Optimization

#### Good Queries
```python
# Specific and focused
"Python 3.12 new features documentation"
"FastAPI dependency injection examples"
"React hooks useEffect best practices"

# With context
"machine learning frameworks 2026 comparison"
"Docker multi-stage build optimization"
```

#### Poor Queries
```python
# Too vague
"stuff about python"
"how to do things"
"programming stuff"

# Too long
"can you please search for me the best tutorials about how to learn python programming language step by step with examples and video courses"
```

## Performance Considerations

### Response Times
- **Simple queries**: ~1-2 seconds
- **Complex queries**: ~2-4 seconds
- **High result counts**: +1 second per 10 additional results

### Optimization Tips

1. **Minimize Result Count**: Only request what you need (default 10 is usually sufficient).

2. **Use Specific Queries**: More specific queries return better results faster.

3. **Batch Processing**: If searching multiple topics, consider batching requests.

4. **Parallel Execution**: For independent searches, run them in parallel (with rate limit awareness).

## Testing Your Setup

### Verification Script

```python
#!/usr/bin/env python3
"""Test script to verify Brave Search integration."""

import subprocess
import json
import sys

def test_brave_search():
    """Test basic search functionality."""
    print("Testing Brave Search integration...")
    
    # Test 1: Basic search
    print("\n1. Testing basic search...")
    cmd = ['python', 'search.py', 'python tutorial', '-n', '3', '--json']
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
        for i, result in enumerate(data['results'], 1):
            print(f"   {i}. {result['title']}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False

if __name__ == '__main__':
    success = test_brave_search()
    sys.exit(0 if success else 1)
```

## Additional Resources

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [API Dashboard](https://api-dashboard.search.brave.com/)
- [Example JSON Output Guide](./EXAMPLE_JSON_OUTPUT.md)
- [Feature Summary](./FEATURES_SUMMARY.md)

## Troubleshooting Checklist

- [ ] `BRAVE_API_KEY` environment variable is set
- [ ] Dependencies are installed (`pip install -r requirements.txt`)
- [ ] Virtual environment is activated
- [ ] Internet connection is working
- [ ] API key is valid (check dashboard)
- [ ] Query doesn't contain problematic characters
- [ ] Result count is within bounds (1-100)
- [ ] Timeout is set appropriately (30s recommended)

---

*Generated by brave-search skill on 2026-02-28*
