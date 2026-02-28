# Web Search Scripts - Complete Toolkit

**Version:** 2.0.0  
**Last Updated:** 2026-02-28  
**License:** MIT

A comprehensive Python-based web search toolkit providing two powerful search tools for different use cases: Brave Search for privacy-focused searches and Linkup Search for AI-specific agentic research with superior factuality.

---

## 📚 Available Scripts

### 🔹 Brave Search (`search.py`)
Privacy-focused search using Brave's independent index.

**Best for:** Privacy-conscious searches, simple queries, fast results, no budget constraints.

**Key Features:**
- ✅ Independent search index (no tracking)
- ✅ Free tier: 2,000 queries/month
- ✅ Fast responses (~1-3 seconds)
- ✅ Simple, straightforward queries
- ✅ Basic citation needs

[Read Brave Search Documentation](./FEATURES_SUMMARY.md) | [View Script](./search.py)

### 🔹 Linkup Search (`linkup_search.py`)
AI-specific agentic search with superior factuality (#1 on SimpleQA benchmark).

**Best for:** AI applications, complex research, factual accuracy, content extraction.

**Key Features:**
- ✅ Agentic search with deep research capability
- ✅ Superior factuality (SOTA performance)
- ✅ Multiple output types (searchResults, sourcedAnswer, structured)
- ✅ Built-in content fetching (/fetch endpoint)
- ✅ JavaScript rendering support
- ✅ Advanced filtering (dates, domains)
- ✅ Markdown extraction

[Read Linkup Search Documentation](./README_LINKUP.md) | [View Script](./linkup_search.py)

---

## 🆚 Feature Comparison

| Feature | Brave Search | Linkup Search |
|---------|-------------|---------------|
| **Search Mode** | ✅ Yes | ✅ Yes |
| **Content Fetching** | ❌ No | ✅ Yes |
| **Output Types** | Basic | 3 types |
| **Deep Research** | ❌ No | ✅ Yes |
| **Date Filtering** | ✅ Yes | ✅ Yes |
| **Domain Filtering** | ✅ Yes | ✅ Yes |
| **JavaScript Render** | ❌ No | ✅ Yes |
| **Markdown Output** | ❌ No | ✅ Yes |
| **Factuality** | Good | ⭐ SOTA |
| **Free Tier** | 2,000/mo | Available |
| **Speed** | Fast | Fast/Deep |

---

## 🎯 When to Use Each

### Choose Brave Search When:
- Privacy is the primary concern
- Queries are straightforward
- Need fast, basic results
- No budget for API calls
- Simple citation needs

### Choose Linkup Search When:
- Building AI applications
- Need highly factual responses
- Complex research questions
- Want natural language answers
- Need to fetch webpage content
- Require structured data extraction

---

## 🚀 Quick Start

### Setup Both Scripts

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies for both scripts
pip install -r requirements.txt
pip install -r requirements_linkup.txt

# 3. Get API keys
export BRAVE_API_KEY="your-brave-api-key-here"
export LINKUP_API_KEY="your-linkup-api-key-here"
```

### Brave Search Usage

```bash
# Basic search
python search.py "python web scraping" -n 5

# JSON output
python search.py "machine learning" --json

# With specific count
python search.py "web development" -n 10 --json
```

### Linkup Search Usage

```bash
# Basic search
python linkup_search.py search "open source licenses" -n 5

# Deep research
python linkup_search.py search "AI trends 2026" --depth deep -n 10

# JSON output
python linkup_search.py search "python tutorials" -n 5 --json

# Fetch webpage content
python linkup_search.py fetch "https://docs.python.org"

# With filters
python linkup_search.py search "machine learning" \
  --from-date 2026-01-01 \
  --include-domains arxiv.org \
  -n 10
```

---

## 📋 Installation

### Prerequisites
- Python 3.7+
- pip package manager
- Git (optional, for version control)

### Step 1: Clone or Navigate to Project
```bash
cd /Users/ugo/tmp/ws
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install Brave Search dependencies
pip install -r requirements.txt

# Install Linkup Search dependencies
pip install -r requirements_linkup.txt
```

### Step 4: Configure API Keys

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

---

## 💻 Usage Guide

### Brave Search Commands

#### Basic Search
```bash
python search.py "your search query"
```

#### Specify Number of Results
```bash
python search.py "python web scraping" -n 5
python search.py "machine learning tutorials" --num-results 20
```

#### JSON Output for Coding Agents
```bash
# Get raw JSON output
python search.py "python web scraping" --json

# Combine with result count
python search.py "machine learning" -n 10 --json

# Pipe to jq for processing
python search.py "query" --json | jq '.results[].url'
```

#### Examples
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

### Linkup Search Commands

#### Search Mode
```bash
# Basic search
python linkup_search.py search "open source licenses" -n 5

# Deep research
python linkup_search.py search "AI trends 2026" --depth deep -n 10

# Different output types
python linkup_search.py search "what is machine learning" --output-type sourcedAnswer

# With date filtering
python linkup_search.py search "python updates" --from-date 2026-01-01 --to-date 2026-02-28

# With domain filtering
python linkup_search.py search "python tutorials" --include-domains python.org realpython.com

# JSON output
python linkup_search.py search "query" -n 5 --json
```

#### Fetch Mode
```bash
# Fetch webpage in markdown format
python linkup_search.py fetch "https://docs.python.org"

# Fetch with HTML output
python linkup_search.py fetch "https://example.com" --output-format html

# Fetch with JavaScript rendering
python linkup_search.py fetch "https://dynamic-site.com" --render-js

# JSON output
python linkup_search.py fetch "https://example.com" --json
```

---

## 📊 Command Line Options

### Brave Search Options

| Option | Description | Default |
|--------|-------------|---------|
| `query` | Search query (required) | - |
| `-n`, `--num-results` | Number of results to display | 10 |
| `--json` | Output as raw JSON for coding agents | False |
| `-h`, `--help` | Show help message | - |

### Linkup Search Options

#### Search Mode
| Option | Description | Default |
|--------|-------------|---------|
| `query` | Search query (required) | - |
| `-n`, `--num-results` | Number of results to display | 10 |
| `--depth` | Search depth: standard or deep | standard |
| `--output-type` | Output type: searchResults, sourcedAnswer, structured | searchResults |
| `--from-date` | Filter from date (YYYY-MM-DD) | None |
| `--to-date` | Filter to date (YYYY-MM-DD) | None |
| `--include-domains` | Restrict to specific domains | None |
| `--exclude-domains` | Exclude specific domains | None |
| `--json` | Output as raw JSON | False |

#### Fetch Mode
| Option | Description | Default |
|--------|-------------|---------|
| `url` | URL to fetch (required) | - |
| `--output-format` | Output format: html or markdown | markdown |
| `--render-js` | Execute JavaScript | False |
| `--json` | Output as raw JSON | False |

---

## 📝 Output Formats

### Human-Readable Output

#### Brave Search Example
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

#### Linkup Search Example
```
============================================================
Linkup Search Results for: open source licenses
Depth: standard, Output Type: searchResults
Showing up to 5 results
============================================================

1. Licenses - Open Source Initiative
   URL: https://opensource.org/licenses
   Content: OSI Approved Licenses Open source licenses are licenses that comply with the Open Source Definition...

2. Open source licenses grant permission for anybody to use, ...
   URL: https://choosealicense.com/licenses/
   Content: Open source licenses grant permission for anybody to use, modify, and share licensed software...

Total results displayed: 5
```

### JSON Output Format

#### Brave Search JSON
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
    }
  ]
}
```

#### Linkup Search JSON
```json
{
  "mode": "search",
  "query": "python tutorials",
  "parameters": {
    "num_results_requested": 3,
    "depth": "standard",
    "output_type": "searchResults"
  },
  "results": [
    {
      "name": "Python Tutorial",
      "url": "https://www.w3schools.com/python/",
      "content": "With our \"Try it Yourself\" editor...",
      "type": "source"
    }
  ],
  "error": false,
  "total_found": 3
}
```

---

## 💡 Programmatic Usage Examples

### Python Integration

#### Brave Search
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

#### Linkup Search
```python
import subprocess
import json

# Search
result = subprocess.run(
    ['python', 'linkup_search.py', 'search', 'machine learning', '--depth', 'deep', '--json'],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)
for item in data['results']:
    print(f"{item['name']}: {item['url']}")

# Fetch
result = subprocess.run(
    ['python', 'linkup_search.py', 'fetch', 'https://docs.python.org', '--json'],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)
print(data['content'])
```

### Shell Integration (with jq)

```bash
# Extract all URLs from Brave Search
python search.py "query" --json | jq '.results[].url'

# Extract titles from Linkup Search
python linkup_search.py search "query" --json | jq '.results[].name'

# Count results
python search.py "query" --json | jq '.num_results_found'

# Filter by domain
python linkup_search.py search "python" --include-domains python.org --json | jq '.results[]'
```

### Node.js Integration

```javascript
const { execSync } = require('child_process');

// Brave Search
const braveData = JSON.parse(execSync('python search.py "query" --json'));
console.log(braveData.results[0].title);

// Linkup Search
const linkupData = JSON.parse(execSync('python linkup_search.py search "query" --json'));
console.log(linkupData.results[0].name);
```

---

## 🛠️ Troubleshooting

### Common Issues

#### "API key not set"
```bash
# Check if key is set
echo $BRAVE_API_KEY
echo $LINKUP_API_KEY

# Set the key
export BRAVE_API_KEY="your-key"
export LINKUP_API_KEY="your-key"
```

#### "Request timed out"
- Reduce number of results with `-n`
- Use `--depth standard` instead of `deep`
- Check internet connection

#### "Invalid API key"
- Verify key at dashboard
- Ensure no extra spaces
- Check account status

#### "No results found"
- Try different query
- Increase result count
- Check API credits
- Verify internet connection

### Specific Fixes

#### Linkup Search Returning No Results
This was fixed in version 2.0.0! The script now correctly parses the API response using the `'results'` key instead of `'sources'`.

If you still experience issues:
1. Run the diagnostic tool: `python test_linkup_api.py`
2. Check your API key is valid
3. Try a simpler query like `"python tutorial"`
4. Verify you have API credits available

---

## 📁 File Structure

```
ws/
├── search.py                 # Brave Search main script
├── linkup_search.py          # Linkup Search main script
├── requirements.txt          # Brave Search dependencies
├── requirements_linkup.txt   # Linkup Search dependencies
├── README.md                 # Main documentation (this file)
├── README_LINKUP.md          # Linkup detailed docs
├── AGENTS.md                 # Project documentation
├── FEATURES_SUMMARY.md       # Brave Search features
├── FEATURES_LINKUP.md        # Linkup Search features
├── PROJECT_SUMMARY.md        # Project overview
├── EXAMPLE_JSON_OUTPUT.md    # JSON usage examples
├── FIX_APPLIED.md            # Bug fix documentation
├── LINKUP_FIXES.md           # Linkup fixes documentation
├── test_json_output.py       # Brave Search test script
├── test_linkup.py            # Linkup Search test script
├── test_linkup_api.py        # Linkup diagnostic tool
├── .gitignore                # Git ignore rules
└── venv/                     # Virtual environment
```

---

## 📈 Performance Metrics

| Metric | Brave Search | Linkup Search |
|--------|-------------|---------------|
| Response Time (standard) | ~1-3s | ~1-3s |
| Response Time (deep) | N/A | ~5-10s |
| Factuality Score | Good | SOTA (#1) |
| Citation Quality | Good | Excellent |
| Complex Query Handling | Moderate | Excellent |
| Content Extraction | None | Full page fetch |

---

## 🎓 Use Cases

### AI Chatbots
Provide grounded, factual responses with citations

### Research Assistants
Gather comprehensive information on complex topics

### Content Aggregation
Fetch and process multiple web pages efficiently

### Competitive Analysis
Monitor specific domains for updates

### Fact-Checking
Verify claims with current, sourced information

### Development Tools
Search documentation and technical resources

---

## 🤝 Contributing

Contributions welcome! Please feel free to:
- Report bugs via issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

MIT License - Feel free to use and modify as needed.

---

## 📚 Additional Resources

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [Brave Search Features](./FEATURES_SUMMARY.md)
- [Linkup Search Features](./FEATURES_LINKUP.md)
- [Project Overview](./PROJECT_SUMMARY.md)
- [Bug Fix Documentation](./FIX_APPLIED.md)

---

*Generated by version-commit-tag skill on 2026-02-28*
