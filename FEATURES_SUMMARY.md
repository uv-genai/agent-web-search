# Brave Search Script - Complete Feature Summary

## Overview

A Python-based web search tool that uses the Brave Search API to perform privacy-focused searches with flexible output options for both humans and coding agents.

---

## 🎯 Core Features

### 1. **Command-Line Interface**
- Simple, intuitive arguments
- Support for multi-word queries with quotes
- Built-in help system

### 2. **Customizable Result Count**
```bash
python search.py "query" -n 5        # Get 5 results
python search.py "query" --num-results 20  # Get 20 results
```
- Default: 10 results
- Range: 1-100 results
- Validation included

### 3. **JSON Output Mode** (NEW!)
```bash
python search.py "query" --json
```
- Raw JSON for programmatic use
- Structured data with query, count, and results
- Error handling in JSON format
- Perfect for AI agents and automation

### 4. **Privacy-Focused**
- Uses Brave's independent search index
- No tracking or profiling
- Free tier: 2,000 queries/month

---

## 📦 Files Included

| File | Description | Size |
|------|-------------|------|
| `search.py` | Main script with all features | 6.5 KB |
| `brave_search_api.py` | Alternative API implementation | 4.3 KB |
| `brave_search_selenium.py` | Selenium-based (experimental) | 5.8 KB |
| `test_json_output.py` | Demo/test script | 3.6 KB |
| `README.md` | Complete documentation | 5.1 KB |
| `EXAMPLE_JSON_OUTPUT.md` | JSON usage examples | 5.2 KB |
| `requirements.txt` | Dependencies | 66 B |
| `venv/` | Virtual environment | ~53 MB |

---

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
cd /Users/ugo/tmp/ws
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Get API Key
Visit [https://api-dashboard.search.brave.com/](https://api-dashboard.search.brave.com/)
- Sign up for free
- Generate API key
- Copy your key

### Step 3: Set Environment Variable
```bash
export BRAVE_API_KEY="your-api-key-here"
```

### Step 4: Run Searches
```bash
# Human-readable output
python search.py "python web scraping" -n 5

# JSON output for coding agents
python search.py "machine learning" --json

# Combine options
python search.py "web development" -n 15 --json
```

---

## 💻 Usage Examples

### Basic Searches

```bash
# Default 10 results
python search.py "best python tutorials"

# Custom result count
python search.py "javascript frameworks 2026" -n 7

# With spaces in query
python search.py "how to learn machine learning" -n 5
```

### JSON for Automation

```bash
# Extract URLs only
python search.py "python" --json | jq '.results[].url'

# Count results
python search.py "query" --json | jq '.num_results_found'

# Filter by keyword
python search.py "python" --json | jq '.results[] | select(.description | contains("tutorial"))'
```

### Programmatic Integration

**Python:**
```python
import subprocess
import json

result = subprocess.run(
    ['python', 'search.py', 'query', '-n', '5', '--json'],
    capture_output=True, text=True
)
data = json.loads(result.stdout)
for item in data['results']:
    print(item['title'])
```

**Node.js:**
```javascript
const { execSync } = require('child_process');
const data = JSON.parse(execSync('python search.py "query" --json'));
console.log(data.results[0].title);
```

---

## 🔧 Command Line Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `query` | positional | required | Search query (use quotes for phrases) |
| `-n`, `--num-results` | integer | 10 | Number of results to display |
| `--json` | flag | false | Output as raw JSON |
| `-h`, `--help` | flag | - | Show help message |

---

## 📊 JSON Output Format

```json
{
  "query": "python web scraping",
  "num_results_requested": 5,
  "num_results_found": 47,
  "results": [
    {
      "title": "GeeksforGeeks",
      "url": "https://www.geeksforgeeks.org/python-web-scraping/",
      "description": "Learn Python web scraping...",
      "engine": "brave_search"
    }
  ]
}
```

### Fields Explained
- `query`: The original search query
- `num_results_requested`: How many results were asked for
- `num_results_found`: Total available results from API
- `results`: Array of result objects
  - `title`: Page title
  - `url`: Destination URL
  - `description`: Page description/snippet
  - `engine`: Source engine name

---

## ⚡ Performance

- **Speed**: Fast API-based responses (~1-3 seconds)
- **Reliability**: No browser automation issues
- **Scalability**: Handle hundreds of queries per hour
- **Free Tier**: 2,000 queries/month at no cost

---

## 🛠️ Integration Examples

### For AI Agents
- ✅ LangChain tools
- ✅ CrewAI tasks
- ✅ AutoGen agents
- ✅ Custom LLM workflows

### For Shell Scripts
```bash
#!/bin/bash
QUERY="$1"
URLS=$(python search.py "$QUERY" --json | jq -r '.results[].url')
while IFS= read -r url; do
    curl -sI "$url" | head -1
done <<< "$URLS"
```

### For Web Applications
- REST API wrapper
- Background job processor
- Content aggregation

---

## 🎓 Use Cases

1. **Research & Development**
   - Quick information gathering
   - Competitor analysis
   - Market research

2. **Content Creation**
   - Source verification
   - Topic exploration
   - Citation finding

3. **Development Tools**
   - Documentation lookup
   - Stack Overflow searching
   - Library discovery

4. **AI Training**
   - Data collection
   - Knowledge retrieval
   - Context building

---

## 🔒 Privacy & Security

- ✅ No personal data collection
- ✅ Independent search index
- ✅ No tracking cookies
- ✅ Encrypted API communications
- ✅ Local processing only

---

## 📝 License

MIT License - Free to use, modify, and distribute.

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📞 Support

For issues or questions:
1. Check `README.md` for setup instructions
2. Review `EXAMPLE_JSON_OUTPUT.md` for usage examples
3. Run `python search.py --help` for command options

---

## 🎉 What's New

**Version 1.0** (Current)
- ✅ Brave Search API integration
- ✅ Customizable result count (`-n` flag)
- ✅ JSON output mode (`--json` flag)
- ✅ Comprehensive error handling
- ✅ Multiple implementation options
- ✅ Full documentation

**Planned Features:**
- [ ] Caching mechanism
- [ ] Result filtering options
- [ ] Multi-engine support
- [ ] GUI interface
- [ ] Batch search capability

---

**Happy Searching! 🚀**
