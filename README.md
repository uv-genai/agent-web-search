# Agent Web Search

A comprehensive Python-based web search toolkit providing two powerful search tools for different use cases, packaged as a modern Python project using `uv` for dependency management and `hatchling` as the build backend.

## 📋 Project Description

### 🔹 Brave Search Tool (`brave-search`)
Privacy-focused search using Brave's independent search index. Perfect for simple queries, fast results, and privacy-conscious users.

### 🔹 Linkup Search Tool (`linkup-search`)
AI-specific agentic search with superior factuality (#1 on SimpleQA benchmark). Ideal for complex research, factual accuracy, and content extraction.

## 🎯 Key Features

### Brave Search Tool
- ✅ Command-line interface with intuitive arguments
- ✅ Customizable result count (1-100 results)
- ✅ JSON output mode for coding agents
- ✅ Brave Search API integration
- ✅ Privacy-focused - independent index, no tracking
- ✅ Fast responses (~1-3 seconds)
- ✅ Free tier: 2,000 queries/month

### Linkup Search Tool
- ✅ Agentic search with deep research capability
- ✅ Superior factuality - SOTA performance
- ✅ Multiple output types (searchResults, sourcedAnswer, structured)
- ✅ Built-in content fetching (/fetch endpoint)
- ✅ JavaScript rendering support
- ✅ Advanced filtering (dates, domains)
- ✅ Markdown extraction from web pages

### Shared Features
- ✅ Environment variable authentication
- ✅ Comprehensive error handling
- ✅ Timeout protection
- ✅ Input validation
- ✅ Dual output modes (text + JSON)
- ✅ Multi-word query support

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

## 🏗️ Project Structure

```
ws/
├── pyproject.toml              # Project configuration with hatchling
├── README.md                   # Main documentation (this file)
├── src/
│   └── agent_web_search/
│       ├── __init__.py         # Package initialization
│       ├── brave_search.py     # Brave Search CLI tool
│       └── linkup_search.py    # Linkup Search CLI tool
├── tests/
│   ├── __init__.py
│   ├── test_brave_search.py    # Brave Search tests
│   └── test_linkup_search.py   # Linkup Search tests
└── .env.example                # Environment variables template
```

## 🚀 Quick Start

### Installation with uv

```bash
# Navigate to project directory
cd /path/to/ws

# Create virtual environment and install dependencies
uv sync

# Activate virtual environment
uv run python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

### Setup API Keys

```bash
# Get Brave Search API key from https://api-dashboard.search.brave.com/
export BRAVE_API_KEY="your-brave-api-key-here"

# Get Linkup API key from https://app.linkup.so/
export LINKUP_API_KEY="your-linkup-api-key-here"
```

Or create a `.env` file in the project root:

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Usage

#### Brave Search

```bash
# Basic search
uv run brave-search "python web scraping" -n 5

# JSON output
uv run brave-search "machine learning" --json

# With specific count
uv run brave-search "web development" -n 10 --json
```

#### Linkup Search

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

## 🛠️ Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/agent_web_search --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_brave_search.py -v
```

### Code Quality

```bash
# Format code
uv run ruff format src tests

# Check code quality
uv run ruff check src tests

# Type checking
uv run mypy src
```

### Building Distribution

```bash
# Build package
uv build

# Install from build
uv pip install dist/*.whl
```

## 📊 Performance Metrics

| Metric | Brave Search | Linkup Search |
|--------|-------------|---------------|
| Response Time (standard) | ~1-3s | ~1-3s |
| Response Time (deep) | N/A | ~5-10s |
| Factuality Score | Good | SOTA (#1) |
| Citation Quality | Good | Excellent |
| Complex Query Handling | Moderate | Excellent |
| Content Extraction | None | Full page fetch |

## 📚 Additional Resources

- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Linkup API Documentation](https://docs.linkup.so/pages/documentation/api-reference)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Hatchling Documentation](https://hatch.pypa.io/)

## 🤝 Contributing

Contributions welcome! Please feel free to:
- Report bugs via issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

MIT License - See LICENSE file for details.

## 📦 Project Metadata

- **Name**: agent-web-search
- **Version**: 2.0.0
- **Python**: >=3.9
- **Build System**: hatchling
- **Package Manager**: uv
- **License**: MIT
- **Author**: Ugo

---

*Built with ❤️ using uv and hatchling*