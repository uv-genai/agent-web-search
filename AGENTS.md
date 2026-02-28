# Brave Search Script - Project Documentation

**Version:** 1.0.0  
**Last Updated:** 2026-02-28  
**License:** MIT

---

## 📋 Project Description

A Python-based web search tool that uses the Brave Search API to perform privacy-focused searches with flexible output options for both humans and coding agents.

### Key Features

- **Command-line interface** with intuitive arguments
- **Customizable result count** using `-n` or `--num-results` flag (1-100 results)
- **JSON output mode** for coding agents using `--json` flag
- **Brave Search API** integration for reliable, fast results
- **Privacy-focused** - uses Brave's independent search index
- **Clean output** - formatted titles, URLs, and descriptions for human readability
- **Machine-readable output** - structured JSON for programmatic use

### Target Users

- Developers building search integrations
- AI agents and automation workflows
- Researchers needing quick information gathering
- Content creators requiring source verification
- Anyone preferring privacy-focused search over Google

---

## 🎯 Design Decisions

### Why Brave Search API?

1. **Reliability**: No browser automation issues like Selenium
2. **Speed**: Fast API responses (~1-3 seconds)
3. **Scalability**: Handle hundreds of queries per hour
4. **Privacy**: Independent index, no tracking or profiling
5. **Cost**: Free tier includes 2,000 queries/month
6. **Simplicity**: Lightweight requests-based implementation

### Architecture Choices

**Single-file design**: The main script (`search.py`) is self-contained with all functionality in one file for easy maintenance and deployment.

**Environment variable authentication**: API key stored in `BRAVE_API_KEY` environment variable for security and flexibility across different environments.

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
ws/
├── search.py              # Main script (all features)
├── requirements.txt       # Dependencies
├── README.md             # User documentation
├── AGENTS.md             # Project documentation (this file)
├── EXAMPLE_JSON_OUTPUT.md # JSON usage examples
├── FEATURES_SUMMARY.md   # Complete feature guide
├── test_json_output.py   # Demo/test script
└── venv/                 # Virtual environment
```

### Core Components

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

**Features**:
- Supports multi-word queries via `nargs='+'`
- Validates result count range (1-100)
- Boolean flag for JSON mode

#### 2. API Integration (`brave_search()`)

```python
def brave_search(query, num_results, json_output=False):
    # Makes request to Brave Search API
    # Handles both text and JSON output formats
    # Comprehensive error handling
```

**Key aspects**:
- Uses Brave Search API endpoint: `https://api.search.brave.com/res/v1/web/search`
- Implements proper headers including `X-Subscription-Token`
- Timeout protection (30 seconds)
- Error responses in both formats

#### 3. Output Formatting

**Human-readable format**:
```
============================================================
Brave Search Results for: python web scraping
Showing 5 results
============================================================

1. GeeksforGeeks
   URL: https://...
   Description: Learn Python web scraping...
```

**JSON format**:
```json
{
  "query": "python web scraping",
  "num_results_requested": 5,
  "num_results_found": 42,
  "results": [
    {
      "title": "GeeksforGeeks",
      "url": "https://...",
      "description": "...",
      "engine": "brave_search"
    }
  ]
}
```

### Error Handling Strategy

1. **API errors**: Status codes captured and reported with details
2. **Timeout errors**: 30-second timeout prevents hanging
3. **Network errors**: Request exceptions caught and reported
4. **JSON errors**: Structured error objects in JSON mode
5. **Input validation**: Result count bounds checked before API call

### Security Considerations

- API key never hardcoded (environment variable only)
- No user data collected or stored
- HTTPS-only communications
- Input sanitization via argparse
- No shell injection vulnerabilities

---

## 📝 Changelog

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

#### Technical Specifications
- **Language**: Python 3.7+
- **Dependencies**: requests, argparse, json (stdlib)
- **API**: Brave Search API (free tier: 2,000 queries/month)
- **Output formats**: Text (human), JSON (machine)
- **Result limit**: 1-100 results per query
- **Timeout**: 30 seconds
- **Error handling**: Comprehensive with dual-format reporting

#### Use Cases Enabled
- AI agent integrations (LangChain, CrewAI, AutoGen)
- Shell script automation with jq/grep
- Python/Node.js application integration
- Research and content creation workflows
- Privacy-focused web searching

#### Files Created
- `search.py` - Main executable script
- `requirements.txt` - Dependency specification
- `README.md` - User documentation
- `AGENTS.md` - Project documentation
- `EXAMPLE_JSON_OUTPUT.md` - JSON usage guide
- `FEATURES_SUMMARY.md` - Complete feature list
- `test_json_output.py` - Demonstration script

---

## 🚀 Quick Start

```bash
# 1. Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Get API key from https://api-dashboard.search.brave.com/
export BRAVE_API_KEY="your-api-key-here"

# 4. Run searches
python search.py "python web scraping" -n 5                    # Human-readable
python search.py "machine learning" --json                     # JSON output
python search.py "web development" -n 10 --json                # Both options
```

---

## 📚 Additional Resources

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Example JSON Output Guide](./EXAMPLE_JSON_OUTPUT.md)
- [Feature Summary](./FEATURES_SUMMARY.md)
- [User Documentation](./README.md)

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

*Generated by version-commit-tag skill on 2026-02-28*
