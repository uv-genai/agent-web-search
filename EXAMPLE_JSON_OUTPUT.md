# Example JSON Output

This document shows examples of the raw JSON output when using the `--json` flag.

## Basic JSON Output

```bash
python search.py "python web scraping" -n 3 --json
```

**Output:**
```json
{
  "query": "python web scraping",
  "num_results_requested": 3,
  "num_results_found": 47,
  "results": [
    {
      "title": "Top Python Web Scraping Libraries 2026",
      "url": "https://www.capsolver.com/blog/web-scraping/best-python-web-scraping-libraries",
      "description": "Discover the best Python libraries for web scraping in 2026 including BeautifulSoup, Scrapy, Selenium, and more.",
      "engine": "brave_search"
    },
    {
      "title": "7 Best Python Web Scraping Libraries in 2026",
      "url": "https://www.zenrows.com/blog/python-web-scraping-library",
      "description": "A comprehensive guide to Python web scraping libraries with code examples and use cases.",
      "engine": "brave_search"
    },
    {
      "title": "Beautiful Soup: Build a Web Scraper With Python",
      "url": "https://realpython.com/beautiful-soup-web-scraper-python/",
      "description": "Learn how to build a web scraper using Beautiful Soup, one of the most popular Python libraries.",
      "engine": "brave_search"
    }
  ]
}
```

## Processing JSON with jq (Shell)

### Extract all URLs
```bash
python search.py "machine learning" --json | jq '.results[].url'
```

**Output:**
```
"https://www.datacamp.com/blog/how-to-learn-ai"
"https://medium.com/@soyoungpark.psy/start-learning-ai-in-2026"
"https://www.coursera.org/resources/ml-learning-roadmap"
```

### Extract titles only
```bash
python search.py "python tutorials" --json | jq '.results[].title'
```

**Output:**
```
"Python Tutorial - W3Schools"
"Python.org - Official Site"
"Real Python Tutorials"
```

### Count results
```bash
python search.py "web development" --json | jq '.num_results_found'
```

**Output:**
```
156
```

### Filter by description keyword
```bash
python search.py "python" --json | jq '.results[] | select(.description | contains("tutorial"))'
```

### Get first result URL
```bash
python search.py "query" --json | jq -r '.results[0].url'
```

## Programmatic Usage Examples

### Python Script
```python
#!/usr/bin/env python3
import subprocess
import json

def search_web(query, num_results=5):
    """Search the web and return results as Python objects."""
    cmd = [
        'python', 'search.py',
        query,
        '-n', str(num_results),
        '--json'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    
    return data['results']

# Usage
results = search_web("python web scraping", 10)
for item in results:
    print(f"{item['title']}")
    print(f"  → {item['url']}")
    if item['description']:
        print(f"  {item['description'][:100]}...")
    print()
```

### Node.js Script
```javascript
const { execSync } = require('child_process');

function searchWeb(query, numResults = 5) {
    const cmd = `python search.py "${query}" -n ${numResults} --json`;
    const output = execSync(cmd);
    return JSON.parse(output);
}

// Usage
const data = searchWeb("machine learning", 10);
data.results.forEach(item => {
    console.log(`${item.title}\n${item.url}\n`);
});
```

### Bash Script
```bash
#!/bin/bash

QUERY="$1"
NUM_RESULTS="${2:-10}"

# Search and extract URLs
URLS=$(python search.py "$QUERY" -n "$NUM_RESULTS" --json | jq -r '.results[].url')

# Process each URL
while IFS= read -r url; do
    echo "Visiting: $url"
    # Add your processing here
done <<< "$URLS"
```

## Error Handling in JSON Mode

If there's an error, the JSON output will include an error object:

```json
{
  "error": true,
  "query": "test query",
  "status_code": 401,
  "message": "Invalid API key"
}
```

Or for timeout errors:
```json
{
  "error": true,
  "query": "test query",
  "message": "Request timed out"
}
```

## Integration with AI Agents

### For LangChain
```python
from langchain.tools import BaseTool
import subprocess
import json

class BraveSearchTool(BaseTool):
    name = "brave_search"
    description = "Search the web using Brave Search"
    
    def _run(self, query: str, num_results: int = 5):
        cmd = ['python', 'search.py', query, '-n', str(num_results), '--json']
        result = subprocess.run(cmd, capture_output=True, text=True)
        data = json.loads(result.stdout)
        
        return "\n".join([
            f"{i+1}. {r['title']}\n   {r['url']}"
            for i, r in enumerate(data['results'])
        ])
```

### For CrewAI
```python
from crewai import Tool

brave_search_tool = Tool(
    name='Brave Search',
    description='Search the web for current information',
    func=lambda query: subprocess.run(
        ['python', 'search.py', query, '--json'],
        capture_output=True, text=True
    ).stdout
)
```

## Tips for Coding Agents

1. **Always parse JSON**: Use `--json` flag for machine-readable output
2. **Handle errors**: Check for `"error": true` in the response
3. **Limit results**: Use `-n` to control output size
4. **Pipe to tools**: Combine with `jq`, `grep`, or other CLI tools
5. **Cache results**: Store frequently searched queries to reduce API calls
