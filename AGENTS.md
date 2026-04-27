# Web Search Scripts - Project Documentation

**Version:** 2.0.1  
**Last Updated:** 2026-04-27  
**License:** MIT

---

## 📋 Project Description

A comprehensive Python-based web search toolkit providing two powerful search tools for different use cases:

### 🔹 Brave Search Script (`search.py`)
Privacy-focused search using Brave's independent search index. Perfect for simple queries, fast results, and privacy-conscious users.

### 🔹 Linkup Search Script (`linkup_search.py`)
AI-specific agentic search with superior factuality (#1 on SimpleQA benchmark). Ideal for complex research, factual accuracy, and content extraction.

---

## 🎯 Key Features

### Brave Search Script
- ✅ **Command-line interface** with intuitive arguments
- ✅ **Customizable result count** (1-100 results)
- ✅ **JSON output mode** for coding agents
- ✅ **Brave Search API** integration
- ✅ **Privacy-focused** - independent index, no tracking
- ✅ **Fast responses** (~1-3 seconds)
- ✅ **Free tier**: 2,000 queries/month

### Linkup Search Script
- ✅ **Agentic search** with deep research capability
- ✅ **Superior factuality** - SOTA performance
- ✅ **Multiple output types** (searchResults, sourcedAnswer, structured)
- ✅ **Built-in content fetching** (/fetch endpoint)
- ✅ **JavaScript rendering** support
- ✅ **Advanced filtering** (dates, domains)
- ✅ **Markdown extraction** from web pages

### Shared Features
- ✅ Environment variable authentication
- ✅ Comprehensive error handling
- ✅ Timeout protection
- ✅ Input validation
- ✅ Dual output modes (text + JSON)
- ✅ Multi-word query support

---

## 🆚 Feature Comparison

| Feature | Brave Search | Linkup Search |
|---------|-------------|---------------|
| Search Mode | ✅ Yes | ✅ Yes |
| Content Fetching | ❌ No | ✅ Yes |
| Output Types | Basic | 3 types |
| Deep Research | ❌ No | ✅ Yes |
| Date Filtering | ✅ Yes | ✅ Yes |
| Domain Filtering | ✅ Yes | ✅ Yes |
| JavaScript Render | ❌ No | ✅ Yes |
| Markdown Output | ❌ No | ✅ Yes |
| Factuality | Good | ⭐ SOTA |
| Free Tier | 2,000/mo | Available |
| Speed | Fast | Fast/Deep |

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

## 🏗️ Design Decisions

### Why Two Separate Scripts?

1. **Different Use Cases**: Brave excels at quick, private searches; Linkup shines in AI/factual scenarios
2. **API Specialization**: Each service has unique strengths optimized for different workflows
3. **Cost Efficiency**: Users can choose the right tool without paying for unused features
4. **Flexibility**: Developers can integrate both for maximum coverage

### Architecture Choices

**Single-file design**: Both main scripts are self-contained with all functionality in one file for easy maintenance and deployment.

**Environment variable authentication**: API keys stored in `BRAVE_API_KEY` and `LINKUP_API_KEY` environment variables for security and flexibility.

**Dual output modes**: Both human-readable text and machine-readable JSON outputs serve different use cases without code duplication.

**Validation layer**: Input validation ensures result counts are within acceptable bounds (1-100) to prevent abuse and errors.

### Technology Stack

- **Python 3.7+**: Modern, widely-supported Python version
- **requests**: Industry-standard HTTP library
- **argparse**: Built-in argument parsing
- **json**: Native JSON support for structured output

---

## 💻 Implementation Details

### File Structure

```
agent-web-search/
├── pyproject.toml            # Project configuration with hatchling
├── CHANGELOG.md              # Version history
├── README.md                 # Main documentation
├── AGENTS.md                 # Project documentation (this file)
├── .env.example              # Environment variables template
├── uv.lock                   # Lock file (auto-generated)
├── src/
│   └── agent_web_search/
│       ├── __init__.py       # Package initialization
│       ├── brave_search.py   # Brave Search CLI tool
│       └── linkup_search.py  # Linkup Search CLI tool
└── tests/
    ├── __init__.py
    ├── test_brave_search.py  # Brave Search tests
    └── test_linkup_search.py # Linkup Search tests
```

### Brave Search Core Components

#### 1. Argument Parsing (`parse_arguments()`)
```python
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Perform a Brave Search and print results to stdout.'
    )
    parser.add_argument('query', nargs='+', help='Search query')
    parser.add_argument('-n', '--num-results', type=int, default=10)
    parser.add_argument('--json', action='store_true', help='JSON output')
```

#### 2. API Integration (`brave_search()`)
```python
def brave_search(query, num_results, json_output=False):
    # Makes request to Brave Search API
    # Endpoint: https://api.search.brave.com/res/v1/web/search
    # Headers include X-Subscription-Token
    # Comprehensive error handling
```

### Linkup Search Core Components

#### 1. Search Mode (`linkup_search()`)
```python
def linkup_search(query, num_results=10, depth='standard', 
                  output_type='searchResults', ...):
    # Uses /v1/search endpoint
    # Supports standard and deep depths
    # Multiple output types: searchResults, sourcedAnswer, structured
    # Advanced filtering: dates, domains
```

#### 2. Fetch Mode (`linkup_fetch()`)
```python
def linkup_fetch(url, output_format='markdown', render_js=False):
    # Uses /v1/fetch endpoint
    # Extracts HTML or Markdown content
    # Optional JavaScript rendering
    # Clean content extraction
```

### Error Handling Strategy

1. **API errors**: Status codes captured and reported with details
2. **Timeout errors**: 30-60 second timeout prevents hanging
3. **Network errors**: Request exceptions caught and reported
4. **JSON errors**: Structured error objects in JSON mode
5. **Input validation**: Result count bounds checked before API call

### Security Considerations

- API keys never hardcoded (environment variables only)
- No user data collected or stored
- HTTPS-only communications
- Input sanitization via argparse
- No shell injection vulnerabilities

---

## 📝 Changelog

### Version 2.0.1 (2026-04-27)

**Bug Fix: Linkup fetch mode returning empty content**

#### Fixed
- 🐛 **Linkup fetch mode returning empty content** — API response key is `"markdown"` not `"content"`; updated `linkup_fetch()` to read the correct key

#### Files Modified (v2.0.1)
- `src/agent_web_search/linkup_search.py` — Fixed `linkup_fetch()` to use `data.get("markdown", "")` instead of `data.get("content", "")`

### Version 2.0.0 (2026-02-28)

**Major Update: Added Linkup Search Script & Fixed Critical Bug**

#### Added
- ✅ **Linkup Search Script** (`linkup_search.py`)
  - Agentic search with deep research capability
  - Search and fetch endpoints
  - Multiple output types (searchResults, sourcedAnswer, structured)
  - JavaScript rendering support
  - Date and domain filtering
  - Markdown extraction
- ✅ **Documentation Updates**
  - `README_LINKUP.md` - Detailed Linkup documentation
  - `FEATURES_LINKUP.md` - Linkup feature guide
  - `PROJECT_SUMMARY.md` - Combined project overview
  - `FEATURES_LINKUP.md` - Comprehensive feature comparison
- ✅ **Testing Tools**
  - `test_linkup.py` - Linkup demo script
  - `test_linkup_api.py` - Diagnostic tool
- ✅ **Bug Fix**
  - Fixed response parsing in Linkup script (results vs sources key)
  - Verified all search operations working correctly

#### Improved
- ✅ **Updated README.md** to include both scripts
- ✅ **Enhanced error handling** in Linkup script
- ✅ **Added comprehensive documentation** for Linkup features
- ✅ **Created diagnostic tools** for troubleshooting

#### Technical Specifications

**Brave Search Script**:
- **Language**: Python 3.7+
- **Dependencies**: requests, argparse, json (stdlib)
- **API**: Brave Search API (free tier: 2,000 queries/month)
- **Output formats**: Text (human), JSON (machine)
- **Result limit**: 1-100 results per query
- **Timeout**: 30 seconds

**Linkup Search Script**:
- **Language**: Python 3.7+
- **Dependencies**: requests, argparse, json (stdlib)
- **API**: Linkup API (https://app.linkup.so/)
- **Endpoints**: /v1/search, /v1/fetch
- **Output formats**: Text, JSON, Markdown
- **Search depths**: Standard, Deep
- **Output types**: searchResults, sourcedAnswer, structured
- **Timeout**: 60 seconds

#### New Use Cases Enabled
- AI agent integrations requiring high-factuality responses
- Research assistants with deep search capabilities
- Content aggregation with page fetching
- Competitive analysis with domain filtering
- Fact-checking with cited sources
- Chatbot enhancements with grounded responses
- Web scraping with JavaScript rendering

#### Files Created (v2.0.0)
- `linkup_search.py` - Main Linkup executable script
- `requirements_linkup.txt` - Linkup dependency specification
- `README_LINKUP.md` - Linkup user documentation
- `FEATURES_LINKUP.md` - Linkup feature guide
- `PROJECT_SUMMARY.md` - Combined project summary
- `test_linkup.py` - Linkup demonstration script
- `test_linkup_api.py` - Linkup diagnostic tool
- `FIX_APPLIED.md` - Bug fix documentation

#### Files Modified (v2.0.0)
- `AGENTS.md` - Updated with both scripts documentation
- `README.md` - Added Linkup script section
- `FEATURES_SUMMARY.md` - Added comparative analysis
- `.gitignore` - Updated for new files

### Version 1.0.0 (2026-02-28)

**Initial Release**

#### Added
- ✅ Brave Search API integration
- ✅ Command-line interface with argparse
- ✅ Customizable result count (`-n` / `--num-results` flag)
- ✅ JSON output mode for coding agents (`--json` flag)
- ✅ Human-readable formatted output
- ✅ Comprehensive error handling
- ✅ Input validation (result count 1-100)
- ✅ Timeout protection (30 seconds)
- ✅ Multi-word query support
- ✅ Environment variable authentication
- ✅ Full documentation (README, AGENTS, examples)
- ✅ Test scripts for demonstration
- ✅ MIT License

---

## 🚀 Quick Start

### Setup Both Scripts

```bash
# 1. Sync dependencies (creates .venv if needed)
uv sync

# 2. Get API keys
export BRAVE_API_KEY="your-brave-api-key-here"
export LINKUP_API_KEY="your-linkup-api-key-here"
```

### Brave Search Usage

```bash
# Basic search
uv run brave-search "python web scraping" -n 5

# JSON output
uv run brave-search "machine learning" --json

# With specific count
uv run brave-search "web development" -n 10 --json
```

### Linkup Search Usage

```bash
# Basic search
uv run linkup-search search "open source licenses" -n 5

# Deep research
uv run linkup-search search "AI trends 2026" --depth deep -n 10

# JSON output
uv run linkup-search search "python tutorials" -n 5 --json

# Fetch webpage content
uv run linkup-search fetch "https://docs.python.org"

# With filters
uv run linkup-search search "machine learning" \
  --from-date 2026-01-01 \
  --include-domains arxiv.org \
  -n 10
```

---

## 📊 Performance Metrics

| Metric | Brave Search | Linkup Search |
|--------|-------------|---------------|
| Response Time (standard) | ~1-3s | ~1-3s |
| Response Time (deep) | N/A | ~5-10s |
| Factuality Score | Good | SOTA (#1) |
| Citation Quality | Good | Excellent |
| Complex Query Handling | Moderate | Excellent |
| Content Extraction | None | Full page fetch |

---

## 📚 Additional Resources

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [Example JSON Output Guide](./EXAMPLE_JSON_OUTPUT.md)
- [Brave Search Features](./FEATURES_SUMMARY.md)
- [Linkup Search Features](./FEATURES_LINKUP.md)
- [Project Overview](./PROJECT_SUMMARY.md)
- [User Documentation](./README.md)
- [Linkup User Docs](./README_LINKUP.md)

---

## 🤝 Contributing

Contributions welcome! Please feel free to:
- Report bugs via issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

MIT License - See LICENSE file for details.

---

*Generated by version-commit-tag skill on 2026-04-27*
