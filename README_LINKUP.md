# Linkup Search Script

**Version:** 1.0.0  
**Last Updated:** 2026-02-28  
**License:** MIT

A Python script that performs agentic web searches and fetches web pages using the Linkup API.

---

## 📋 Overview

Linkup is a web search engine specifically designed for AI applications, providing grounded data to enrich AI outputs with factual information. This script provides both search and fetch capabilities using Linkup's powerful API.

### Key Features

- ✅ **Search Mode**: Agentic search with multiple output types
- ✅ **Fetch Mode**: Extract content from specific URLs
- ✅ **Customizable depth**: Standard (fast) or Deep (comprehensive) search
- ✅ **Multiple output formats**: searchResults, sourcedAnswer, structured
- ✅ **Date filtering**: Filter results by date range
- ✅ **Domain filtering**: Include/exclude specific domains
- ✅ **JSON output mode**: For coding agents and automation
- ✅ **JavaScript rendering**: Capture dynamic content
- ✅ **Markdown extraction**: Clean content formatting

---

## 🚀 Installation

### 1. Create Virtual Environment

```bash
cd /Users/ugo/tmp/ws
python3 -m venv venv_linkup
source venv_linkup/bin/activate  # On Windows: venv_linkup\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements_linkup.txt
```

### 3. Get Linkup API Key

- Visit [https://app.linkup.so/](https://app.linkup.so/)
- Sign up for a free account
- Generate your API key in the dashboard
- Free tier available (check pricing page)

### 4. Set Environment Variable

```bash
export LINKUP_API_KEY="your-api-key-here"
```

Or add to your `.bashrc` or `.zshrc`:

```bash
echo 'export LINKUP_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

---

## 💻 Usage

### Search Mode

#### Basic Search

```bash
python linkup_search.py search "python web scraping tutorials"
```

#### Specify Number of Results

```bash
python linkup_search.py search "machine learning" -n 15
```

#### Deep Search (Comprehensive Research)

```bash
python linkup_search.py search "quantum computing advances 2026" --depth deep
```

#### Date Filtering

```bash
python linkup_search.py search "AI news" --from-date 2026-01-01 --to-date 2026-02-28
```

#### Domain Filtering

```bash
# Only search specific domains
python linkup_search.py search "python documentation" --include-domains python.org realpython.com geeksforgeeks.org

# Exclude specific domains
python linkup_search.py search "web scraping" --exclude-domains medium.com reddit.com
```

#### Sourced Answer (Natural Language Response)

```bash
python linkup_search.py search "What is machine learning?" --output-type sourcedAnswer
```

#### JSON Output for Coding Agents

```bash
# Search with JSON output
python linkup_search.py search "python tutorials" -n 10 --json

# Deep search with JSON
python linkup_search.py search "advanced AI techniques" --depth deep --json
```

### Fetch Mode

#### Basic Fetch

```bash
python linkup_search.py fetch "https://example.com/article"
```

#### Fetch as Markdown

```bash
python linkup_search.py fetch "https://docs.python.org" --output-format markdown
```

#### Fetch with JavaScript Rendering

```bash
# For pages that require JS execution
python linkup_search.py fetch "https://example.com/dynamic-page" --render-js
```

#### Fetch with JSON Output

```bash
python linkup_search.py fetch "https://example.com" --json
```

---

## 🔧 Command Line Options

### Search Subcommand

| Option | Description | Default |
|--------|-------------|---------|
| `query` | Search query (required) | - |
| `-n`, `--num-results` | Number of results (1-100) | 10 |
| `--depth` | Search depth: standard or deep | standard |
| `--output-type` | Output type: searchResults, sourcedAnswer, structured | searchResults |
| `--from-date` | Filter from date (YYYY-MM-DD) | None |
| `--to-date` | Filter to date (YYYY-MM-DD) | None |
| `--include-domains` | Restrict to specific domains | None |
| `--exclude-domains` | Exclude specific domains | None |
| `--json` | Output as raw JSON | False |

### Fetch Subcommand

| Option | Description | Default |
|--------|-------------|---------|
| `url` | URL to fetch (required) | - |
| `--output-format` | Format: html or markdown | markdown |
| `--render-js` | Execute JavaScript | False |
| `--json` | Output as raw JSON | False |

---

## 📊 Search Output Formats

### 1. searchResults (Default)

Returns an array of sources with name, URL, and content snippets:

```json
{
  "mode": "search",
  "query": "python tutorials",
  "parameters": {
    "num_results_requested": 10,
    "depth": "standard",
    "output_type": "searchResults"
  },
  "results": [
    {
      "name": "Real Python",
      "url": "https://realpython.com",
      "content": "Python tutorials and resources...",
      "type": "source"
    }
  ],
  "total_found": 47,
  "error": false
}
```

### 2. sourcedAnswer

Returns a natural language answer with cited sources:

```json
{
  "mode": "search",
  "query": "What is Python?",
  "answer": "Python is a high-level programming language...",
  "sources": [
    {
      "name": "Python.org",
      "url": "https://python.org",
      "content": "Official Python documentation..."
    }
  ],
  "error": false
}
```

### 3. structured

Returns data following your custom schema:

```bash
# Requires structuredOutputSchema parameter (not yet implemented in CLI)
python linkup_search.py search "products" --output-type structured --structured-output-schema '{"products": [{"name": string, "price": number}]}'
```

---

## 🤖 Integration Examples

### Python Integration

```python
import subprocess
import json

def linkup_search(query, num_results=10):
    """Perform a Linkup search and return results."""
    cmd = [
        'python', 'linkup_search.py', 'search',
        query, '-n', str(num_results), '--json'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def linkup_fetch(url):
    """Fetch a URL and return content."""
    cmd = ['python', 'linkup_search.py', 'fetch', url, '--json']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

# Usage
results = linkup_search("machine learning tutorials", 5)
for item in results['results']:
    print(f"{item['name']}: {item['url']}")

page = linkup_fetch("https://example.com")
print(page['content'])
```

### Shell Integration

```bash
# Extract all URLs from search results
python linkup_search.py search "python docs" --json | jq '.results[].url'

# Count total results found
python linkup_search.py search "query" --json | jq '.total_found'

# Fetch and save content
python linkup_search.py fetch "https://example.com" > page.md

# Search and fetch first result
FIRST_URL=$(python linkup_search.py search "topic" --json | jq -r '.results[0].url')
python linkup_search.py fetch "$FIRST_URL"
```

### Node.js Integration

```javascript
const { execSync } = require('child_process');

function linkupSearch(query, numResults = 10) {
    const cmd = `python linkup_search.py search "${query}" -n ${numResults} --json`;
    return JSON.parse(execSync(cmd));
}

function linkupFetch(url) {
    const cmd = `python linkup_search.py fetch "${url}" --json`;
    return JSON.parse(execSync(cmd));
}

// Usage
const results = linkupSearch("web development", 5);
console.log(results.results.map(r => r.name));
```

---

## 🔒 API Parameters Explained

### Search Depth

- **`standard`**: Fast, basic search results (~1-2 seconds)
- **`deep`**: Thorough multi-step research (~5-10 seconds)

### Output Types

- **`searchResults`**: Array of sources with snippets (best for citations)
- **`sourcedAnswer`**: Natural language answer with references (best for Q&A)
- **`structured`**: Custom JSON schema (best for data extraction)

### Date Filtering

Use ISO 8601 format (`YYYY-MM-DD`):

```bash
--from-date 2026-01-01
--to-date 2026-02-28
```

### Domain Limits

- Maximum 100 domains in `includeDomains`
- No limit on `excludeDomains`

---

## ⚡ Performance Tips

1. **Use `standard` depth** for quick lookups
2. **Use `deep` depth** for complex research questions
3. **Filter by date** to get recent information
4. **Use domain filters** to focus on trusted sources
5. **Cache results** to avoid redundant API calls
6. **Use `sourcedAnswer`** for direct answers without parsing

---

## 🛠️ Troubleshooting

### "LINKUP_API_KEY environment variable not set"

Make sure you've exported the API key:

```bash
export LINKUP_API_KEY="your-key"
# Or check .bashrc/.zshrc
grep LINKUP_API_KEY ~/.bashrc
```

### "Request timed out"

- Try reducing `--num-results`
- Use `--depth standard` instead of `deep`
- Check internet connection

### "Invalid API key"

- Verify your API key at [https://app.linkup.so/](https://app.linkup.so/)
- Ensure no extra spaces or characters
- Check if your account is active

### "No results found"

- Try rephrasing your query
- Remove date filters if too restrictive
- Increase `--num-results`

---

## 📚 Additional Resources

- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [Linkup Playground](https://app.linkup.so/playground) - Test queries interactively
- [Prompt Optimizer](https://prompt.linkup.so) - Optimize your search prompts
- [Linkup Blog](https://www.linkup.so/blog) - Latest updates and use cases

---

## 🎯 Use Cases

### AI Agent Grounding
Provide factual context to LLMs with cited sources

### Content Research
Gather information from multiple sources efficiently

### Fact-Checking
Verify claims with current, sourced information

### Competitive Analysis
Monitor specific domains for updates

### Academic Research
Find recent papers and studies with date filtering

### Development
Search documentation and technical resources

---

## 📄 License

MIT License - Feel free to use and modify as needed.

---

*This script mirrors the functionality of `search.py` but uses Linkup's superior agentic search capabilities.*
