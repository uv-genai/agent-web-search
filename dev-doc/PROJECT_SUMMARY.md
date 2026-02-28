# Web Search Scripts - Project Summary

**Version:** 1.0.0  
**Last Updated:** 2026-02-28  
**Author:** Ugo (ugovaretto@gmail.com)

---

## 📦 Project Overview

This project provides two powerful Python-based web search scripts:

1. **Brave Search Script** (`search.py`) - Privacy-focused search using Brave's independent index
2. **Linkup Search Script** (`linkup_search.py`) - AI-specific agentic search with superior factuality

Both scripts offer command-line interfaces, customizable result counts, and JSON output modes for coding agents.

---

## 🎯 Available Scripts

### 1. Brave Search (`search.py`)

**Best For:** Privacy-conscious searches, simple queries, no API cost

**Features:**
- ✅ Brave's independent search index (no tracking)
- ✅ Customizable result count (1-100)
- ✅ JSON output for automation
- ✅ Free tier: 2,000 queries/month
- ✅ Fast responses (~1-3 seconds)

**Usage:**
```bash
python search.py "query" -n 5                    # Human-readable
python search.py "query" --json                  # JSON output
python search.py "query" -n 10 --json            # Both options
```

**Documentation:** [README.md](./README.md)

---

### 2. Linkup Search (`linkup_search.py`)

**Best For:** AI applications, complex research, factual accuracy

**Features:**
- ✅ Agentic search with deep research capability
- ✅ Superior factuality (#1 on SimpleQA benchmark)
- ✅ Multiple output types (searchResults, sourcedAnswer, structured)
- ✅ Built-in content fetching (/fetch endpoint)
- ✅ JavaScript rendering support
- ✅ Date and domain filtering
- ✅ Markdown extraction

**Usage:**
```bash
# Search mode
python linkup_search.py search "query" -n 5
python linkup_search.py search "query" --depth deep
python linkup_search.py search "query" --output-type sourcedAnswer
python linkup_search.py search "query" --json

# Fetch mode
python linkup_search.py fetch "https://example.com"
python linkup_search.py fetch "https://example.com" --render-js
python linkup_search.py fetch "https://example.com" --json
```

**Documentation:** [README_LINKUP.md](./README_LINKUP.md)

---

## 📁 File Structure

```
ws/
├── search.py                 # Brave Search main script
├── linkup_search.py          # Linkup Search main script
├── requirements.txt          # Brave Search dependencies
├── requirements_linkup.txt   # Linkup Search dependencies
├── README.md                 # Main documentation (both scripts)
├── README_LINKUP.md          # Linkup Search detailed docs
├── AGENTS.md                 # Project documentation
├── FEATURES_SUMMARY.md       # Brave Search features
├── FEATURES_LINKUP.md        # Linkup Search features
├── EXAMPLE_JSON_OUTPUT.md    # JSON usage examples
├── test_json_output.py       # Brave Search test script
├── test_linkup.py            # Linkup Search test script
├── .gitignore                # Git ignore rules
├── PROJECT_SUMMARY.md        # This file
└── venv/                     # Virtual environment
```

---

## 🔑 API Keys Required

### Brave Search
- **Get from:** https://api-dashboard.search.brave.com/
- **Free tier:** 2,000 queries/month
- **Set as:** `export BRAVE_API_KEY="your-key"`

### Linkup Search
- **Get from:** https://app.linkup.so/
- **Free tier:** Check pricing page
- **Set as:** `export LINKUP_API_KEY="your-key"`

---

## 🚀 Quick Start Guide

### Setup Brave Search

```bash
cd /Users/ugo/tmp/ws

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get API key and set it
export BRAVE_API_KEY="your-api-key-here"

# Test the script
python search.py "python tutorials" -n 5
```

### Setup Linkup Search

```bash
cd /Users/ugo/tmp/ws

# Create virtual environment
python3 -m venv venv_linkup
source venv_linkup/bin/activate

# Install dependencies
pip install -r requirements_linkup.txt

# Get API key and set it
export LINKUP_API_KEY="your-api-key-here"

# Test the script
python linkup_search.py search "machine learning" --depth deep -n 5
python linkup_search.py fetch "https://docs.python.org"
```

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
| **API Cost** | Free tier | Free tier |
| **Speed** | Fast | Fast/Deep |

---

## 🤖 Integration Examples

### Python Integration

```python
import subprocess
import json

# Brave Search
def brave_search(query, num_results=10):
    cmd = ['python', 'search.py', query, '-n', str(num_results), '--json']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

# Linkup Search
def linkup_search(query, depth='standard'):
    cmd = ['python', 'linkup_search.py', 'search', query, '--depth', depth, '--json']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

# Linkup Fetch
def linkup_fetch(url):
    cmd = ['python', 'linkup_search.py', 'fetch', url, '--json']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)
```

### Shell Integration

```bash
# Extract URLs from Brave Search
python search.py "query" --json | jq '.results[].url'

# Fetch and save content with Linkup
python linkup_search.py fetch "https://example.com" > page.md

# Search and process results
python linkup_search.py search "topic" --json | jq '.results[] | select(.name | contains("Python"))'
```

---

## 📊 When to Use Each

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
- Building chatbots or agents

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
# OR
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

---

## 📈 Performance Metrics

### Brave Search
- Response Time: ~1-3 seconds
- Accuracy: Good
- Privacy: Excellent
- Cost: Free (2,000/mo)

### Linkup Search
- Standard Depth: ~1-3 seconds
- Deep Depth: ~5-10 seconds
- Factuality: ⭐ State-of-the-art
- Cost: Free tier available

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

## 📝 Changelog

### Version 1.0.0 (2026-02-28)

**Initial Release**

#### Brave Search Script
- ✅ Brave Search API integration
- ✅ Command-line interface
- ✅ Customizable result count
- ✅ JSON output mode
- ✅ Comprehensive error handling

#### Linkup Search Script
- ✅ Linkup API integration
- ✅ Search and fetch endpoints
- ✅ Multiple output types
- ✅ Deep research capability
- ✅ Content extraction
- ✅ JavaScript rendering
- ✅ Advanced filtering

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs via issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

MIT License - See LICENSE file for details.

---

## 📞 Support

For issues or questions:
1. Check relevant README files
2. Review documentation in this directory
3. Visit API provider dashboards for key issues

---

**Happy Searching! 🚀**

*Two powerful search tools for different use cases - choose the one that fits your needs best.*
