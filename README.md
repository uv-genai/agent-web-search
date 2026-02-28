# Brave Search Script

A Python script that performs Brave Search queries from the command line and prints results to stdout.

## Features

- ✅ **Command-line interface** with easy-to-use arguments
- ✅ **Customizable result count** using `-n` or `--num-results` flag
- ✅ **JSON output mode** for coding agents using `--json` flag
- ✅ **Brave Search API** integration for reliable, fast results
- ✅ **Privacy-focused** - uses Brave's independent search index
- ✅ **Clean output** - formatted titles, URLs, and descriptions

## Installation

1. **Create virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get a Brave Search API key**:
   - Visit [https://api-dashboard.search.brave.com/](https://api-dashboard.search.brave.com/)
   - Sign up for a free account
   - Generate an API key (free tier includes 2,000 queries/month)

4. **Set your API key as an environment variable**:
   ```bash
   export BRAVE_API_KEY="your-api-key-here"
   ```
   
   Or add it to your `.bashrc` or `.zshrc`:
   ```bash
   echo 'export BRAVE_API_KEY="your-api-key-here"' >> ~/.bashrc
   source ~/.bashrc
   ```

## Usage

### Basic Usage
```bash
python search.py "your search query"
```

### Specify Number of Results
```bash
python search.py "python web scraping" -n 5
python search.py "machine learning tutorials" --num-results 20
```

### JSON Output for Coding Agents
```bash
# Get raw JSON output
python search.py "python web scraping" --json

# Combine with result count
python search.py "machine learning" -n 10 --json

# Pipe to jq for processing
python search.py "query" --json | jq '.results[].url'
```

### Examples
```bash
# Get 5 results about Python programming
python search.py "python programming" -n 5

# Get 15 results about web development (human-readable)
python search.py "web development frameworks 2026" --num-results 15

# Get JSON output for programmatic use
python search.py "best coding practices" --json

# Default (10 results, human-readable)
python search.py "best coding practices"
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `query` | Search query (required) | - |
| `-n`, `--num-results` | Number of results to display | 10 |
| `--json` | Output as raw JSON for coding agents | False |
| `-h`, `--help` | Show help message | - |

## JSON Output Format

When using `--json`, the output is structured as follows:

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
    ...
  ]
}
```

### Programmatic Usage Examples

**Python:**
```python
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
```

**Shell (with jq):**
```bash
# Extract all URLs
python search.py "query" --json | jq '.results[].url'

# Extract titles
python search.py "query" --json | jq '.results[].title'

# Count results
python search.py "query" --json | jq '.num_results_found'
```

**Node.js:**
```javascript
const { execSync } = require('child_process');
const data = JSON.parse(execSync('python search.py "query" --json'));
console.log(data.results[0].title);
```

## Output Format

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

## Requirements

- Python 3.7+
- requests library
- Brave Search API key (free tier available)

## Files

- `search.py` - Main search script
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment (created during setup)
- `brave_search_api.py` - Alternative implementation (API-based)
- `brave_search_selenium.py` - Selenium-based implementation (experimental)

## Troubleshooting

### "BRAVE_API_KEY environment variable not set"
Make sure you've exported the API key in your terminal session.

### "Request timed out"
Check your internet connection or try again later.

### "API returned status code 401"
Your API key is invalid or expired. Get a new one from the Brave dashboard.

## License

MIT License - Feel free to use and modify as needed.
